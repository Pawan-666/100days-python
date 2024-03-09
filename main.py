print("Welcome to the Treasure Island, Your mission is to find the treasure")
in_out = input("type left or right to go to that direction: ")
if in_out.lower() == "left":
   in_out = input("swim or wait: ") 
   if in_out.lower() == "wait":
       in_out = input("Choose door color, either red,blue or yellow: ")
       if (in_out.lower() == "red") or (in_out.lower() == "blue"):
           print("Game Over")
       elif in_out.lower() == "yellow":
           print("you win!")
       else:
           print("Enter the specified color only")
   elif in_out.lower() == "swim":
       print("Game Over")
   else:
       print("Wrong Entry")
elif in_out.lower() == "right":
    print("Game Over")
else:
    print("Wrong entry")
