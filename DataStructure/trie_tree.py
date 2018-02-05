__author__ = 'cookie'
# -*- coding:utf-8 -*-
'''
1、根节点不包含字符，除根节点外每一个节点都只包含一个字符
2、从根节点到某一个节点，路径上经过的字符连接起来，就是该节点对应的字符串
3、每个节点的所有子节点包含的字符都不相同。
'''
class TreeNode:
    def __init__(self, c):
        self.val = c
        self.occurances = 0 # 有多少单词通过这个节点,即由根至该节点组成的字符串前缀出现的次数
        self.children = {}
        self.isEnd = False # 是不是字符串的最后一个节点

class TrieTree:
    def __init__(self):
        self.head = TreeNode('')

    # 判断字典树中是否有该字符串
    def contains(self, word):
        nodes = self.head
        for w in word:
            if w not in nodes.children:
                return False
            else:
                nodes = nodes.children[w]
        if nodes.isEnd:
            return True
        else:
            return False

    # 返回某前缀在字典树中出现的次数
    def frequency(self, word):
        nodes = self.head
        for w in word:
            if w not in nodes.children:
                return False
            else:
                nodes = nodes.children[w]
        return nodes.occurances

    # 插入一个字符串（没有考虑字符串本来就存在的情况）
    def insert(self, word):
        if not word:
            return
        nodes = self.head
        nodes.occurances += 1
        for w in word:
            if w not in nodes.children:
                nodes.children[w] = TreeNode(w)
            nodes = nodes.children[w]
            nodes.occurances += 1
        nodes.isEnd = True

    # 删除一个字符串（没有处理occurances）
    def remove(self, word):
        nodes = self.head
        last_node = None
        single, singel_w = None, None
        for w in word:
            if w not in nodes.children:
                return False
            if len(nodes.children) > 1:
                single = None
            elif not single:
                single = last_node
                single_w = nodes.val
            last_node = nodes
            nodes = nodes.children[w]
        if single:
            single.children.pop(single_w)
        else:
            last_node.children.pop(word[-1])
        self.head.occurances -= 1
        return True

    # 整个字典树中不同字符串的个数
    def size(self):
        return self.head.occurances

if __name__ == '__main__':
    t = TrieTree()
    t.insert('abord')
    t.insert('abandent')
    t.insert('black')
    print(t.contains('aban'))
    print(t.size())
    print(t.remove('abord'))
    print(t.size())
    t.insert('blace')
    print(t.remove('black'))
    print(t.contains('blace'))
    print(t.remove('abor'))