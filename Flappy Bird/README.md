# FLAPPY BIRDS #

### GOAL ###

The game is a side-scroller where the player controls a bird, attempting to fly between columns of green pipes without hitting them. 

The moment you hit the pipes, you loose the game. 

### DESCRIPTION ###

 The player has to save the bird from colliding with the hurdles like pipes.
 
 Each time the bird passes through the pipes, the score gets incremented by one. The game ends when the bird collides with the pipes or falls down due to gravity. The sections below describe the steps that have to be taken for building this game.


### WHAT I HAD DONE ### 

1) Import Libraries - pygame  and functions like random, os, time etc.

2) Define the height, width and several features of the window. 

3) Initialise the images required to play the game- base, background, pipe, birds.

**Class Required**

  4) Class Bird:

  a) Initialise the velocity, height, width, gravity variables.
  
  b) Jump function- to make the bird jump by certain velocity.
  
  c) move function- Calculate displacement, terminal velocity etc.
  
  5) Class Pipe: 

  a) Initialise the height, width, gap, velocity etc of the base.
  
  b) set height function - to assign random height to the pipes. 
  
  c) move function - assign certain velocity. 
  
  d) collide function - If pipe and bird collide, we return to 0 Score. 
  
  6) Class Base:
   
   a) move floor of the game 
   
  7) Other functions: 

  a) create menu screen. 
  
  b) end screen. 
  
  c) Score window. 
  
  d) create the main game screen 





### LIBRARIES NEEDED ###

The libraries that are required are: 

pygame 2.1.2 



### DEMONSTRATION ###

https://drive.google.com/file/d/1cQjocJGrLMk2SZozC5cXuLleEVq_DicX/view?usp=sharing

### Shreya Ganjoo ### 
