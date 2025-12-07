age = int(input("enter the age :"))

day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    discout = price - 2
print(f"tiket price for you is ${discout}")

