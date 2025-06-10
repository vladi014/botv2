import unittest
from solana_bot.scoring import rug_check, potential_score

class TestScoring(unittest.TestCase):
    def test_rug_check_pass(self):
        metadata = {"mint_authority": None, "freeze_authority": None}
        liquidity = {"lp_locked": True}
        holders = [{"percentage": 2.0} for _ in range(10)]
        safe, issues = rug_check(metadata, liquidity, holders, False)
        self.assertTrue(safe)
        self.assertEqual(len(issues), 0)

    def test_rug_check_fail(self):
        metadata = {"mint_authority": "abc", "freeze_authority": None}
        liquidity = {"lp_locked": False}
        holders = [{"percentage": 5.0} for _ in range(10)]
        safe, issues = rug_check(metadata, liquidity, holders, True)
        self.assertFalse(safe)
        self.assertGreaterEqual(len(issues), 1)

    def test_potential_score(self):
        score = potential_score(1000, 10, 5, 2, 50)
        self.assertGreater(score, 0)

if __name__ == '__main__':
    unittest.main()
