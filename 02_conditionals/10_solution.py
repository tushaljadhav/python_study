species = input("Enter the species:")
age = float(input("Enter the Age:"))

if species == "dog":
    if age < 2 :
        food = "Adult dog  Food"
    else:
        food = "Senior dog food"
elif species == "cat":
    if age > 5 :
        food = "Senior Cat Food"
    else :
        food = "Adult Cat Food"
else:
    food = "Invalid Species"
print(food)