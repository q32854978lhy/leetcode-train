#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums_copy=nums1[:m]
        nums1[:]=[]
        p1=0
        p2=0 #双指针加辅助数组空间
        while p1<m and p2<n:
            if nums_copy[p1]<nums2[p2]:
                nums1.append(nums_copy[p1])
                p1+=1
            else:
                nums1.append(nums2[p2])
                p2+=1
        if p1<m:
            nums1[p1+p2:]=nums_copy[p1:]
        else:
            nums1[p1+p2:]=nums2[p2:] 
        
# @lc code=end

