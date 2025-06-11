"""Helpers for fetching off-chain sentiment and listings."""

import os
from typing import List, Dict

import aiohttp

TWITTER_SEARCH_URL = "https://api.twitter.com/2/tweets/search/recent"

async def get_twitter_mentions(token_symbol: str, session: aiohttp.ClientSession) -> int:
    """Return the number of recent Twitter mentions for ``token_symbol``."""

    bearer = os.getenv("TWITTER_BEARER_TOKEN")
    if not bearer:
        return 0

    headers = {"Authorization": f"Bearer {bearer}"}
    params = {"query": token_symbol, "max_results": 10}

    try:
        async with session.get(TWITTER_SEARCH_URL, params=params, headers=headers) as resp:
            data = await resp.json()
        return int(data.get("meta", {}).get("result_count", 0))
    except Exception:
        return 0


async def get_new_pools(session: aiohttp.ClientSession) -> List[Dict[str, str]]:
    """Fetch recently created pools from the Raydium API."""

    try:
        async with session.get("https://api.raydium.io/v2/main/pairs") as resp:
            data = await resp.json()
    except Exception:
        return []

    pools = []
    for pair in data[:5]:  # take only a handful for demo
        pools.append({"mint_address": pair.get("baseMint"), "symbol": pair.get("name", "").split("/")[0]})

    return pools
