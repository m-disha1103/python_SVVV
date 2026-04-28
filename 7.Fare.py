#28 april 2026
#cab fare system
distance=float(input("Enter the distance traveled in kilometers: "))
night=input("night(yes/no): ")
fare=0
if distance <= 5:
    fare = 50
elif distance <=10:
    fare = 50 + (distance - 5) * 40
else:
    fare = 50 + 5 * 40 + (distance - 10) * 30 

if night:
    fare+= 0.20*fare
print("Final Fare = ",int(fare))    