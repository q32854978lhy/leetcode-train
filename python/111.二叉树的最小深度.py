#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1'''
        if root ==None :
            return 0
        else:
            stack,min_depth=[(1,root)],float('inf')
        while stack:
            depth,cur_node=stack.pop()
            next_node=[cur_node.left,cur_node.right]
            if not any(next_node):
                min_depth=min(min_depth,depth)
            else:
                for  c_node in next_node:
                    if c_node:
                        stack.append((depth+1,c_node))
        return min_depth
            

# @lc code=end

