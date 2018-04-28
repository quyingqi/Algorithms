__author__ = 'cookie'
# -*- coding: utf-8 -*-
#  2018/4/28 17:07
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt_list = [0]*(nums[-1]+1)
        for n in nums:
            cnt_list[n] += 1
        tail = [0] * (nums[-1]+2)
        for i,n in enumerate(cnt_list):
            if n == 0:
                continue
            if tail[i] > 0:
                if n > tail[i]:
                    n -= tail[i]
                    tail[i+1] += tail[i]
                else:
                    tail[i+1] += n
                    continue
            if i+2 < len(cnt_list) and cnt_list[i+1] >= n and cnt_list[i+2] >= n:
                cnt_list[i+1] -= n
                cnt_list[i+2] -= n
                tail[i+3] += n
            else:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    res = s.isPossible([1,2,3,3,4,4,5,7,7,8,8,9,9,10,11,11,11,12,12,13,13])
    print(res)