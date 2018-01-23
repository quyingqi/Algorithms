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
            if(root):
                res.append(root.val) # 访问当前节点
                stack.append(root.right) # 右孩子入栈
                root = root.left  # 向左走
            else:
                root = stack.pop() # 出栈
        return res

    # inorder
    def inorderTraversal_2(self, root):
        res = []
        stack = []
        while(root or stack):
            while(root):  # 向左走到头，同时都入栈
                stack.append(root)
                root = root.left
            node = stack.pop() # 出栈
            res.append(node.val) # 访问该节点
            root = node.right # 向右走
        return res

    # postorder
    def postorderTraversal_2(self, root):
        pass

    ##------------------------------------------------------##
    # 3.Morris Traversal
    # preorder
    def preorderTraversal_3(self, root):
        res = []
        while(root):
            if root.left:
                # 找到当前节点的前驱节点
                tmp = root.left
                while(tmp.right and tmp.right != root):
                    tmp = tmp.right

                if tmp.right == root: # 如果已经连接过，则重置回去
                    tmp.right = None
                    root = root.right
                else:
                    tmp.right = root # 如果没有连接过，将前驱节点指向当前节点，并访问当前节点
                    res.append(root.val)
                    root = root.left # 往左走
            else:
                res.append(root.val) # 访问当前节点
                root = root.right
        return res

    # inorder
    def inorderTraversal_3(self, root):
        res = []
        while(root):
            if root.left:
                # 找到当前节点的前驱节点
                tmp = root.left
                while(tmp.right and tmp.right != root):
                    tmp = tmp.right

                if tmp.right == root: # 如果已经连接过，则重置回去，并访问当前节点
                    tmp.right = None
                    res.append(root.val)
                    root = root.right
                else:
                    tmp.right = root # 如果没有连接过，将前驱节点指向当前节点
                    root = root.left # 往左走
            else:
                res.append(root.val) # 访问当前节点
                root = root.right
        return res

    # postorder
    def postorderTraversal_3(self, root):
        pass