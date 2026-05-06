#06 may 2026
#Cinema Booking System
#Scenario:
# in an online cinema booking system, there are N seats in a row, represented as an arrayo of 0s, and 1s (0=empty, 1=occupied).
#you need to find the longest stretch of consecutive empty seats (0s), so that a large family can sit together.
#Example: seats=[1,0,0,0,1,0,0] output: 3
lst=eval(input())
max,count=0,0
for ele in lst:
    if ele==0:
        count+=1
    else:
        if max<count:
            max=count
        count=0
if max<count:
    max=count
print(max)
#output
# [1,0,0,1,0,1,0,0]
# 2
