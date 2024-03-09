import random

items = ["rock","paper","scissors"]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
your_choice= items[your_choice]
print(your_choice)
comp_choice = random.choice(items)
print(f"your_choice: {your_choice}")
if your_choice == 0:
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
elif your_choice == 1:
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
else:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

print(f"comp_choice: {comp_choice}")

if comp_choice == 0:
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
elif comp_choice == 1:
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
else:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
if your_choice == comp_choice:
    print("It's a tie.")
elif your_choice == "rock":
    if comp_choice == "scissors":
        print("Rock smashes scissors. You win!")
    else:
        print("Paper covers rock! You lose.")
elif your_choice == "paper":
    if comp_choice == "rock":
        print("Paper covers rock.You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif your_choice == "scissors" :
    if comp_choice == "paper":
        print("Scissors cut paper.You win!")
    else:
        print("Rock smashes scissors! You lose.")



# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.

