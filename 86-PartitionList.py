
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        small = ListNode(0)
        smallHead = small
        large = ListNode(0)
        largeHead = large
        index = head
        while(index):
            if index.val < x:
                small.next = index
                small = small.next
            else:
                large.next = index
                large = large.next
            index = index.next
        large.next = None
        small.next = largeHead.next
        return smallHead.next

if __name__ == '__main__':
    s = Solution()
    head = ListNode(2)
    head.next = ListNode(1)
    #head.next.next = ListNode(3)
    res = s.partition(head, 2)
    while(res):
        print(res.val)
        res = res.next
