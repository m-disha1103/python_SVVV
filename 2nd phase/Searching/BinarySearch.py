# 29 june 2026

lst = [10,20,30,40,50,60]
key = int(input())
l = 0
r = len(lst)-1
while l<r:
    mid = l+(r-l)//2
    if lst[mid]==key:
        print(mid+1)
    elif lst[mid]<key:
        l = mid+1
    else:
        r = mid-1