distance = int(input("Enter The Distance :"))

if distance <= 3 :
    transpot = "Walk"
elif distance <= 15:
    transpot = "Bike"
else :
    transpot = "Car"

print("Ai recommend you the transport of :",transpot)