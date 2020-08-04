#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        value=0
        result=""
        for i in range(max(len(a),len(b))):
            value=carry          
            if i< len(a):
                value=value+int(a[-(1+i)])
            if i< len(b):
                value=value+int(b[-(1+i)])
            carry=value//2
            value=value%2
            result=result+str(value)
        if carry==1:
            result=result+str(1)
        return result[::-1]
# @lc code=end

