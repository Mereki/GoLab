# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Mandapat
#               Mason McIntosh
#               Diego Arroyo
#               Lisandro Demagistris
# Section:      509
# Assignment:   Go Lab
# Date:         8 October 2023

board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]  # board initialized beforehand


def pboard(b):  # prints out board to console
    for row in b:
        for j in row:
            print(j, end="")
        print()


def update(b, x, y, ply):  # update board on x,y coordinate, piece dependent on player
    if ply == "Black":
        b[x][y] = chr(9675)
    else:
        b[x][y] = chr(9679)


def player(c):  # Updates turn
    if c % 2 == 0:  # Black
        return "Black"
    else:
        return "White"  # White


count = 0
resp = ""

while resp != "stop":
    pboard(board)  # Draw board before every iteration
    person = player(count)  # Update player turn

    resp = input(f"({person}) Please enter a coordinate in range 0-8, and in the format: x y, or enter \"stop\" to "
                 f"end the game: ") # format input as "x y" without quotations, user input
    if resp == "stop":
        break
    elif len(resp) <= 1 or len(resp) == 2 or len(resp) > 3:  # input must meet correct format: x (space) y
        print("Invalid input, try again")
        continue

    sep = resp.split(" ")
    x = sep[0]
    y = sep[1]

    if not x.isnumeric():  # Checks if x is numeric
        print("X value is not numeric, try again")
        continue
    elif not y.isnumeric():  # Checks if y is numeric
        print("Y value is not numeric, try again")
        continue
    elif x == "9" or y == "9":  # Out of bounds if value is 9 (0-8)
        print("Out of bounds, try again")
        continue
    else:
        x = int(x)
        y = int(y)

    if (board[x][y] == chr(9675)) or (board[x][y] == chr(9679)):  # If user choice has a piece on the spot, invalid
        print("Illegal move. Try again")
        continue
    elif person == "Black" or person == "White":  # If input passes all checks, proceed to place piece onto board
        update(board, x, y, person)
        count += 1

# If user input == "stop", prints out board once more and gives out a conclusion message
pboard(board)
print("Game has concluded.")
