# 06 may 2026
#find the longest subarray with sum=k
lst=eval(input())
k=int(input())
left = 0
current_sum = 0
max_len = 0

for right in range(len(lst)):
    current_sum = current_sum + lst[right]

    # shrink window if sum > k
    while current_sum > k:
        current_sum = current_sum - lst[left]
        left = left + 1

    # check if sum == k
    if current_sum == k:
        length = right - left + 1
        if length > max_len:
            max_len = length

print("Longest subarray length:", max_len)
