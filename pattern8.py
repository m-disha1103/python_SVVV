#28 april 2026
# Homework
#pattern 8
#* * * * *
#  * * * * *
#    * * * * *
#      * * * * *
n = 4
for i in range(n):
    
    for k in range(i):
            print("  ", end=" ")
    for j in range(5):
            print("*", end="")
    
    print()