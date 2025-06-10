"""Scoring utilities for evaluating Solana meme coins."""

from typing import List, Dict, Tuple


def rug_check(metadata: Dict[str, str], liquidity: Dict[str, float], holders: List[Dict[str, float]], custom_program: bool) -> Tuple[bool, List[str]]:
    """Evaluate basic rug pull risk.

    Returns
    -------
    Tuple[bool, List[str]]
        ``True`` if the token appears safe and a list of issues otherwise.
    """
    issues = []
    if metadata.get("mint_authority") is not None or metadata.get("freeze_authority") is not None:
        issues.append("Mint or freeze authority active")
    if not liquidity.get("lp_locked", False):
        issues.append("Liquidity not locked")
    total_pct = sum(holder.get("percentage", 0) for holder in holders[:10])
    if total_pct > 30:
        issues.append("Top holders exceed 30%")
    if custom_program:
        issues.append("Custom program suspicious")
    return len(issues) == 0, issues


def potential_score(volume_24h: float, volume_growth: float, liquidity_growth: float, dev_activity: float, social_mentions: int) -> float:
    """Calculate a simple potential score using weighted factors."""
    score = 0.0
    score += volume_24h * 0.4
    score += volume_growth * 0.2
    score += liquidity_growth * 0.2
    score += dev_activity * 0.1
    score += social_mentions * 0.1
    return score
