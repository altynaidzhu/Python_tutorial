item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))


total = price * quantity

print (f"You have bought {quantity} x {item}/s")
print (f"You total is: ${round(total),2}/s")







length = float(input("Enter the length of a rectangle:" ))
width = float(input("Enter the width of a rectangle:" ))
height = float(input("Enter the heifht of a rectangle:" ))

volume =  length * width * height

print(f"The volume is : {volume} cm^2")