#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            i=0
            for j in range (1,len(nums)): #i,j双指针
                if nums[i]!=nums[j]:
                    i+=1
                    nums[i]=nums[j]
            return i+1

        
# @lc code=end

