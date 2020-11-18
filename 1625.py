import unittest


def findLexSmallestString(self, s: str, a: int, b: int) -> str:
    queue = [s]
    ans = s
    seen = set()
    while queue:
        size = len(queue)
        for i in range(size):
            current = queue.pop()
            ans = min(current, ans)
            rotate = current[b:] + current[:b]
            if rotate not in seen:
                seen.add(rotate)
                queue.append(rotate)
            t = transform(current, a)
            if t not in seen:
                seen.add(t)
                queue.append(t)
    return ans


def transform(s: str, delta: int):
    ans = ''
    for i, c in enumerate(s):
        if i % 2 == 1:
            ans += str((int(c) + delta) % 10)
        else:
            ans += c
    return ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('2050', findLexSmallestString(self, '5525', 5, 2))


if __name__ == '__main__':
    unittest.main()
