row1 = ["😃", "😃", "😃"]
row2 = ["🥲", "🥲", "🥲"]
row3 = ["😂", "😂", "😂"]

map = [row1, row2, row3]
print(map)
print(f"{row1}\n{row2}\n{row3}")

position = input("where do you want to put the treasure? ")
row = int(position[0]) - 1
column = int(position[1]) - 1

# new_map = map[row]
# new_map[column] = "x"
map[row][column] = "X "
print(f"{row1}\n{row2}\n{row3}")
