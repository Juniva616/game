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
ships_of_user = ships_num
ships_of_comp = ships_num
print()
print(f"Dear {name}, you start the game on the {size}x{size} board with {ships_num} ships!")
print()

class Board:
    """
    Creates game boards.
    """
    def __init__(self, name, size, ships_num):
        self.name = name
        self.size = size
        self.ships_num = ships_num   
        self.board = [["." for x in range(size)] for y in range(size)]      
                            
    def show_board(self):
        print(f"{self.name}'s Board:")
        for row in self.board:  
            print(" ".join(row))  


def random_dot(size):
    n = random.randint(0,size-1)
    return n


def populate_board(player, ships_num):
    while ships_num > 0:
        x = random_dot(size)
        y = random_dot(size)
        if player.board[x][y] == '.': 
            player.board[x][y] = '&'
            ships_num -= 1
        else:
            pass             


user_ships = Board(name, size, ships_num) 
computer_board = Board('Computer', size, ships_num) 
comp_ships = Board('comp_ships', size, ships_num)

#user_board.show_board()
#comp_ships.show_board()
#print(user_board.board[1][1])
#random_dot(size)
populate_board(user_ships, ships_num)
populate_board(comp_ships, ships_num)
user_ships.show_board()
comp_ships.show_board()
computer_board.show_board()

def ship_check(ships, who):
    if ships > 0:
        if who == True:
            computer_board.board[x][y] = 'X' 
            comp_ships.board[x][y] = 'X'
            computer_board.show_board()
            user_shoot()
        else:
            user_ships.board[x][y] == 'X'
            user_ships.show_board()
            comp_shoot()
    else:
        if ship == 0:
            if who == True:
                print(f"Dear {name}, you have won! Congratulations!")       
            else:
                print(f"Sorry, you are lost. Computer has won this time!")  
            

def user_shoot(who):
    while (who):
        try:
            x = int(input(f"Insert the row (from 0 to {size - 1}). \n"))
            y = int(input(f"Insert the colunm (from 0 to {size - 1}). \n"))
            print(f"You have chosen {(x, y)}.")
            if (0 <= x < size) & (0 <= y < size):
                who = True
                check_shoot(x, y, who)
                break
            else:
                raise ValueError()
        except ValueError:
            print(f"Invalid data! Please choose a number from 0 to {size - 1}.")  
            

def comp_shoot():
    who = False
    x = random_dot(size)
    y = random_dot(size)
    check_shoot(x, y, who)


def check_shoot(x, y, who):
    if who == True:
        if comp_ships.board[x][y] == '.':
            print("You have missed.")
            comp_ships.board[x][y] == 'o'
            who = False
            comp_shoot()
        elif comp_ships.board[x][y] == '&':
            print("You hit Computer's ship!")
            comp_ships.board[x][y] == 'X'
            ships_of_comp -= 1
            ship_check(ships_of_comp)
        elif comp_ships.board[x][y] == 'o' or 'X':
            print("You have already shot at this point. Choose another one.")
            user_shoot()
    else:
        if user_ships.board[x][y] == '.':
            print(f"Computer shot at {(x,y)} and missed.")          
            user_ships.board[x][y] == 'o'
            who = True
            user_shoot() 
        elif user_ships.board[x][y] == '&':
            print("Computer hit your ship!")   
            user_ships.board[x][y] == 'X'
            ships_of_user -= 1
            who = False
            ship_check(ships_of_user)
        elif user_ships.board[x][y] == 'o' or 'X':
            comp_shoot()
               
        
who = True
user_shoot(who)
    

