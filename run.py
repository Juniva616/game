import random

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

class Board:
    """
    We 'll live - we'll see.
    """
    def __init__(self, name, size, ship_num):
        self.name = name
        self.size = size
        self.ship_num = ship_num   
        self.board = [["." for x in range(size)] for y in range(size)]      
                            
    def show_board(self):
        print(f"{self.name}'s Board:")
        for row in self.board:  
            print(" ".join(row))  

user_board = Board(name, size, ships_num) 
computer_board = Board('Computer', size, ships_num) 
comp_ships = Board('comp_ships', size, ships_num)

user_board.show_board()
computer_board.show_board()
comp_ships.show_board()

def random_dot(size):
    dot = []
    for i in range(0,2):
        n = random.randint(0,size-1)
        dot.append(n)
    return dot
 
dot = random_dot(size)    
print(dot)





