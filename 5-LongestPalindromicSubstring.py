
class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        max_length = 0
        max_range = []
        index = length//2
        for i in range(length):
            if i%2 == 0:
                index += i
            else:
                index += -i
            if index < 0 or index >= length:
                break
            print(index)
            left, right = index, index
            while(left>0 and right<length-1):
                if s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                else:
                    break
            if right-left+1 > max_length:
                max_length = right-left+1
                max_range = (left, right)

            if index+1 < length and s[index] == s[index+1]:
                left, right = index, index+1
                while(left>0 and right<length-1):
                    if s[left-1] == s[right+1]:
                        left -= 1
                        right += 1
                    else:
                        break
                if right-left+1 > max_length:
                    max_length = right-left+1
                    max_range = (left, right)

            if max_length > 2*(index+1) or max_length > (length-index)*2-1:
                break
        print(s[max_range[0] : max_range[1]+1])

if __name__ == '__main__':
    sol = Solution()
    sol.longestPalindrome('dddddddd')
    
