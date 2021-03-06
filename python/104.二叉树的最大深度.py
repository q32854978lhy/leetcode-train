#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else: 
            leftheight=self.maxDepth(root.left)
            rightheight=self.maxDepth(root.right)
            return max(leftheight,rightheight)+1
        
# @lc code=end

