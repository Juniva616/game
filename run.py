import random


name = input("Please, insert your name: \n")  
print()
print(f"Hello, {name}!")
print("There are 3 sizes of the game board: 4 x 4 = 16, 5 x 5 = 25 and 6 x 6 = 36")
area = input("To choose the area, enter one of this numbers 16, 25 or 36: \n") 
if area == 16:
    size = 4
    ships_num = 6   
    Board(name, area, player, ships_num) 
elif area == 25:
    size = 5
    ships_num = 10 
    Board(name, area, player, ships_num)  
elif area == 36:
    size = 6
    ships_num = 13   
    Board(name, area, player, ships_num)    
else:
    print("Please enter one of these numbers: 16, 25, 36")

print("REMEMBER! If you want to stop the game, press CTRL+C ")

player = True





#print(random.randint(0, 3))

