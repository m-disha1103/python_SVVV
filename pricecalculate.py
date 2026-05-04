# 04 may 2026
#you have a list of item prices calculate total bill after removing 3 items 
#100,200,0,50,0,300  input
lst = eval(input("Enter list of prices: "))
# Remove 3 items (0s in this case)  
ele=int(input("entern no."))

for i in range(len(lst)-1,0,-1):
    if lst[i]==ele:
        lst.pop(i)

print("List after removing items:", lst)