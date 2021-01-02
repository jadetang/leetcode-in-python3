import unittest
from typing import List

def stoneGameVI(aliceValues: List[int], bobValues: List[int]) -> int:
    def score(aliceValues, bobValues, aliceTurn, l, r):
        if l == r:
            return aliceValues[l] if aliceTurn else bobValues[l]
        if aliceTurn:
            return max(aliceValues[l] - score(aliceValues, bobValues, not aliceTurn, l + 1, r),
                       aliceValues[r] - score(aliceValues, bobValues, not aliceTurn, l, r - 1))
        else:
            return max(bobValues[l] - score(aliceValues, bobValues, not aliceTurn, l + 1, r),
                       bobValues[r] - score(aliceValues, bobValues, not aliceTurn, l, r - 1))

    return score(aliceValues, bobValues, 0, len(bobValues) - 1, True)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stoneGameVI([1,2], [3,1 ])


if __name__ == '__main__':
    unittest.main()
