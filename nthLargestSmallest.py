# 04 may 2026
# wap to find nth largest and nth smallest number
lst = eval(input("Enter list: "))
n = int(input("Enter n: "))

# Find nth largest
temp = lst.copy()

for i in range(n):
    largest = temp[0]
    for num in temp:
        if num > largest:
            largest = num
    temp.remove(largest)   # remove largest each time

nth_largest = largest


# Find nth smallest
temp = lst.copy()

for i in range(n):
    smallest = temp[0]
    for num in temp:
        if num < smallest:
            smallest = num
    temp.remove(smallest)   # remove smallest each time

nth_smallest = smallest


print("Nth Largest:", nth_largest)
print("Nth Smallest:", nth_smallest)