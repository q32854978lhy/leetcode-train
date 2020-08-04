#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack=['?']                #构造栈
        dic={"(":")","{":"}","[":"]","?":"?"}
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                temp=stack.pop()
                if dic[temp]!=i:
                    return False
        return len(stack)==1
        
# @lc code=end

