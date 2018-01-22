class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        # 求l1和l2的长度
        l1_len = self.get_length(l1)
        l2_len = self.get_length(l2)
        print(l1_len, l2_len)

        # 对于超出长度的部分
        res_pre = ListNode(0)
        add_pre = ListNode(0)
        l1_cur, l2_cur = l1, l2
        while(l1_len != l2_len):
            if l1_len > l2_len:
                cur_val = l1_cur.val
                l1_len -= 1
                l1_cur = l1_cur.next
            else:
                cur_val = l2_cur.val
                l2_len -= 1
                l2_cur = l2_cur.next
            res_cur = ListNode(cur_val)
            print('p', cur_val)
            res_cur.next = res_pre
            res_pre = res_cur
            add_cur = ListNode(0)
            add_cur.next = add_pre
            add_pre = add_cur

        # 对于长度一致的部分，求和
        res_cur = ListNode((l1_cur.val + l2_cur.val) % 10)
        res_cur.next = res_pre
        res_pre = res_cur
        add_cur = ListNode((l1_cur.val + l2_cur.val) // 10)
        add_cur.next = add_pre
        add_pre = add_cur
        while(l1_cur.next):
            l1_cur = l1_cur.next
            l2_cur = l2_cur.next
            res_cur = ListNode((l1_cur.val + l2_cur.val) % 10)
            add_cur = ListNode((l1_cur.val + l2_cur.val) // 10)
            res_cur.next = res_pre
            res_pre = res_cur
            add_cur.next = add_pre
            add_pre = add_cur

        # 根据倒着的res，去加倒着的add
        addi = 0
        res_cur = res_cur.next
        while(add_cur and res_cur):
            print(res_cur.val, add_cur.val)
            tmp = (res_cur.val + add_cur.val + addi) // 10
            res_cur.val = (res_cur.val + add_cur.val + addi) % 10
            addi = tmp
            add_cur = add_cur.next
            res_cur = res_cur.next
        while(res_pre):
            print(res_pre.val)
            res_pre = res_pre.next
        '''
        # 把倒着的res反过来
        res_aft = ListNode(res_pre.val)
        while(res_pre.next):
            res_cur = ListNode(res_pre.next.val)
            res_cur.next = res_aft
            res_aft = res_cur
            res_pre = res_pre.next
        while(res_aft):
            print(res_aft.val)
            res_aft = res_aft.next
        if res_aft.val == 0:
            return res_aft.next
        else:
            return res_aft
        '''

    def get_length(self, l):
        l_len = 0
        while(l):
            l_len += 1
            l = l.next
        return l_len

class Solution2():
    def addTwoNumbers(self, l1, l2):
        # 先把l1和l2都存到栈里
        stack1, stack2 = [], []
        while(l1):
            stack1.append(l1.val)
            l1 = l1.next
        while(l2):
            stack2.append(l2.val)
            l2 = l2.next
        print(stack1, stack2)

        # 再边出栈边计算，相当于从个位数开始算；将结果生成反向链表
        sum_pre = None
        addi = 0
        while(stack1 and stack2):
            sum_cur = ListNode((stack1[-1] + stack2[-1] + addi) % 10)
            addi = (stack1.pop() + stack2.pop() + addi) // 10
            sum_cur.next = sum_pre
            sum_pre = sum_cur
        stack = stack1 if stack1 else stack2
        while(stack):
            sum_cur = ListNode((stack[-1] + addi) % 10)
            addi = (stack.pop() + addi) // 10
            sum_cur.next = sum_pre
            sum_pre = sum_cur
        if addi > 0:
            sum_cur = ListNode(addi)
            sum_cur.next = sum_pre
            sum_pre = sum_cur
        while(sum_pre):
            print(sum_pre.val)
            sum_pre = sum_pre.next

if __name__ == '__main__':
    s = Solution2()
    l1 = ListNode(9)
#    l1.next = ListNode(2)
#    l1.next.next = ListNode(4)
#    l1.next.next.next = ListNode(3)
#    l1.next.next.next.next = ListNode(6)
    l2 = ListNode(1)
#    l2.next = ListNode(9)
#    l2.next.next = ListNode(9)

    s.addTwoNumbers(l1, l2)
