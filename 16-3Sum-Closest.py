# 2017-11-22
# 数组，计算 ****
import sys
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        print(nums)
        min_gap = sys.maxsize
        for i, n1 in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while(l < r):
                s = n1+nums[l]+nums[r]
                if abs(s-target) < min_gap:
                    min_gap = abs(s-target)
                    res = s
                if s == target:
                    return res
                elif s < target:
                    l += 1
                else:
                    r -= 1
        print(min_gap)
        print(res)

if __name__== '__main__':
    s = Solution()
    num = [-1,0,1,2,-1,-4]
    num = [-4,3,-2,4,7,1]
    num = [2,-1,1,2,0,0]
    num = [-1,2,1,-4]
    num = [0, 2,1,-3]
    s.threeSumClosest(num, 1)
