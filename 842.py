import unittest
from typing import List


class Solution:

    def __init__(self):
        self.ans = []
        self.found = False

    def splitIntoFibonacci(self, array: str) -> List[int]:
        def backtrack(index, path):
            if self.found:
                return
            if index >= len(array):
                if len(path) >= 3:
                    self.ans = path.copy()
                    self.found = True
                return
            if array[index] == '0':
                if len(path) < 2 or (len(path) >= 2 and path[-1] + path[-2] == 0):
                    path.append(0)
                    backtrack(index + 1, path)
                    path.pop()
                return
            i = index
            while i < len(array) and not self.found:
                number = int(array[index:i + 1])
                if len(path) < 2 or (len(path) >= 2 and path[-1] + path[-2] == number):
                    path.append(number)
                    backtrack(i + 1, path)
                    path.pop()
                i += 1
        backtrack(0, [])
        return self.ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        solution.splitIntoFibonacci('1320581321313221264343965566089105744171833277577')


if __name__ == '__main__':
    unittest.main()
