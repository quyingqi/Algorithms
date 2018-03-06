__author__ = 'cookie'
# -*- coding: utf-8 -*-
#  2018/3/6 22:22
# 求二叉树中两个节点的最近公共父节点

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: # 如果在root的左子树和右子树分别找到了p和q，那么root就是最小的公共父节点
            return root
        if l: # 一种情况是只在左子树中找到了p或q，往上传；2、p和q都在左子树中，此时l记录着它们的最小公共父节点，直接往上传即可
            return l
        if r:
            return r

class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        stack = [root]
        parent = {root:None} #记录每个节点的父节点
        while(stack):
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
            if p in parent and q in parent:
                break
        path1 = [p]
        # 分别求两个节点到根节点的路径
        while(parent[p]):
            path1.append(parent[p])
            p = parent[p]
        path2 = [q]
        while(parent[q]):
            path2.append(parent[q])
            q = parent[q]
        # 计算两条路径上从下往上第一个相同的节点，即为公共父节点
        length = min(len(path1), len(path2))
        for i in range(length, 0, -1):
            if path1[-i] == path2[-i]:
                return path1[-i]

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    p = root.left
    q = root.right
    res = Solution1().lowestCommonAncestor(root, p, q)
    print(res.val)