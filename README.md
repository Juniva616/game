# THE SEA BATTLE GAME

The Sea Battle game is a Python terminal game, which runs in the Code Insitute mock terminal on Heroku.

The Sea Battle game is played on two ruled grids on which each player's fleet of battleships are marked. The locations of the fleets are concealed from the other player. Players call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

The application provides a working the Sea Battle game for a single user to play against the computer.

 ![The game on different screen sizes](https://github.com/Juniva616/game/blob/main/readme-files/md-screens.png)

## How to play

The rules are similar to the classic pencil and paper game. More info you can find on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

In this version the player enters their name and can choose one of three sizes of the game boards: 4 x 4 = 16, 5 x 5 = 25 and 6 x 6 = 36.
For each size of the board the quantity of the ships are preset automatically and their positions on the boards are generated randomly for both players
(a human and a computer).

The player can see own ships, but cannot see  the opponent's ships. The player makes a shot by choosing two numbers (coordinates on the game board). 

Ships are indicated by '&' sign.  Missed shots are marked on the board with an 'o' sign. Hits are indicated by 'X'.

The player and the computer then take it in turns to make shots and try to sink each other's ships. If the player hits the ship he/she is entitled to one more shot. If the player misses, then it is the opponent's turn to shoot. The same rule applies to the computer.

The winner is the player who sinks all of their opponent's ships first.
 
 
# Features


## Existing features
- Accepts User's input: 
    - The player enters their name
    - The player is greeted by name
    - The player can choose the grid size
   
    ![The input of the name and grid size ](https://github.com/Juniva616/game/blob/main/readme-files/md-maria16.png)    

- Random board generation
    - Ships are randomly placed on both the player and the computer boards
    - The player cannot see where the computer's ships are.

    ![The game boards screen. ](https://github.com/Juniva616/game/blob/main/readme-files/md-shot.png)  

- Input validation and error-checking
    - You cannot enter a name longer than 15 characters   

        ![The name length validation](https://github.com/Juniva616/game/blob/main/readme-files/md-longname.png) 

    - You cannot enter coordinates outside the size of the game board 
     
         ![The coordinates input validation](https://github.com/Juniva616/game/blob/main/readme-files/md-coord.png)  

     - You must enter valid numbers for coordinates and the game board

         ![The board size input validation](https://github.com/Juniva616/game/blob/main/readme-files/md-invaliddata.png)  


    - You cannot enter the same coordinates for a shot twice      

- Immediate Feedback 
    - Shows the player's input of the shot coordinates 
    - Shows the computer choice of the shot coordinates
    - Shows scores of the remained ships after each hit

- Play agains the computer
- Accepts user inputs
- Data maintained in  class instances
- Congratulations at the end of the game

 ![The end of game screen. ](https://github.com/Juniva616/game/blob/main/readme-files/md-gameover.png)  
 

## Data Model

My program uses OOP principles, in particular, the program creates two instances of the Board class to contain the player's board and the computer's board.

The Board class stores the board size,  the number of ships, the position of the ships, the killed and missed shots, a populate_board method to populate boards with ships and a show_board method to display the players' boards.

The logic of the game is implemented by a few functions that call each other in the due order.

## Testing

- The program has been tested in VSCode editor and successfully run many times in its terminal.
- The program was run many times during debugging and I confirm that the program works well, without any breaks or errors.
- Input validation, implemented in the program, tested by entering invalid data for each of input position and proves to adequately and politely tolerate any user input errors.
- After deployment the game was tested in the Code Institute Heroku terminal.

## Validation
### Python code validation

The code has passed through validation in VSCode in-built linter flake8 without any errors.

There are a few warnings caused by the using ASCII characters for drawing the ship. The ship image is an important feature that improves User Experience. 
 

## Technologies Used

### Language Used
- Python 3

### Sites & Programs Used

- VSCode:
VSCode was used for editing the code, commiting and pushing it to GitHub.

- Git:
Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

- GitHub:
GitHub is used to store the projects code after being pushed from Git.

- Paint:
Paint was used to create images for README.md.

- The site https://ui.dev/amiresponsive
The site allowed to get a nice picture demonstrating how The Sea Battle game will look on different devices.

- Google Translate:
https://translate.google.com/

 
## Unfixed bugs

No unfixed bugs.

## Deployment

The project was deployed using the Code Institute's mock terminal for Heroku.

Steps for deployment:

    - Fork or clone this repository
    - Create a new Heroku App
    - Set the buidbacks to Python and NodeJS in that order
    - Link the Heroku App to the repository
    - Click on Deploy

The URL on GitHub with my project is ![https://github.com/Juniva616/game](https://github.com/Juniva616/game)

The live link to my project is ![https://shoot-ships.herokuapp.com/](https://shoot-ships.herokuapp.com/)

## Credits
- My Mentor for precious advice during making the project
- Tutors of the Code Institute for their valuable help with code issues
- The Code Institute for the deployment terminal and for the perfect lessons and practices
