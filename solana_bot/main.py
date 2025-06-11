"""Entry point for the Solana meme coin bot."""

import asyncio
import aiohttp

from .onchain import (
    fetch_token_metadata,
    fetch_liquidity,
    get_top_holders,
    check_custom_program,
)
from .offchain import get_twitter_mentions, get_new_pools
from .scoring import rug_check, potential_score


async def analyze_token(token: dict, session: aiohttp.ClientSession) -> None:
    """Gather on-chain and off-chain data, then print the evaluation."""
    mint = token["mint_address"]
    symbol = token.get("symbol", "")

    metadata = await fetch_token_metadata(mint, session)
    liquidity = await fetch_liquidity(mint, session)
    holders = await get_top_holders(mint, session)
    custom = await check_custom_program(mint, session)

    safe, issues = rug_check(metadata, liquidity, holders, custom)
    if not safe:
        print(f"[RISK] {mint} -> {issues}")
        return

    mentions = await get_twitter_mentions(symbol, session)
    # Placeholder metrics for demo
    volume_24h = 10_000
    volume_growth = 50
    liquidity_growth = 20
    dev_activity = 5
    score = potential_score(
        volume_24h, volume_growth, liquidity_growth, dev_activity, mentions
    )
    print(f"[TOKEN] {mint} score={score:.2f}")


async def monitor() -> None:
    """Continuously fetch new pools and evaluate them."""
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                pools = await get_new_pools(session)
                tasks = [analyze_token(pool, session) for pool in pools]
                await asyncio.gather(*tasks)
            except Exception as exc:
                print(f"Error processing pools: {exc}")
            await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(monitor())
