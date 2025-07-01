print("Welcome to place the rabbit\n")

field = [ ["🟢","🟢","🟢"], ["🟢","🟢","🟢"], ["🟢","🟢","🟢"] ]

print(f"{field[0]}\n{field[1]}\n{field[2]}\n")

print("\nwhere do you want to place the rabbit?\n")

position = input("type row and column ")
row = int(position[0])
column = int(position[1])

field[row-1][column-1] = "🐇"

print("\n success . . .\n")

print(f"{field[0]}\n{field[1]}\n{field[2]}\n")

