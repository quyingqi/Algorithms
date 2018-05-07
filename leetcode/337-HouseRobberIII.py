__author__ = 'cookie'
# -*- coding: utf-8 -*-
#  2018/5/7 11:16

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root): # 递归：对于每个节点，取/不取。 【超时，因为对各个节点有重复计算】
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        val = root.val
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        return max(val, self.rob(root.left)+self.rob(root.right))

    def rob2(self, root): # 递归+哈希表：把算过的节点的值存下来，避免重复计算
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dic = {}
        return self.iter(root)

    def iter(self, root):
        if not root:
            return 0
        if root in self.dic:
            return self.dic[root]
        val = root.val
        if root.left:
            val += self.iter(root.left.left) + self.iter(root.left.right)
        if root.right:
            val += self.iter(root.right.left) + self.iter(root.right.right)
        res = max(val, self.iter(root.left)+self.iter(root.right))
        self.dic[root] = res
        return res

    def rob3(self, root): # 递归时把取和不取的值都返回，可以避免重复计算，同时不需要额外记录。
        """
        :type root: TreeNode
        :rtype: int
        """
        yes, no = self.iter(root)
        return max(yes, no)

    def iter3(self, root):
        if not root:
            return 0, 0
        left = self.iter3(root.left)
        right = self.iter3(root.right)
        yes = root.val + left[1] + right[1]  # 加入当前节点（左右孩子不加入）
        no = max(left) + max(right)  # 不加入当前节点（左右孩子分别 加入or不加入取最大值）
        return yes, no

if __name__ == '__main__':
    pass