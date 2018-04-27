__author__ = 'cookie'
# -*- coding: utf-8 -*-
#  2018/4/27 11:32

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = self.quick_sort(nums, 0, len(nums)-1, k)
        return res

    # 快排实现
    def quick_sort(self, nums, l, r, k):
        if l >= r:
            if l == r and l+1 == k: # 对于单个数字，要判断一下是不是第k个
                return nums[l]
            return
        i, j = l, r-1
        while(i <= j):
            while(i <= j and nums[i] > nums[r]): # 左指针右移
                i += 1
            while(i <= j and nums[j] <= nums[r]): # 右指针左移
                j -= 1
            if i >= j:  # 两个指针相交后，跟flag交换
                nums[i], nums[r] = nums[r], nums[i]
                if i+1 == k:  # 交换后看是不是第k个，是的话直接返回
                    return nums[i]
            else:     # 两个指针还没相交，内容互换
                nums[i], nums[j] = nums[j], nums[i]
        if k < i+1:
            return self.quick_sort(nums, l, i-1, k)
        elif k > i+1:
            return self.quick_sort(nums, i+1, r, k)

    # 堆排实现
    def hip_sort(self,nums):
        pass

if __name__ == '__main__':
    s = Solution()
    res = s.findKthLargest([5,3,6,2,7,5,3], 4)
    print(res)