# 2017-11-30

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        res = []
        self.find_path(root, sum, res, [])
        return res

    def find_path(self, root, sum, res, path):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            if sum == root.val:
                res.append(path)
                print(res)
            return
        self.find_path(root.left, sum-root.val, res, path[:])
        self.find_path(root.right, sum-root.val, res, path[:])
        return

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.left.left = TreeNode(18)
    root.left.right = TreeNode(11)
    s = Solution()
    s.pathSum(root, 30)
