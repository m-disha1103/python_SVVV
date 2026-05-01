#homeWork
# Hollow Diamond Pattern
n = int(input("Enter size: "))

# Upper part (including middle row)
for i in range(1, n + 1):
    # leading spaces
    print(" " * (n - i), end="")
    
    if i == 1:
        print("*")
    else:
        # two boundary stars with inner gap
        print("*" + " " * (2 * i - 3) + "*")

# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

# output:
# Enter size: 5
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *        