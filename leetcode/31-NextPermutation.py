# 2017-11-22
# 数，排序 **

class Solution:
    def nextPermutation(self, nums):
        modify = False
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] >= nums[i]:continue
            tmp = nums[i-1]
            print(tmp)
            for j in range(len(nums)-1, i-1, -1):
                if nums[j] <= tmp:continue
                nums[i-1] = nums[j]
                nums[j] = tmp
                self.exchange(nums, i, len(nums)-1)
                break
            modify = True
            break
        if not modify:
            self.exchange(nums, 0, len(nums)-1)

    def exchange(self, nums, j, k):
        while(j < k):
            tmp = nums[j]
            nums[j] = nums[k]
            nums[k] = tmp
            j += 1
            k -= 1

if __name__== '__main__':
    s = Solution()
    nums = [2,2,0,4,3,1]
    s.nextPermutation(nums)
    print(nums)
