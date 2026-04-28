#28 april 2026
#(*) [Pattern Printing1]
n= 4
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ", end=" ")
    for j in range(1,i+1):
        print("*", end=" ")
    print()
    
#output
#       * 
#     * *
#   * * *
# * * * *   