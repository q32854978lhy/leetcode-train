#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def  hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """ if not root:
            return False
        if not root.left and not root.right  and root.val==sum:
            return True
        sum-=root.val
        return self.hasPathSum(root.left,sum)"""
        if not root:
            return False
        else:
            stack=[((sum-root.val),root),]
        while stack:
            sum_num,cur_node=stack.pop()
            next_node=[cur_node.left,cur_node.right]
            if not  cur_node.left and not cur_node.right  and  sum_num==0:
                return True
            for c in next_node:
                if c :
                     stack.append((sum_num-c.val,c))
        return False


        
# @lc code=end

