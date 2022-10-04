import random

def game_intro():
    """
    Receives name and area from user's input. Calculates size and ships_number.
    """
    name = input("Please, insert your name: \n")  
    print()
    print(f"Hello, {name}!")

    while True:
        print("There are 3 sizes of the game board: 4 x 4 = 16, 5 x 5 = 25 and 6 x 6 = 36")
        area = int(input("To choose the board area, enter one of the numbers 16, 25 or 36: \n"))   
        player = True
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
            print("Wrong input! Please enter one of these numbers: 16, 25, 36")
         
        
    print("!!!----> REMEMBER! If you want to stop the game, press CTRL+C <----!!!!!")
        
    return name, size, player, ships_num

name, size, player, ships_num = game_intro()
print()
print(f"Dear {name}, you start the game on the {size}x{size} board with {ships_num} ships!")
print()







#print(random.randint(0, 3))

