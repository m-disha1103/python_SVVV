# 04 may 2026
# write a program to rotate element by k times in anticlockwise direction keeping  m element constant at the left side 
lst = eval(input("Enter list: "))
k = int(input("Enter k: "))
m = int(input("Enter m: "))

n = len(lst)
fixed_part = lst[:m]
rotate_part = lst[m:]

length = len(rotate_part)
k = k % length
rotated = rotate_part[k:] + rotate_part[:k]
result = fixed_part + rotated

print("Rotated List:", result)