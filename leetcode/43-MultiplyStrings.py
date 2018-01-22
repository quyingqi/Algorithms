
class Solution(object):
    def multiply(self, num1, num2):
        res = 0
        for idx1, n2 in enumerate(num2[::-1]):
            tmp = 0
            n2 = int(n2)
            for idx2, n1 in enumerate(num1[::-1]):
                n1 = int(n1)
                tmp += (n1*n2)*(10**idx2)
            res += tmp*(10**idx1)
        return str(res)

