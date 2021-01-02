import sys
import unittest
from collections import defaultdict
from typing import List


def maxNumOfSubstrings(self, s: str) -> List[str]:

    start = defaultdict(lambda: sys.maxsize)
    end = defaultdict(lambda: -sys.maxsize - 1)
    for i, c in enumerate(s):
        start[c] = min(start[c], i)
        end[c] = max(end[c], i)

    def extend(  startp):
        endp = end[s[startp]]
        for i in range(startp, endp + 1):
            if start[s[i]] < startp:
                return -1
            endp = max(endp, end[s[i]])
        return endp

    ans = []
    lastP = -1
    for i, c in enumerate(s):
        if start[c] != i:
            continue
        endP = extend(i)
        if endP == -1:
            continue
        if start[c] > lastP:
            ans.append('')
        ans[-1] = s[start[c] : endP + 1]
        lastP = endP
    return ans

class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(maxNumOfSubstrings(self, 'adefaddaccc'))

if __name__ == '__main__':
    unittest.main()
