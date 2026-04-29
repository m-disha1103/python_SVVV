#29 april 2026
#write a program to print prime no from 1-n
n=int(input("enter last range: "))
sum=0
for i in range(2,n+1):
    for j in range(2,(i//2)+1):  #for-else loop used to check prime no
        if i%j==0:
            break
    else:
        print(i,end=" ")
        sum+=i #to sum prime numbers

print(" Sum of prime numbers:",sum)

# output:
# enter last range: 20
# 2 3 5 7 11 13 17 19 
# enter last range: 10
# 2 3 5 7        