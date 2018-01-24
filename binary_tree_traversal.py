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
    def postorderTraversal_2_1(self, root):
        res = []
        stack = []
        flag = [] # 记录栈里的节点是第几次走到（因为根节点要在第二次走到时才能访问）
        while(root or stack):
            if root: # 如果当前节点不为空，则入栈，往左走
                stack.append(root)
                flag.append(0)
                root = root.left
            else:  # 如果当前节点为空，则看栈顶节点
                f = flag.pop()
                if f == 0: # 如果栈顶节点是第一次走到，则往它的右孩子走
                    flag.append(1)
                    root = stack[-1].right
                else:  # 如果栈顶节点是第二次走到，则访问它，root置为空
                    node = stack.pop()
                    res.append(node.val)
                    root = None
        return res

    def postorderTraversal_2_2(self, root):
        res = []
        stack = []
        output = []  # 按照后序遍历的倒序 保存节点
        while(root or stack):
            if root: # 如果当前节点不为空，则入栈，往右走
                stack.append(root)
                output.append(root)
                root = root.right
            else:  # 如果当前节点为空，则往栈顶节点的左边走
                node = stack.pop()
                root = node.left
        while(output):
            res.append(output.pop().val)
        return res

    def postorderTraversal_2_3(self, root):
        res = []
        stack = []
        pre = None # 记录上一个访问的节点
        while(root or stack):
            # 如果是叶子节点 或者上一个访问的是其右孩子 或上一个访问的是其左孩子且右孩子为空，则访问该节点
            if not root.left and not root.right or (pre and (pre == root.right or (pre == root.left and not root.right))):
                res.append(root.val)
                pre = root
                if stack:
                    root = stack.pop() # 出栈
                else:
                    root = None
            else:
                stack.append(root)  # 入栈
                if pre == root.left: # 如果上一个访问的是其左孩子，则转到右边
                    root = root.right
                elif root.left:
                    root = root.left # 否则，一直往左走
                elif root.right:
                    root = root.right # 左边走到头，再往右走
        return res

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