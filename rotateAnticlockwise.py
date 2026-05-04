# 04 may 2026
# write a program to rotate the elements in a list by k times in anticlockwise direction [10,20,30,40,50] k=2 output [40,50,10,20,30]
lst=eval(input("enter list: "))
k= int(input("enter k: "))
# 1,2,3,4,5

for i in range(k):
    item= lst.pop()
    lst.insert(0,item)

print(lst)    

# write a program to rotate element by k times in anticlockwise direction keeping  m element constant at the left side 