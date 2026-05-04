# 04 may 2026
# write a program to find second duplicate of given number in a list
lst = eval(input("Enter a list: "))
ele=int(input("enter no. "))
c= 3 #2 1 0
# 1 2 3 4 1 2 15 1
for i in range(len(lst)):
    if lst[i]==ele:
        c-=1
    if c==0:
        print("second duplicate is at index: ",i)
        break
else:
    print("not exist")    
