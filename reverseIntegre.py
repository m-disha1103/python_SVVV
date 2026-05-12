# 11 may 2026
#leet code
# reverse integer
class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        
        reversed_num = str(abs(x))[::-1]
        
        result = sign * int(reversed_num)
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result
        
