# 2017-11-21
# 数组，计算 ****

class Solution:
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        res = []
        for i, n1 in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while(l < r):
                if nums[l] + nums[r] + n1 == 0:
                    res.append([n1, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while(l < r and nums[l] == nums[l-1]):
                        l += 1
                    while(l < r and nums[r] == nums[r+1]):
                        r -= 1
                elif nums[l] + nums[r] + n1 < 0:
                    l += 1
                else:
                    r -= 1
        print(res)
        return res 


    def threeSum_time_limit(self, nums):
        nums.sort()
        hash_map = {}
        for i, n in enumerate(nums):
            if n not in hash_map:
                hash_map[n] = [i]
            else:
                hash_map[n].append(i)
        res = []
        for i, n1 in enumerate(nums):
            if i > 0 and n1 == nums[i-1]:
                continue
            for t, n2 in enumerate(nums[i+1:]):
                j = i+t+1
                if j > i+1 and n2 == nums[j-1]:
                    continue
                n3 = -(n1+n2)
                if n3 < n1 or n3 < n2:
                    continue
                if n3 not in hash_map:
                    continue
                if hash_map[n3] == [i] or hash_map[n3] == [j] or hash_map[n3] == [i, j]:
                    continue
                res.append([n1,n2,n3])
        print(res)


if __name__== '__main__':
    s = Solution()
    num = [-4,3,-2,4,7,1]
    num = [2,-1,1,2,0,0]
    num = [-2,0,0,2,2]
    num = [0,0,0]
    num = [-1,0,1,2,-1,-4]
    s.threeSum(num)
