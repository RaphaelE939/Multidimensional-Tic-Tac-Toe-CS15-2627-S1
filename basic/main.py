grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]



def display_grid(grid):
    for row in grid:
        print(row[0], "|", row[1], "|", row[2])
        print("---+---+---")
def determine_winner(grid):
    tho = False
    for row in grid:
        if row == ["X","X","X"]:
            print("X wins")
            tho = True
            break
        elif row == ["O","O","O"]:
            print("O wins")
            tho = True
            break
        elif grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
            print("X wins")
            tho = True
            break
        elif grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
            print("O wins")
            tho = True
            break

    for column in range(3):
        if grid[0][column] == "X" and grid[1][column] == "X" and grid[2][column] == "X":
            print("X wins")
            tho = True
            break
        elif grid[0][column] == "O" and grid[1][column] == "O" and grid[2][column] == "O":
            print("O wins")
            tho = True
            break

    if grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X":
        print("X wins")
        tho = True
    elif grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O":
        print("O wins")
        tho = True

    if tho == False:
        print("No one wins, its a tie.")


display_grid(grid_1)
determine_winner(grid_1)
print("\n")
display_grid(grid_2)
determine_winner(grid_2)
print("\n")
display_grid(grid_3)
determine_winner(grid_3)
print("\n")
display_grid(grid_4)
determine_winner(grid_4)
