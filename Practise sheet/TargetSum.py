#capgemini
#Pair with Target sum
# scenaior: In a billing system, find two item prices that sum up to a given target amount.
lst=eval(input())
target=int(input()) 
left,right=0,len(lst)-1  #traversing from both ends
while left<right:
    current_sum=lst[left]+lst[right]
    if current_sum==target:
        print("Pair found:", lst[left], lst[right])
        break
    elif current_sum<target:
        left+=1  #move left pointer to the right to increase sum
    else:
        right-=1  #move right pointer to the left to decrease sum
else:
    print("No pair found that sums to the target.")

# [2,7,11,15]
# 9
# Pair found: 2 7