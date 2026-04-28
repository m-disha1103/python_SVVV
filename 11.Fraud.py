#28 april 2026
#Fraud Transaction Detection 
amount = int(input("Enter amount: "))
location = input("Location match (Yes/No): ")
transactions = int(input("Enter number of transactions in 1 min: "))

# Convert location to boolean
location_match = True if location.lower() == "yes" else False

if (amount > 50000 and not location_match) or (transactions > 3):
    print("Fraud Detected")
else:
    print("Transaction Safe")

