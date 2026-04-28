#28 april 2026
#homeWork
#E-commerce Return policy
days = int(input("Enter number of days: "))
defective = input("Is product defective (Yes/No): ").lower()
premium = input("Is user premium (Yes/No): ").lower()

is_defective = True if defective == "yes" else False
is_premium = True if premium == "yes" else False

if (days <= 7) or is_defective or (is_premium and days <= 15):
    print("Return Accepted")
else:
    print("Return Rejected")