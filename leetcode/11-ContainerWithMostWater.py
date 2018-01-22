# 2017-11-21
# trick ***

class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        max_area = 0
        while(i != j):
            area = (j-i) * min(height[i], height[j])
            if area > max_area:
                max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        print(max_area)

if __name__== '__main__':
    s = Solution()
    height = [4,3,2,4,7,1]
    height = [3,2,1,3]
    height = [2,1]
    s.maxArea(height)
