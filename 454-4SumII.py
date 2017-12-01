# 2017-11-22
# 数组，计算 **

class Solution:
    def fourSumCount(self, A, B, C, D):
        ab = {}
        res = 0
        for i,a in enumerate(A):
            for j,b in enumerate(B):
                if a+b in ab:
                    ab[a+b] += 1
                else:
                    ab[a+b] = 1
        for m,c in enumerate(C):
            for n,d in enumerate(D):
                if -c-d in ab:
                    res += ab[-c-d]
        print(res)
        

if __name__== '__main__':
    s = Solution()
    A = [-1,-1]
    B = [-1,1]
    C = [-1,1]
    D = [1,-1]
    s.fourSumCount(A,B,C,D)
