#https://leetcode.com/problems/largest-number/

from functools import cmp_to_key

def comparator(x, y):
    str_x = str(x)
    str_y = str(y)
    if(str_x + str_y > str_y + str_x):
        return 1
    elif(str_x + str_y < str_y + str_x):
        return -1
    else: return 0
    
class Solution:
    def largestNumber(self, nums):
        return str(int(''.join(str(i) for i in sorted(nums, key=cmp_to_key(comparator), reverse=True))))