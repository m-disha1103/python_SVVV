#28 april 2026
#Password Strength Checker
password = input("Enter password: ")
missing = []


if len(password) < 8:
    missing.append("length < 8")

if not any(ch.isdigit() for ch in password):
    missing.append("digit")

if not any(ch.isupper() for ch in password):
    missing.append("uppercase letter")

if not any(not ch.isalnum() for ch in password):
    missing.append("special character")

if len(missing) == 0:
    print("Strong Password")
else:
    print("Weak Password: Missing " + ", ".join(missing))

    