# 2048 GAME IN PYTHON 

### GOAL

This is a mathematical puzzle game with the aim to reach 2048 before the board fills up. The game has to reach 2048 before all tiles have been filled!

### DESCRIPTION

 When two equal tiles collide, they combine to give you a tile that displays their sum. The more you do this, the higher the tiles get !
 This project has been created using Data Structures and Algorithms in Python language. 

### WHAT I HAD DONE

Classes have been defined in the given code: 
   1) **Board**: 
   In this I decided the background color and tile colors of the board game, along with initialising variables like score, grid, main_window, board etc,
   along with initialising functions specifically: 
      1) __init__(self): which initialise the above mentioned variables
      2) Transpose: Uses zip function to get the transpose 
      3) Reverse: To reverse the grid matrix 
      4) CompressGrid: Moves all non empty to the left side to simplify merging! 
      5) mergeGrid: It adds the grid value of two adjacent tiles if they have same grid values.
      6) Random_cell: It first stores all the empty cells in a list and then picks a random cell from the created list and make its grid value 2
      7) Can_merge: It returns a boolean value denoting we can merge any two tiles or not. We can merge two tiles if and only if they hold the same grid value.
      8) paintGrid: It assigns foreground and background color to each tile of the 4×4 grid corresponding to its grid value.
   2) **Game**: 
   Functions:
      1) __init__(self): It is the constructor function. It initializes all the variables with appropriate default values.
      2) start: It calls random_cell twice to assign ‘2’ to grid value of two random cells/tiles,
         and then it paints the grid and after that, it calls link_keys to link up, down, left, and right keys.
      3) Link_keys: It initially checks if the game is already won or lost, and if it is, it executes a return statement without doing anything. 
         Otherwise, it continues the execution procedure. 

### LIBRARIES NEEDED

The follwing are required :
     1) Tkinter - The GUI library (python)
     
     2) Basics and DSA in python. 
     
     
### DEMONSTRATION 

https://drive.google.com/file/d/1iTS2wU-UZ7ZeiQCI2A1W8D_NX4q-Xqvi/view?usp=sharing


### NAME
 Shreya Ganjoo
