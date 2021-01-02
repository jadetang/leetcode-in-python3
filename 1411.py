import unittest
from typing import List


def numOfWays(n: int) -> int:
    dp = [[0] * 3 for i in range(3 * n)]

    dp[0][0], dp[0][1], dp[0][2] = 1, 1, 1

    mod = 1_000_000_009
    for col in range(n):
        for color in range(3):
            if col == 0:
                continue
            if col < 3:
                for nextColor in range(0, 3):
                    if color != nextColor:
                        dp[col][color] = (dp[col][color] + dp[col - 1][nextColor]) % mod
            else:
                preCol = col - 3
                for nextColor1 in range(0, 3):
                    for nextColor2 in range(0, 3):
                        if color != nextColor1 and color != nextColor2:
                            dp[col][color] = (dp[col - 1][nextColor1] + dp[preCol][nextColor2] + dp[col][color]) % mod
    print(dp)
    return sum(dp[n - 1])


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(12, numOfWays(1))


if __name__ == '__main__':
    unittest.main()
