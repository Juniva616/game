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
print("-" * 35)
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

populate_board(user_ships, ships_num)
populate_board(comp_ships, ships_num)
user_ships.show_board()
#comp_ships.show_board()
computer_board.show_board()

ships_of_user = ships_num
ships_of_comp = ships_num

def ship_check(ships, x, y, who):
    if ships > 0:
        if who == True:
            computer_board.board[x][y] = 'X' 
            comp_ships.board[x][y] = 'X'
            computer_board.show_board()
            user_shoot(who)
        else:
            user_ships.board[x][y] = 'X'
            user_ships.show_board()
            computer_board.show_board()
            comp_shoot()
    else:
        if ships == 0:
            if who == True:
                print("-" * 35)
                print(f"Dear {name}, you have won! Congratulations!")       
            else:
                print(f"Sorry, you are lost. Computer has won this time!")  
            

def user_shoot(who):
    while (who):
        try:
            x = int(input(f"Insert the row (from 0 to {size - 1}): \n"))
            y = int(input(f"Insert the colunm (from 0 to {size - 1}): \n"))
            print(f"You have chosen {(x, y)}.")
            if (0 <= x < size) & (0 <= y < size):
                who = True
                check_shoot(x, y, who, ships_of_user, ships_of_comp)
                break
            else:
                raise ValueError()
        except ValueError:
            print(f"Invalid data! Please choose a number from 0 to {size - 1}.")  
            

def comp_shoot():
    who = False
    x = random_dot(size)
    y = random_dot(size)
    if user_ships.board[x][y] == '.':
        print(f"Computer is shooting at {(x,y)}.")
        check_shoot(x, y, who, ships_of_user, ships_of_comp)
    elif user_ships.board[x][y] == '&':
        print(f"Computer is shooting at {(x,y)}.")
        check_shoot(x, y, who, ships_of_user, ships_of_comp)
    else:
        comp_shoot()


def check_shoot(x, y, who, ships_of_user, ships_of_comp):
    print("-" * 35)
    if (who == True):
        if comp_ships.board[x][y] == '.':
            print("You have missed.")
            comp_ships.board[x][y] = 'o'
            computer_board.board[x][y] = 'o'
            #print(comp_ships.board)
            user_ships.show_board()
            computer_board.show_board()
            who = False
            comp_shoot()
        elif comp_ships.board[x][y] == '&':
            print("You hit Computer's ship! Shoot again.")
            comp_ships.board[x][y] = 'X'
            computer_board.board[x][y] = 'X'
            user_ships.show_board()
            #computer_board.show_board()
            ships_of_comp = ships_of_comp - 1
            print(f"ships_of_comp = {ships_of_comp}" )
            ship_check(ships_of_comp, x, y, who)
        elif comp_ships.board[x][y] == 'o':
            print("You have already shot at this point. Choose another one.")
            user_ships.show_board()
            computer_board.show_board()
            user_shoot(who)
        elif comp_ships.board[x][y] == 'X':  
            print("You have already shot at this point. Choose another one.")
            user_ships.show_board()
            computer_board.show_board()
            user_shoot(who)  
    else:
        if user_ships.board[x][y] == '.':
            print(f"Computer shot at {(x,y)} and missed.")          
            user_ships.board[x][y] = 'o'
            user_ships.show_board()
            computer_board.show_board()
            who = True
            user_shoot(who) 
        elif user_ships.board[x][y] == '&':
            print("Computer hit your ship! It shoots again.")   
            user_ships.board[x][y] = 'X'
            #user_ships.show_board()
            #computer_board.show_board()
            ships_of_user = ships_of_user - 1
            print(f"ships_of_user = {ships_of_user}")
            who = False
            ship_check(ships_of_user, x, y, who)
        elif user_ships.board[x][y] == 'o':
            comp_shoot()
        elif user_ships.board[x][y] == 'X':
            comp_shoot()      
        
who = True
user_shoot(who)
    

