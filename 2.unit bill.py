#28 april 2026
# unit bill calculation
units = int(input("Enter the number of units consumed: "))
bill = 50

if units <= 100:
    bill += units * 1.5
elif units <=200:
    bill += 100 * 1.5 + (units - 100) * 3.5    
else:
    bill += 100*1.5 +100*3.5+(units-200)*5    

if bill>2000:
    bill *= 1.1
print("The total bill is: ", bill)  #if-elif-else statement is used to calculate the electricity bill based on the number of units consumed. The first 100 units are charged at a rate of 1.5 per unit, the next 100 units are charged at a rate of 3.5 per unit, and any additional units beyond 200 are charged at a rate of 5 per unit. If the total bill exceeds 2000, an additional charge of 10% is added to the bill. Finally, the total bill is printed to the user.    