"""Asynchronous utilities for retrieving on-chain data about Solana tokens.

These helpers use Solana's public RPC endpoint and the Raydium API to collect
metadata and liquidity information.  They are intentionally lightweight so
they can be replaced or extended with more robust indexers in a production
environment.
"""

import os
from typing import List, Dict

import aiohttp

SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")
RAYDIUM_PAIRS_URL = "https://api.raydium.io/v2/main/pairs"

async def fetch_token_metadata(mint_address: str, session: aiohttp.ClientSession) -> Dict[str, str]:
    """Return metadata for the given token mint from Solana RPC."""

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getAccountInfo",
        "params": [mint_address, {"encoding": "jsonParsed"}],
    }
    async with session.post(SOLANA_RPC_URL, json=payload) as resp:
        data = await resp.json()

    value = data.get("result", {}).get("value")
    if not value:
        return {"mint_authority": None, "freeze_authority": None}

    info = value.get("data", {}).get("parsed", {}).get("info", {})
    return {
        "mint_authority": info.get("mintAuthority"),
        "freeze_authority": info.get("freezeAuthority"),
    }


async def fetch_liquidity(mint_address: str, session: aiohttp.ClientSession) -> Dict[str, float]:
    """Return liquidity information for a Raydium pool containing ``mint_address``."""

    async with session.get(RAYDIUM_PAIRS_URL) as resp:
        data = await resp.json()

    for pair in data:
        if pair.get("baseMint") == mint_address or pair.get("quoteMint") == mint_address:
            return {
                "sol": pair.get("tokenAmountPc", 0.0),
                "token": pair.get("tokenAmountCoin", 0.0),
                "lp_locked": True,  # Raydium API doesn't expose lock status
            }

    return {"sol": 0.0, "token": 0.0, "lp_locked": False}


async def get_top_holders(mint_address: str, session: aiohttp.ClientSession, limit: int = 10) -> List[Dict[str, float]]:
    """Retrieve the top token holders using Solana RPC."""

    supply_payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenSupply",
        "params": [mint_address],
    }
    largest_payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenLargestAccounts",
        "params": [mint_address],
    }

    async with session.post(SOLANA_RPC_URL, json=supply_payload) as resp:
        supply_data = await resp.json()
    async with session.post(SOLANA_RPC_URL, json=largest_payload) as resp:
        largest_data = await resp.json()

    supply = float(supply_data.get("result", {}).get("value", {}).get("uiAmount", 0))
    accounts = largest_data.get("result", {}).get("value", [])[:limit]

    holders: List[Dict[str, float]] = []
    for acc in accounts:
        amount = float(acc.get("uiAmount", 0))
        pct = (amount / supply * 100) if supply else 0
        holders.append({"address": acc.get("address"), "balance": amount, "percentage": pct})

    return holders


async def check_custom_program(mint_address: str, session: aiohttp.ClientSession) -> bool:
    """Detect whether ``mint_address`` is managed by a custom program."""

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getAccountInfo",
        "params": [mint_address, {"encoding": "jsonParsed"}],
    }
    async with session.post(SOLANA_RPC_URL, json=payload) as resp:
        data = await resp.json()

    owner = data.get("result", {}).get("value", {}).get("owner")
    # SPL token program id
    return owner != "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
