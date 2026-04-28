#28 april 2026
#ATM Withdrawal System
balance=float(input("Enter your current balance: "))
withdraw=float(input("Enter the amount to withdraw: "))
min_balance=1000
if withdraw>balance:
    print("Insufficient balance!")
elif balance-withdraw<min_balance:
    print("Transaction failed! Minimum balance voilation.")  
else:
    balance=balance-withdraw
    print("transaction successful!")
    print("Withdrawal successful! Your new balance is: ", balance)  
    