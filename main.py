print("Welcome to the tip calculator")
initial_total = float(input("What was the total bill? $"))
no_of_people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? "))
final_total = initial_total + tip_percentage/100*initial_total
each_person = final_total/no_of_people
final_amount = round(each_person,2)
final_amount = "{:.2f}".format(final_amount)      # force 2 no.s after floating point
print(f"Each person should pay: ${final_amount}")



