def game_intro():
    """
    Receives name and area from user's input. Calculates size and ships_number.
    Validates input, raising ValueError.
    """
    name = input("Please, insert your name: \n")
    print()
    print(f"Hello, {name}! To stop the game press CTRL+C, otherwise we continue.")  
    print()

    while True:
        try:
            print("There are 3 sizes of the game board: 4 x 4 = 16, 5 x 5 = 25 and 6 x 6 = 36")
            area = int(input("Please, choose one of the numbers 16, 25 or 36: \n"))
            if area == 16:
                size = 4
                ships_num = 6
                break
            elif area == 25:
                size = 5
                ships_num = 10
                break
            elif area == 36:
                size = 6
                ships_num = 13
                break
            else:
                raise ValueError()
        except ValueError:
            print("Invalid data! Please try again.")          

    return name, size, ships_num

name, size, ships_num = game_intro()
print()
print(f"Dear {name}, you start the game on the {size}x{size} board with {ships_num} ships!")
print()

def player_board(name, size, ships_num):
    """
    Creates a player's board, populates it with ships.
    """
    print(f"{name}'s Board:")
    board = [["." for x in range(size)] for y in range(size)]  
    for row in board:
        print(" ".join(row))

player_board(name, size, ships_num) 

def computer_board(name, size, ships_num):
    """
    Creates a player's board, populates it with ships.
    """
    print(f"{name}'s Board:")
    board = [["." for x in range(size)] for y in range(size)]  
    for row in board:
        print(" ".join(row))

computer_board(name, size, ships_num) 