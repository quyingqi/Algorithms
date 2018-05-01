__author__ = 'cookie'
# -*- coding: utf-8 -*-
#  2018/5/1 11:45

class Solution:
    def findAnagrams(self, s, p): # 438-找出所有anagram的位置
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dic = [0]*26
        for i in p:
            dic[ord(i)-ord('a')] += 1 # 记录p中出现的字符
        cnt = len(p)
        for i in s[:len(p)]:    # 若在s中也出现过，消掉
            if dic[ord(i)-ord('a')] > 0:
                cnt -= 1  # cnt记录p中的字符消掉了多少
            dic[ord(i)-ord('a')] -= 1
        res = []
        if cnt == 0:
            res.append(0)
        for i in range(len(p), len(s)): # 以p的长度为滑动窗口，每次向右滑一步，只需要对最左边的start和最右边新加入的i进行处理
            start = i-len(p)
            if dic[ord(s[start])-ord('a')] >= 0:
                cnt += 1
            dic[ord(s[start])-ord('a')] += 1
            if dic[ord(s[i])-ord('a')] > 0:
                cnt -= 1
            dic[ord(s[i])-ord('a')] -= 1
            if cnt == 0:
                res.append(start+1)
        return res

    def checkInclusion(self, s1, s2): # 567-判断是否含有anagram
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dic = [0]*26
        for i in s1:
            dic[ord(i)-ord('a')] += 1
        cnt = len(s1)
        for i in s2[:len(s1)]:
            if dic[ord(i)-ord('a')] > 0:
                cnt -= 1
            dic[ord(i)-ord('a')] -= 1
        if cnt == 0:
            return True
        for i in range(len(s1), len(s2)):
            start = i-len(s1)
            if dic[ord(s2[start])-ord('a')] >= 0:
                cnt += 1
            dic[ord(s2[start])-ord('a')] += 1
            if dic[ord(s2[i])-ord('a')] > 0:
                cnt -= 1
            dic[ord(s2[i])-ord('a')] -= 1
            if cnt == 0:
                return True
        return False

if __name__ == '__main__':
    s = 'abdbcabdc'
    p = 'abcd'
    res = Solution().findAnagrams(s, p)
    print(res)
    res = Solution().checkInclusion(p, s)
    print(res)