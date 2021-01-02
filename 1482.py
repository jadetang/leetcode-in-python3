import sys
import unittest
from collections import defaultdict
from typing import List


def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

    totalFlowers = len(bloomDay)

    def canMake(days, m, k):
        flowers = [0] * totalFlowers
        for (i, day) in days:
            for d in day:
                flowers[d] = 1
        i = 0
        while i < len(flowers):
            if flowers[i] == 1:
                j = i
                while j < len(flowers) and flowers[j] == 1:
                    j += 1
                    length = j - i
                    if length == k:
                        m -= 1
                        break
                i = j
            else:
                i += 1
        return m <= 0

    daysFlower = defaultdict(list)
    for i, day in enumerate(bloomDay):
        daysFlower[day].append(i)
    daysFlowerList = list(daysFlower.items())
    daysFlowerList.sort()

    if not canMake(daysFlowerList, m, k):
        return -1

    left = 0
    right = len(daysFlowerList)

    while left < right:
        mid = left + (right - left) // 2
        if canMake(daysFlowerList[:mid + 1], m, k):
            right = mid
        else:
            left = mid + 1
    return daysFlowerList[left][0]


class MyTestCase(unittest.TestCase):
    def test_something(self):
    #    print(minDays(self, [1, 10, 3, 10, 2], 3, 1))
        print(minDays(self, [7,7,7,7,12,7,7], 2, 3))

if __name__ == '__main__':
    unittest.main()
