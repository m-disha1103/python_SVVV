#28 april 2026
# Odd - Even Game
number=int(input("Enter a number: "))
even=0
odd=0
while(number):
    if number%2==0:
        even=even+1
    else:
        odd+=1
    number= int(input("enter number: "))    

print("Even count: ", even)
print("Odd count: ", odd)  #if-else statement is used to determine whether the number is odd or even