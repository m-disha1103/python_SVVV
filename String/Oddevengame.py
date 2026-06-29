num=int(input("enter no.: "))
even,odd=0,0
while(num):
    if num%2==0:
        even+=1
    else:
        odd+=1
    num=int(input("enter no.: "))

print("even count",even)
print("odd count",odd)            