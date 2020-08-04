#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """n=len(nums)
        curr_sum=max_sum=nums[0]
        for i in range(1,n):
             curr_sum=max(nums[i],curr_sum+nums[i])
             max_sum=max(curr_sum,max_sum)
        return max_sum 暴力法"""
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1] 
            max_sum = max(nums[i], max_sum)
        return max_sum       
# @lc code=end

