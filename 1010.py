import unittest
from typing import List


def numPairsDivisibleBy60(self, time: List[int]) -> int:
    count = dict()
    for i in time:
        count[i % 60] = count.get(i % 60, 0) + 1
    ans = 0
    for mod, value in count.items():
        if mod > 30:
            continue
        if mod == 0 or mod == 30:
            ans += value * (value - 1) // 2
            continue
        ans += value * count.get(60 - mod, 0)
    return ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(3, numPairsDivisibleBy60(self, [30, 20, 150, 100, 40]))


if __name__ == '__main__':
    unittest.main()
