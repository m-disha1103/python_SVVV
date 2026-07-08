# 30 june 2026
# arr=(3,6,7,11)
# h=8 
# min= 1|4
# max= 11|5|4
# s=6 1+1+2+2 = 6
# s=3 1+2+3+4 = 10 X
# s=5 1+2+2+3 = 8
# s=4 1+2+2+3 = 8
def isFeasible(lst,h,s):
    sum=0
    for p in lst:
        sum +=(p+s-1)//s
    return sum<=h
# lst=[3,6,7,11]
lst=[1,5,8,9,11]
h=8

min=1
max=11
while min<=max:
    s=min+(max-min)//2
    if (isFeasible(lst,h,s)):
        max=s - 1
    else:
        min=s + 1

print(s)