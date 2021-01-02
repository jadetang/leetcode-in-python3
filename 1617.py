import unittest
from typing import List

def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
    def diameter(edges: List[List[int]]) -> int:
        start = -1
        for i, l in enumerate(edges):
            if l:
                start = i
                break
        if start == -1:
            return 0
    

    def maxDistance(n: int) -> int:
        graph = [[]] * 16
        for i in range(1, 16):
            if n & (1 << i) > 0:
                for j in edges[i]:
                    if n | (1 << j) > 0:
                        graph[i].append(j)
        return diameter(graph)

    ans = [0] * (n - 1)
    for i in range(1, 1 << n):
        distance = maxDistance(n)
        ans[distance] = ans[distance] + 1
    return ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(4, countSubgraphsForEachDiameter(self, 'cabbac'))


if __name__ == '__main__':
    unittest.main()
