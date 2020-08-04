#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        else:
            res=0
            for i in range(n-1,-1,-1):
                 if  s[i]!=" ":
                     res+=1
                 elif s[i]==" " and res==0:
                     res=0
                 else:
                     return res
            return res 
# @lc code=end

