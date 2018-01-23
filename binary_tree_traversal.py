__author__ = 'cookie'
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTreeTraversal:
    # 1.recursive 递归
    def preorderTraversal_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preorder_helper(root, res)
        return res

    # preorder
    def preorder_helper(self, root, res):
        if not root:
            return res
        res.append(root.val)
        self.preorder_helper(root.left, res)
        self.preorder_helper(root.right, res)

    # inorder
    def inorder_helper(self, root, res):
        if not root:
            return res
        self.inorder_helper(root.left, res)
        res.append(root.val)
        self.inorder_helper(root.right, res)

    # preorder
    def postorder_helper(self, root, res):
        if not root:
            return res
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)

    ##------------------------------------------------------##
    # 2.stack 栈
    # preorder
    def preorderTraversal_2(self, root):
        res = []
        stack = []
        while(root or stack):


    # inorder
    def inorderTraversal_2(self, root):
        res = []
        stack = []
        while(root or stack):
            while(root):
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node)
            root = node.right
        return res

    def postorderTraversal_2(self, root):

    ##------------------------------------------------------##
    # 3.Morris Traversal
    def preorderTraversal_3(self, root):

    def inorderTraversal_3(self, root):

    def postorderTraversal_3(self, root):