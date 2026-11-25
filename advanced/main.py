grid = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

practice_grid = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

def display_grid(grid):
    print("                 Tic Tac Toe"
          "\nYou can play 2-Player Tic Tac Toe by following this board."
          f"\n{practice_grid}"
          f"\nFor now, you grid is empty:"
          f"\n{grid}"
          "\nPlayer 1 is X and Player 2 is O. Add either X or O by pressing number 1-9. You cannot override previous additions or put in anything that is not X or O."
          "\n")
def play_game(grid):
    while True:
        while True:
            player1 = input("You are X, where would you like to place?"
                            "\n")
            if player1 not in ["1","2","3","4","5","6","7","8","9"]:
                print("Invalid input, try again. Must be between 1 and 9")
            elif player1 == "1":
                if grid[0][0] == "":
                    grid[0][0] = "X"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")

            elif player1 == "2":
                if grid[0][1] == "":
                    grid[0][1] = "X"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player1 == "3":
                if grid[0][2] == "":
                    grid[0][2] = "X"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player1 == "4":
                if grid[1][0] == "":
                    grid[1][0] = "X"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player1 == "5":
                if grid[1][1] == "":
                    grid[1][1] = "X"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player1 == "6":
                if grid[1][2] == "":
                    grid[1][2] = "X"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player1 == "7":
                if grid[2][0] == "":
                    grid[2][0] = "X"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player1 == "8":
                if grid[2][1] == "":
                    grid[2][1] = "X"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player1 == "9":
                if grid[2][2] == "":
                    grid[2][2] = "X"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")

        while True:
            player2 = input("You are O, where would you like to place?"
                            "\n")
            if player2 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print("Invalid input, try again. Must be between 1 and 9")
            elif player2 == "1":
                if grid[0][0] == "":
                    grid[0][0] = "O"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player2 == "2":
                if grid[0][1] == "":
                    grid[0][1] = "O"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player2 == "3":
                if grid[0][2] == "":
                    grid[0][2] = "O"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player2 == "4":
                if grid[1][0] == "":
                    grid[1][0] = "O"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player2 == "5":
                if grid[1][1] == "":
                    grid[1][1] = "O"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player2 == "6":
                if grid[1][2] == "":
                    grid[1][2] = "O"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player2 == "7":
                if grid[2][0] == "":
                    grid[2][0] = "O"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player2 == "8":
                if grid[2][1] == "":
                    grid[2][1] = "O"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")
            elif player2 == "9":
                if grid[2][2] == "":
                    grid[2][2] = "O"
                    for row in grid:
                        print(row[0], "|", row[1], "|", row[2])
                        print("---+---+---")
                    if determine_winner(grid):
                        return
                    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
                        print("All the spots are filled, it is a tie")
                        return
                    break
                else:
                    print("Spot is already taken")


def determine_winner(grid):
    for row in grid:
        if row == ["X", "X", "X"]:
            print("X wins")
            return True
        elif row == ["O", "O", "O"]:
            print("O wins")
            return True

        elif grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
            print("X wins")
            return True

        elif grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
            print("O wins")
            return True


    for column in range(3):
        if grid[0][column] == "X" and grid[1][column] == "X" and grid[2][column] == "X":
            print("X wins")
            return True

        elif grid[0][column] == "O" and grid[1][column] == "O" and grid[2][column] == "O":
            print("O wins")
            return True


    if grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X":
        print("X wins")
        return True
    elif grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O":
        print("O wins")
        return True

    return False
display_grid(grid)
play_game(grid)
