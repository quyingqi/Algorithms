__author__ = 'cookie'
# -*- coding: utf-8 -*-
#  2018/4/28 23:05

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start, end = None, None
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                start = i-1
                break
        if start == None:
            return 0
        for j in range(len(nums)-1, 0, -1):
            if nums[j] < nums[j-1]:
                end = j
                break
        minn = min(nums[start:end+1])
        maxx = max(nums[start:end+1])
        print(start, end, minn, maxx)
        for i in range(len(nums)):
            if nums[i] > minn:
                start = i
                break
        for j in range(len(nums)-1, -1, -1):
            if nums[j] < maxx:
                end = j
                break
        return end-start+1

if __name__ == '__main__':
    s = Solution()
    l1 = [2,5,6,4,8,11,9,10,15]
    l2 = [1,3,2,3,3]
    l3 = [1,3,2,2,2]
    l4 = [4,2,1,3,5]
    l5 = [2,1]
    l6 = [1,2,4,5,3]
    res = s.findUnsortedSubarray(l6)
    print(res)