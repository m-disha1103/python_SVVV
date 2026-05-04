# 04 may 2026
#write a program to find second-largest and third-smallest number in a list of elementswithout using built-in functions

lst = eval(input("Enter a list: "))

# Initialize values
largest = second_largest = float('-inf')
smallest = second_smallest = third_smallest = float('inf')

for num in lst:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    if num < smallest:
        third_smallest = second_smallest
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        third_smallest = second_smallest
        second_smallest = num
    elif num < third_smallest and num != second_smallest and num != smallest:
        third_smallest = num

print("Second Largest:", second_largest)
print("Third Smallest:", third_smallest)