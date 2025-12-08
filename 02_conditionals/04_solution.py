fruit = "Banana"
color = input("Enter Banana Color:").lower()

if fruit == "Banana":
    if color == "green" :
        print("Banana is Unripe")
    elif color == "yellow" :
        print("Banana is Ripe")
    elif color == "brown" :
        print("Banana is Overripe")
    else:
        print("Enter a Valid Color")
