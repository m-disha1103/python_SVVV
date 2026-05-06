#06 may 2026
#hybrid inheritence
#Hybrid inheritance is a combination of more than one type of inheritance. 
# It uses a mix like single, multiple, or multilevel inheritance within the same program. 
# Python's method resolution order (MRO) handles such cases.

class Solution:
    def add(self, a, b):
        return a + b 
    def add(self, a, b, c):
        return a + b + c    

s=Solution()
#print(s.add(2, 5))    
print(s.add(2, 5, 3)) # This will call the second add 