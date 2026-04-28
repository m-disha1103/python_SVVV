# 28 april 2026
# parking lot management system
no_of_hours = float(input("Enter the number of hours parked: "))
bill=0

if no_of_hours <= 2:
    bill =no_of_hours * 100
elif no_of_hours <= 5:
    bill = 2*100 + (no_of_hours - 2) * 50
else:
    bill = 2*100 + 3 * 50 + (no_of_hours - 5) * 25
print("The bill is: ", bill)  #if-elif-else statement is used to calculate the parking bill based on the number of hours parked. The first 2 hours are charged at a rate of 100 per hour, the next 3 hours are charged at a rate of 50 per hour, and any additional hours beyond 5 are charged at a rate of 25 per hour. The total bill is then printed to the user.        
