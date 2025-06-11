import aiohttp
import asyncio
import unittest
from aioresponses import aioresponses

from solana_bot.onchain import fetch_token_metadata, get_top_holders
from solana_bot.offchain import get_twitter_mentions

SOL_RPC = "https://api.mainnet-beta.solana.com"

class TestOnChain(unittest.IsolatedAsyncioTestCase):
    async def test_fetch_token_metadata(self):
        response = {
            "result": {
                "value": {
                    "data": {"parsed": {"info": {"mintAuthority": None, "freezeAuthority": None}}},
                    "owner": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                }
            }
        }
        with aioresponses() as m:
            m.post(SOL_RPC, payload=response)
            async with aiohttp.ClientSession() as session:
                meta = await fetch_token_metadata("mint", session)
        self.assertIsNone(meta["mint_authority"])

    async def test_get_top_holders(self):
        supply_resp = {"result": {"value": {"uiAmount": 1000}}}
        largest_resp = {"result": {"value": [{"address": "a", "uiAmount": 100}]}}
        with aioresponses() as m:
            m.post(SOL_RPC, payload=supply_resp)
            m.post(SOL_RPC, payload=largest_resp)
            async with aiohttp.ClientSession() as session:
                holders = await get_top_holders("mint", session, limit=1)
        self.assertEqual(len(holders), 1)
        self.assertAlmostEqual(holders[0]["percentage"], 10.0)

class TestOffChain(unittest.IsolatedAsyncioTestCase):
    async def test_get_twitter_mentions_no_token(self):
        async with aiohttp.ClientSession() as session:
            mentions = await get_twitter_mentions("ABC", session)
        self.assertEqual(mentions, 0)
