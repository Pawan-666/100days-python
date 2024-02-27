print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

full_name = name1.lower() + name2.lower()
print(full_name)

t = full_name.count("t")
r = full_name.count("r")
u = full_name.count("u")
e = full_name.count("e")

true = t + r + u + e

l = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")
e = full_name.count("e")

love = l + o + v + e

true_love= str(true) + str(love)
true_love_score = int(true_love)

if (true_love_score < 10) or (true_love_score) > 90:
    print(f"Your score is {true_love_score}, you go together like coke and mentos.")
# For Love Scores between 40 and 50, the message should be:
elif true_love_score > 40 or true_love_score < 50:
    print(f"Your score is {true_love_score}, you are alright together.")
# Otherwise, the message will just be their score. e.g.:
else:
    print(f"Your score is {true_love_score}.")
