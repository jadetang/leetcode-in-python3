import unittest

from Tree import Tree
from typing import List


def solve(root: Tree) -> bool:
    queue: List[Tree] = [root]
    meet_empty = False
    while root:
        node = queue.pop()
        if node:
            if meet_empty:
                return False
            queue.append(node.left)
            queue.append(node.right)
        else:
            meet_empty = True
    return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, solve(Tree(1, None, None)))


if __name__ == '__main__':
    unittest.main()
