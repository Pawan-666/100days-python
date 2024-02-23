#Days, weeks, months remaining

your_age = round(float(input("Enter your current age: ")),2)
remaining_yrs = 70.00 - your_age
remaining_days = remaining_yrs * 365
remaining_weeks = remaining_yrs * 52
remaining_months = remaining_yrs * 12
message = f"You have remaining {int(remaining_days)} days {int(remaining_weeks)} weeks {int(remaining_months)} months"
print(message)
