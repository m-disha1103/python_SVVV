arr = list(map(int, input().split()))

n = len(arr)
stack = []
ans = [-1] * n

for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)