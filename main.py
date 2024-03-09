import random

names_string = input("Give everybody's name, seperated by a comma. ")
names = names_string.split(", ")
print(names)

random_name = random.choice(names)
# random_name = random.randint(0, len(names) - 1)
print(random_name)
# print(f"{names[random_name]} is going to pay the bill")
print(f"{random_name} is going to pay the bill")
