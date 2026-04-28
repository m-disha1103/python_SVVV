#another way 
#28 april 2026
#password strength Checker
from symtable import Symbol


password=input("enter a password: ")
hasUpper=False
hasDigit=False
hasSymbol=False
hasLen=len(password)>=8
for i in password():
    if i.isupper():
        hasUpper=True
    elif i.isdigit():
        hasDigit=True
    elif i.islower():
        hasLower=True
    else:
        hasSymbol=True
if hasUpper and hasDigit and hasSymbol and hasLen:
    print("strong password")
else:
    print("weak password")                