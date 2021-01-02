class Node:
    def __init__(self, left, right, leftNode, rightNode, value, nums):
        self.left = left
        self.right = right
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.value = value
        self.nums = nums


class Tree:
    def __init__(self, nums):
        def build(nums, left, right):
            if left == right:
                return Node(left, right, None, None, True, nums[left])
            mid = left + (right - left) // 2
            leftNode = build(nums, left, mid)
            rightNode = build(nums, mid + 1, right)
            if not leftNode.value or not rightNode.value or leftNode.nums != rightNode.nums:
                return Node(left, right, leftNode, rightNode, False, None)
            else:
                return Node(left, right, leftNode, rightNode, True, leftNode.nums)

        self.nums = nums
        self.root = build(nums, 0, len(nums) - 1)

    def query(self, i, j):
        def q(node, i, j):
            if node.left == i and node.right == j:
                return node.value, node.nums
            mid = node.left + (node.right - node.left) // 2
            if mid >= j:
                return q(node.leftNode, i, j)
            elif i >= mid + 1:
                return q(node.rightNode, i, j)
            else:
                leftResult = q(node.left, i, mid)
                rightResult = q(node.right, mid + 1, j)
                if not leftResult[0] or rightResult[0] or leftResult[1] != rightResult[1]:
                    return False, None
                else:
                    return True, leftResult[1]
        return q(self.root, i, j)[0]


class Solution:
    def solve(self, nums, queries):
        if not nums or not queries:
            return 0
        if len(nums) == 1:
            return len(queries)
        ans = 0
        diff = [0] * (len(nums) - 1)
        for i in range(0, len(nums) - 1):
            diff[i] = nums[i + 1] - nums[i]
        tree = Tree(diff)
        for left, right in queries:
            if left == right or left + 1 == right:
                ans += 1
            else:
                diff = tree.query(left, right - 1)
                #print(left, right, diff)
                if len(diff) == 1:
                    ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([1,3,5,7,6,5,4,1], [[0,3],[3,4],[2,4]]))
