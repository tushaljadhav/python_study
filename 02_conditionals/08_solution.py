password = input("Create Password :")

if len(password) <= 6:
    str = "Weak"
elif len(password) <= 10:
    str = "Medium"
else:
    str = "Strong"
print("Password strength is:",str)