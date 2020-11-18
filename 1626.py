import unittest
from typing import List


def bestTeamScore(scores: List[int], ages: List[int]) -> int:
    data = list(zip(scores, ages))
    n = len(scores)
    data.sort(key=lambda tup: (tup[1], tup[0]))
    dp = [data[i][0] for i in range(n)]
    for i in range(n):
        for j in range(i):
            if data[i][0] >= data[j][0]:
                dp[i] = max(dp[i], data[i][0] + dp[j])
    return max(dp)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(34, bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
