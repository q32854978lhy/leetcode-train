#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirro(root,root)
    def isMirro(self,root_a,root_b):
        if root_a==None and root_b==None:
            return True
        if root_a and root_b and root_a.val==root_b.val:
            return self.isMirro(root_a.left,root_b.right) and self.isMirro(root_a.right,root_b.left)
        return False
                    # @lc code=end

