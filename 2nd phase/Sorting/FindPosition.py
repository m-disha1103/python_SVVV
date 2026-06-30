# 29 june 2026
# wap to find the position of a element in a group of element [ 5 7 2 6 9 3 1] key=4
def FP(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i + 1   
    return -1              

arr = [5, 7, 2, 6, 9, 3, 1]
key = 5

position =FP(arr, key)

if position == -1:
    print("Element not found")
else:
    print("Element found at position:", position)