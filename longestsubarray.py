# 06 may 2026
#find the longest subarray with sum<=k 
lst=eval(input())
k=int(input())
# current_sum=0
# max_length=0
# left=0
# for right in range(len(lst)):
#     current_sum+=lst[right]
#     while current_sum>k and left<=right:
#         current_sum-=lst[left]
#         left+=1
#     max_length=max(max_length,right-left+1)
# print(max_length)
# #output: 5 means (1,0,1,1,0) is the longest subarray with sum<=4f
# #input: 1,2,1,0,1,1,0
#       4
l=0
max=0
sum=0
for r in range(len(lst)):
    sum+=lst[r]
    if sum<=k and r-l+1>max:
        sum-=lst[l]
    while sum>k:
        sum-=lst[l]
        l+=1
print(max)        