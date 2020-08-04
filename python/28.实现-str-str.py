#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        """else:
            n=len(needle)
            for j in range(len(haystack)):
                if  haystack[j:j+n]==needle:
                        return j
            return -1"""
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                 if haystack[i+j] != needle[j]:
                     break
                 if j == len(needle)-1:
                     return i 
        return -1

        
# @lc code=end

