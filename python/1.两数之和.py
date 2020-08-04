#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=dict()  #初始化字典
        for value ,key  in enumerate(nums):
            dic[key]=value
        for index_i,num in enumerate(nums):
            index_j=dic.get(target-num) #获取target-num的index
            if index_j is not None and index_j!=index_i:
                return [index_i,index_j]     
        
# @lc code=end

