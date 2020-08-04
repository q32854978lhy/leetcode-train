#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
             for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal"""
        dp=[]
        for  i  in range(numRows):
            row=[0 for num in range(i+1) ]
            row[0],row[-1]=1,1
            for j in range(1,i):
                row[j]=dp[i-1][j-1]+dp[i-1][j]
            dp.append(row)
        return dp
        

        
# @lc code=end

