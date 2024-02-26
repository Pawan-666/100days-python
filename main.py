height = int(input("Enter your height: "))
total_bill = 0

if height > 120:
    print("Yes, you can ride")
    age = int(input("Enter your age: "))
    if age < 12:
         total_bill = 5 

    elif age < 18:
         total_bill = 7 

    else: 
        total_bill = 12 

    want_photos = input("You want photos too, yes or no: ")
    if want_photos == "yes":
        total_bill += 3

    print(f"Your total bill is {total_bill}.")

else:
    print("Can't ride")
