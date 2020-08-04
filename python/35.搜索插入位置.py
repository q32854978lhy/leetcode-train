#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l= 0
        r=len(nums)-1
        while l <= r: #二分法
            mid=int(l+r)//2
            if nums[mid]==target:
                 return mid
            if nums[mid] < target:
                 l = mid+1
            else:
                 r = mid-1
        return l   
# @lc code=end

