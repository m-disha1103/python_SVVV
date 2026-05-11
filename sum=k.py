# 06 may 2026
#find the longest subarray with sum=k
lst=eval(input())
k=int(input())
# left = 0
# current_sum = 0
# max_len = 0

# for right in range(len(lst)):
#     current_sum = current_sum + lst[right]

#     # shrink window if sum > k
#     while current_sum > k:
#         current_sum = current_sum - lst[left]
#         left = left + 1

#     # check if sum == k
#     if current_sum == k:
#         length = right - left + 1
#         if length > max_len:
#             max_len = length

# print("Longest subarray length:", max_len)

# 11 may 2026
# 2nd method
dict={}
sum=0
max_len=0
for i in range(len(lst)):
    sum+=lst[i]
    if dict.get(sum-k)!=None:
        max_len=max(max_len,i-dict[sum-k])
        if max_len<1:
            max_len=1
    dict[sum]=i
print("Longest subarray length:", max_len)
# | i | lst[i] | sum | sum-k | Present in d? | max_len    | Dictionary                           |
# | - | ------ | --- | ----- | ------------- | ---------- | ------------------------------------ |
# | 0 | 10     | 10  | -5    | No            | 0          | {10:0}                               |
# | 1 | 5      | 15  | 0     | No            | 2 (sum==k) | {10:0, 15:1}                         |
# | 2 | 2      | 17  | 2     | No            | 2          | {10:0, 15:1, 17:2}                   |
# | 3 | 7      | 24  | 9     | No            | 2          | {10:0, 15:1, 17:2, 24:3}             |
# | 4 | 1      | 25  | 10    | Yes → index 0 | 4          | {10:0, 15:1, 17:2, 24:3,
