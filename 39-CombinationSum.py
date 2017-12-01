
class Solution:

    def combinationSum(self, candidates, target):
        res = []
        l = []
        self.get_sum(candidates, 0, target, l, res)
        print(res)
        
    def get_sum(self, nums, index, target, l, ans):
        if target == 0:
            ans.append(l)
            return
        if index == len(nums) or target < 0:
            return
        self.get_sum(nums, index+1, target, l.copy(), ans) # index不放入
        l.append(nums[index])
        self.get_sum(nums, index, target-nums[index], l, ans) # index放入

    def combinationSum2(self, candidates, target):
        res = []
        l = []
        candidates.sort()
        self.get_sum2(candidates, 0, target, l, res)
        print(res)
        
    def get_sum2(self, nums, index, target, l, ans):
        if target == 0:
            if l not in ans:
                ans.append(l)
            return
        if index == len(nums) or target < 0:
            return
        self.get_sum2(nums, index+1, target, l.copy(), ans) # index不放入
        l.append(nums[index])
        self.get_sum2(nums, index+1, target-nums[index], l, ans) # index放入

    def combinationSum3(self, k, n):
        res = []
        self.get_sum3(1, k, n, [], res)
        print(res)

    def get_sum3(self, num, k, target, l, ans):
        if target == 0 and k == 0:
            ans.append(l)
            return
        if num > 9 or k < 0 or target < 0:
            return
        self.get_sum3(num+1, k, target, l.copy(), ans) #当前数不放入
        l.append(num)
        self.get_sum3(num+1, k-1, target-num, l, ans) #当前数放入

    def combinationSum4(self, nums, target):
        res = self.get_sum4(nums, 0, target, [])
        print(res)
        
    def get_sum4(self, nums, index, target, l):
        if target == 0:
            return 1
        if index == len(nums) or target < 0:
            return 0
        a = self.get_sum4(nums, index+1, target, l.copy()) # index不放入
        l.append(nums[index])
        b = self.get_sum4(nums, 0, target-nums[index], l) # index放入
        return a+b


    
if __name__ == '__main__':
    s = Solution()
    candi = [2,3,6,7]
    tar = 7
    s.combinationSum(candi, tar)
    candi = [10,1,2,7,6,1,5]
    tar = 8
    s.combinationSum2(candi, tar)
    s.combinationSum3(3,7)
    nums = [4,2,1]
    tar = 32
    s.combinationSum4(nums, tar)
