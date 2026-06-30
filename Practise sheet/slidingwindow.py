from collections import deque

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

dq = deque()

for i in range(len(arr)):
    # Remove indices outside the current window
    while dq and dq[0] <= i - k:
        dq.popleft()

    # Remove smaller elements from the back
    while dq and arr[dq[-1]] < arr[i]:
        dq.pop()

    dq.append(i)

    # Print maximum when the first window is complete
    if i >= k - 1:
        print(arr[dq[0]], end=" ")