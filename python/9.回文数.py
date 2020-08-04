#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)
        #if str_x==str_x[::-1]:
        #    return True 
        #else:
        #    return False  简单方法
        start=0
        end=len(str_x)-1
        while start<end : #双指针
              if str_x[start]==str_x[end]:
                 start+=1
                 end-=1
              else :
                  return False
        return True
        
# @lc code=end

