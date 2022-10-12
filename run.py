""" This module imports in-built module to generate random numbers."""
import random


def game_intro():
    """
    Shows welcoming information.
    Receives name and area from user's input. Validates name's length.
    Calculates the board size and ships_number.
    Validates input, raising ValueError.
    """
    print('*' * 55)
    print('*' * 55)
    print("*********    WELCOME TO THE SEA BATTLE GAME!    *******")
    print("*        There are 3 sizes of the game board:")
    print("*       4 x 4 = 16, 5 x 5 = 25 and 6 x 6 = 36")
    print("*  To stop the game press CTRL+C, otherwise we continue")
    print('*' * 55)
    print("*  Top left corner is:    row: 0    column: 0")
    print()
    print("*    & - ships     X - killed ships     o - missed")
    print('*' * 55)
    naming = False
    while not naming:
        _name = input("Please, insert your name: \n")
        print()
        if len(_name) < 15:
            naming = True
        else:
            print("The name is too long! Please, shorten it!")
            print()
    print(f"Hello, {_name}!")
    print()
    while True:
        try:
            area = int(
                input("Please, choose the board size - 16, 25 or 36: \n")
            )
            if area == 16:
                _size = 4
                _ships_num = 6
                break
            if area == 25:
                _size = 5
                _ships_num = 10
                break
            if area == 36:
                _size = 6
                _ships_num = 13
                break
            raise ValueError()
        except ValueError:
            print("Invalid data! Please try again.")

    return _name, _size, _ships_num


class Board():
    """
    Creates game boards.
    """
    def __init__(self, names, sizes, ships_nums):
        self.name = names
        self.size = sizes
        self.ships_num = ships_nums
        self.board = [["." for x in range(size)] for y in range(size)]  # noqa

    def show_board(self):
        """
        Shows game board.
        """
        print(f"{self.name}'s Board:")
        for row in self.board:
            print(" ".join(row))


def random_dot(size):
    """
    Gets random integers within board sizes.
    """
    return random.randint(0, size-1)


def populate_board(player, ships_num):
    """
    Populates game boards with ships randomly.
    """
    while ships_num > 0:
        x = random_dot(size)
        y = random_dot(size)
        if player.board[x][y] == '.':
            player.board[x][y] = '&'
            ships_num -= 1
        else:
            pass


def user_shoot(who):
    """
    Gets user's input as (x,y) coordinates.
    Checks if the coordinates are within the game board measures,
    raises ValueError if they are not.
    """
    while who:
        try:
            x = int(input(f"Insert the row (from 0 to {size - 1}): \n"))
            y = int(input(f"Insert the colunm (from 0 to {size - 1}): \n"))
            print(f"You are shooting at {(x, y)}.")
            if (0 <= x < size) & (0 <= y < size):
                who = True
                check_shoot(x, y, who)
                break
            else:
                raise ValueError()
        except ValueError:
            print(f"Invalid data! Please choose \
a number from 0 to {size - 1}.")


def comp_shoot():
    """
    Gets random coordinates for Computer's shoots.
    Checks if the coordinates have already been used or not.
    """
    who = False
    x = random_dot(size)
    y = random_dot(size)
    if user_ships.board[x][y] == '.':
        print(f"Computer is shooting at {(x,y)}.")
        check_shoot(x, y, who)
    elif user_ships.board[x][y] == '&':
        print(f"Computer is shooting at {(x,y)}.")
        check_shoot(x, y, who)
    else:
        comp_shoot()


def check_shoot(x, y, who):
    """
    Checks where the shoot got, updates and shows
    the game boards, both for the user and Computer.
    """
    print("-" * 35)
    if who is True:
        if comp_ships.board[x][y] == '.':
            print("You have missed.")
            comp_ships.board[x][y] = 'o'
            computer_board.board[x][y] = 'o'
            user_ships.show_board()
            computer_board.show_board()
            who = False
            comp_shoot()
        elif comp_ships.board[x][y] == '&':
            print("You hit Computer's ship! Shoot again.")
            comp_ships.board[x][y] = 'X'
            computer_board.board[x][y] = 'X'
            user_ships.show_board()
            computer_board.show_board()
            ship_check(who)
        elif comp_ships.board[x][y] == 'o':
            print("You have already shot at this point. \
Choose another one.")
            user_ships.show_board()
            computer_board.show_board()
            user_shoot(who)
        elif comp_ships.board[x][y] == 'X':
            print("You have already shot at this point. \
Choose another one.")
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
            who = False
            user_ships.show_board()
            computer_board.show_board()
            ship_check(who)
        elif user_ships.board[x][y] == 'o':
            comp_shoot()
        elif user_ships.board[x][y] == 'X':
            comp_shoot()


def ship_check(who):
    """
    Checks if all the ships are shot. If so, ends the game.
    """
    print("-" * 35)
    if who is True:
        fleet = comp_ships.board
        ships = 0
        for ship in fleet:
            alive_ships = ship.count('&')
            ships += alive_ships
        print(f"Computer has {ships} ships now. ")

        if ships == 0:
            print(f"Well done, {name}, you have won! \
Congratulations!")
            game_over()
        else:
            user_shoot(who)
    else:
        fleet = user_ships.board
        ships = 0
        for ship in fleet:
            alive_ships = ship.count('&')
            ships += alive_ships
        print(f"You have {ships} ships now. ")
        if ships == 0:
            print(f"Sorry, {name}, you have lost! \
Computer has won this time!")
            game_over()
        else:
            comp_shoot()


def game_over():
    """
    Finishes the game and prints farewell message.
    """
    print()
    print("*" * 50)
    print("*               GAME IS OVER!                    *")
    print("*       Thank you for playing our game!          *")
    print("*                                                *")
    print("*" * 50)
    print("                    |>>")
    print("                    |")
    print("              _____/|\_____")
    print("              \--<>---<>--/")
    print("      ~ ~ ~ ~ ~\~~~~~~~~~/~ ~ ~ ~ ~ ~")
    print("     ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ")
    print()


name, size, ships_num = game_intro()
print("-" * 50)
print(f"Dear {name}, you start the game on the {size}x{size} \
board with {ships_num} ships!")
print()

user_ships = Board(name, size, ships_num)
computer_board = Board('Computer', size, ships_num)
comp_ships = Board('comp_ships', size, ships_num)
populate_board(user_ships, ships_num)
populate_board(comp_ships, ships_num)
user_ships.show_board()
computer_board.show_board()

who = True
user_shoot(who)
