#28 april 2026
#Dynamic pricing Engine
base=int(input("Enter the base price: "))
demand=int(input("Demand (yes/no): "))
weekend=int(input("Is it weekend (yes/no): "))
if demand=="yes" and weekend=="yes":
    base=base*1.3
elif demand=="yes" and weekend=="no":
    base=base*1.2
elif demand=="no" and weekend=="yes":
    base=base*1.1

print("final price: ", base)        