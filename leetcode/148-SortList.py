__author__ = 'cookie'
# -*- coding: utf-8 -*-
#  2018/4/24 21:58

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head, tail = self.iter(head, None)
        return head

    #用快排实现链表的排序
    def iter(self, head, tail):
        flag = head     #第一个数作为比较对象
        i = head.next
        left, right = ListNode(0), ListNode(0) #记录比flag小的数、大的数的头节点
        li, ri, fi = left, right, flag
        while(i and i != tail):
            if i.val > flag.val:  #如果当前节点>flag，把它加到right后面
                ri.next = i
                ri = ri.next
            elif i.val < flag.val:   #如果当前节点<=flag，把它加到left后面
                li.next = i
                li = li.next
            else:                   #如果当前节点==flag，把它加到flag后面
                fi.next = i
                fi = fi.next
            i = i.next

        if left.next: # 如果有比flag小的数，则对左边的部分递归，得到排序后的头和尾
            l_head, l_tail = self.iter(left.next, li.next)
            l_tail.next = flag
        else:       # 否则，头节点就是flag
            l_head = flag
        if right.next: # 如果有比flag大的数，则对右边的部分递归，得到排序后的头和尾
            r_head, r_tail = self.iter(right.next, ri.next)
            fi.next = r_head
        else:       # 否则，尾节点就是flag
            fi.next = None
            r_tail = fi
        return l_head, r_tail

if __name__ == '__main__':
    s = Solution()
    list = [6,5,7,2,4,3]
    li = ListNode(1)
    tmp = li
    for i in list:
        tmp.next = ListNode(i)
        tmp = tmp.next
    res = s.sortList(li)
    r = []
    while(res):
        r.append(res.val)
        res = res.next
    print(r)