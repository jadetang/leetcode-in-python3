import unittest


def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    if len(s) == 0:
        return 0
    first = {}
    ans = 0
    for i, c in enumerate(s):
        print(first)
        if c not in first:
            first[c] = i
        else:
            ans = max(ans, i - first[c] - 1)
    return ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(4, maxLengthBetweenEqualCharacters(self, 'cabbac'))


if __name__ == '__main__':
    unittest.main()
