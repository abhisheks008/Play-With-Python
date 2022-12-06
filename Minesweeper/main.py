import pygame
import sys

from random import randrange

# Colors used
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
# Sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30
# Sets the starting number of squares
SQUARES = 10
# Sets the margin between each Box
MARGIN = 5
MENU_SIZE = 40
LEFT_CLICK = 1
RIGHT_CLICK = 3


# Class that holds the game logic          
class Game:
    
    def __init__(self):
        # Create a grid of SQUARES x SQUARES
        self.grid = [[self.Box(x, y) for x in range(SQUARES)] for y in range(SQUARES)]
        self.init = False
        self.game_lost = False
        self.game_won = False
        self.num_bombs = 10
        self.sqx = SQUARES
        self.sqy = SQUARES
        self.resize = False
        self.flag_count = 0

    def draw(self):
        # Set the screen background color
        screen.fill(BLACK)
        # Draw the grid
        for row in range(self.sqy):
            for column in range(self.sqx):
                color = WHITE
                if self.grid[row][column].is_visible:
                     color = RED if self.grid[row][column].has_bomb else YELLOW  
                elif self.grid[row][column].has_flag:
                    color = BLUE
                pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN + MENU_SIZE,
                                WIDTH,
                                HEIGHT])
                self.grid[row][column].show_text()
        
    # Adjusts the grid when the screen size has changed
    def adjustGrid(self, sizex, sizey):
        global screen
        self.sqx = (sizex - MARGIN) // (WIDTH + MARGIN)
        self.sqy = (sizey - MARGIN - MENU_SIZE) // (HEIGHT + MARGIN)
        if self.sqx < 8:
            self.sqx = 8
        if self.sqy < 8:
            self.sqy = 8
        if self.num_bombs > (self.sqx * self.sqy) // 3:
            self.num_bombs = self.sqx * self.sqy // 3
        self.grid = [[self.Box(x, y) for x in range(self.sqx)] for y in range(self.sqy)]
        size = ((self.sqx*(WIDTH + MARGIN) + MARGIN), (self.sqy*(HEIGHT + MARGIN) + MARGIN + MENU_SIZE))
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    # Makes all Boxs visible when user loses
    def gameOver(self):
        for row in range(self.sqy):
            for column in range(self.sqx):
                if self.grid[row][column].has_bomb:
                    self.grid[row][column].is_visible = True
                self.grid[row][column].has_flag = False

    # Changes the number of bombs placed and caps it
    def changeNumBombs(self, bombs):
        self.num_bombs += bombs
        if self.num_bombs < 1:
            self.num_bombs = 1
        elif self.num_bombs > (self.sqx * self.sqy) // 3:
            self.num_bombs = self.sqx * self.sqy // 3
        self.reset() 

    # Place BOMBS on random places
    def placeBombs(self, row, column):
        bombplaced = 0
        while bombplaced < self.num_bombs:
            x = randrange(self.sqy)
            y = randrange(self.sqx)
            if not self.grid[x][y].has_bomb and not (row == x and column == y):
                self.grid[x][y].has_bomb = True
                bombplaced += 1
        self.countAllBombs()
        if self.grid[row][column].bomb_count != 0:
            self.reset()
            self.placeBombs(row, column)
        
    # Count all bombs next to a Box (3x3) for the entire grid
    def countAllBombs(self):
        for row in range(self.sqy):
            for column in range(self.sqx):
                self.grid[row][column].neighborBombCounts(self.sqy, self.sqx)
    
    # Restarts the game
    def reset(self):
        for row in range(self.sqy):
            for column in range(self.sqx):
                self.init = False
                self.grid[row][column].is_visible = False
                self.grid[row][column].has_bomb = False
                self.grid[row][column].bomb_count = 0
                self.grid[row][column].test = False
                self.grid[row][column].has_flag = False
                self.game_lost = False
                self.game_won = False
                self.flag_count = 0

    def checkVictory(self):   
        count = 0
        total = self.sqx * self.sqy
        for row in range(self.sqy):
            for column in range(self.sqx):
                if self.grid[row][column].is_visible:
                    count += 1
        if ((total - count) == self.num_bombs) and not self.game_lost:
            self.game_won = True
            for row in range(self.sqy):
                for column in range(self.sqx):
                    if self.grid[row][column].has_bomb:
                        self.grid[row][column].has_flag = True
        
    
    def countFlags(self):
        total_flags = 0
        for row in range(self.sqy):
            for column in range(self.sqx):
                if self.grid[row][column].has_flag:
                            total_flags += 1
        self.flag_count = total_flags

    # Handle for grid clicks
    def click(self, row, column, button):
        if button == LEFT_CLICK and self.game_won:
                self.reset()
        elif button == LEFT_CLICK and not self.grid[row][column].has_flag: 
            if not self.game_lost:
                # Place bombs after first click so you never click a bomb first
                if not self.init:
                    self.placeBombs(row, column)
                    self.init = True
                # Set the click square to visible
                self.grid[row][column].is_visible = True
                self.grid[row][column].has_flag = False
                if self.grid[row][column].has_bomb:
                    self.gameOver()
                    self.game_lost = True
                if self.grid[row][column].bomb_count == 0 and not self.grid[row][column].has_bomb:
                    self.grid[row][column].openNeighbors(self.sqy, self.sqx)
                self.checkVictory()
            else:
                self.game_lost = False
                self.reset()
        
        elif button == RIGHT_CLICK and not self.game_won:
            if not self.grid[row][column].has_flag:
                if self.flag_count < self.num_bombs and not self.grid[row][column].is_visible:
                    self.grid[row][column].has_flag = True
            else:
                self.grid[row][column].has_flag = False
            self.countFlags()


    # Game Sub-Class for each Box of the grid
    class Box:

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.is_visible = False
            self.has_bomb = False
            self.bomb_count = 0
            self.text = ""
            self.test = False
            self.has_flag = False

        # Handle for the number of bombs text
        def show_text(self):
            if self.is_visible:
                if self.bomb_count == 0:
                    self.text = font.render("", True, BLACK)
                else:
                    self.text = font.render(str(self.bomb_count), True, BLACK)
                screen.blit(self.text, (self.x * (WIDTH + MARGIN) + 10, self.y * (HEIGHT + MARGIN) + 10 + MENU_SIZE))
        
        # Counts how many bombs are next to this Box (3x3)
        def neighborBombCounts(self, sqx, sqy):
            if not self.test:
                self.test = True
                if not self.has_bomb:
                    for column in range(self.x - 1 , self.x + 2):
                        for row in range(self.y - 1 , self.y + 2):
                            if (row >= 0 and row < sqx and column >= 0 and column < sqy
                                and not (column == self.x and row == self.y)
                                and game.grid[row][column].has_bomb):
                                    self.bomb_count += 1
        
        # Open all Boxs next to the clicked Box with zero bombs nearby
        def openNeighbors(self, sqx, sqy):
            column = self.x
            row = self.y
            for row_off in range(-1, 2):
                for column_off in range(-1, 2):
                    if ((row_off == 0 or column_off == 0) and row_off != column_off
                        and row+row_off >= 0 and column+column_off >=0 and row+row_off < sqx and column+column_off < sqy):
                            game.grid[row + row_off][column + column_off].neighborBombCounts(game.sqy, game.sqx)
                            if not game.grid[row + row_off][column + column_off].is_visible and not game.grid[row + row_off][column + column_off].has_bomb:  
                                    game.grid[row + row_off][column + column_off].is_visible = True
                                    game.grid[row + row_off][column + column_off].has_flag = False
                                    if game.grid[row + row_off][column + column_off].bomb_count == 0: 
                                        game.grid[row + row_off][column + column_off].openNeighbors(game.sqy, game.sqx)


class Menu():

    def __init__(self):
        self.width = pygame.display.get_surface().get_width() - 2*MARGIN
        self.btn_minus = self.Button(20, 10, 20, 20, "-", 6, -3)
        self.btn_plus = self.Button(70, 10, 20, 20, "+", 3, -4)
        self.btn_flags = self.Button(300, 16, 10, 10, "")
        self.btn_flags.background = RED
        self.label_bombs = self.Label(41.5, 10)
        self.label_game_end = self.Label(100, 10)
        self.label_flags = self.Label(self.width - 30, 10)
        self.label = self.Label((self.width/3), 10)

    def click(self, obj):
        if self.btn_minus.click():
            obj.changeNumBombs(-1)
        if self.btn_plus.click():
            obj.changeNumBombs(1)
        
    def draw(self, obj):
        self.width = pygame.display.get_surface().get_width() - 2*MARGIN 
        pygame.draw.rect(screen, YELLOW, [MARGIN, 0, self.width, MENU_SIZE])
        self.btn_minus.draw(screen)
        self.btn_plus.draw(screen)
        self.btn_flags.draw(screen)
        self.label_bombs.show(screen, game.num_bombs)
        self.label.show(screen, "Minesweeper")
        self.label_flags.show(screen, game.flag_count)
        if obj.game_lost:
            self.label_game_end.show(screen, "Game Over")
        elif obj.game_won:
            self.label_game_end.show(screen, "You Won!")
    

    class Label:
    
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.text = ""
        
        def show(self, surface, value): 
            text = str(value)
            self.text = font.render(text, True, BLACK)     
            surface.blit(self.text, (self.x, self.y))
    

    class Button:

        def __init__(self, x, y, width, height, text, xoff=0, yoff=0):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.background = WHITE
            self.text = text
            self.x_offset = xoff
            self.y_offset = yoff

        def draw(self, surface):
            pygame.draw.ellipse(surface, self.background, [self.x, self.y, self.width, self.height], 0)
            text = font.render(self.text, True, BLACK)     
            surface.blit(text, (self.x + self.x_offset, self.y + self.y_offset))
        
        def click(self):
            pos = pygame.mouse.get_pos()
            if pos[0] > self.x and pos[1] > self.y and pos[0] < (self.x + self.width) and pos[1] < (self.y + self.height):
                return True
            else:
                return False


# Initialize pygame and sets screen size and caption
pygame.init()
size = (SQUARES*(WIDTH + MARGIN) + MARGIN, (SQUARES*(HEIGHT + MARGIN) + MARGIN) + MENU_SIZE)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Minesweeper")
# Font to use in the entire game
font = pygame.font.Font('freesansbold.ttf', 25)
# Create instances for Game and Menu
game = Game()
menu = Menu()
clock = pygame.time.Clock()
# Main loop
while True:
    for event in pygame.event.get():
        # Closes the game if user clicked the X
        if event.type == pygame.QUIT:  
            pygame.quit()
            sys.exit()
        # Mouse clicks event
        elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse position
                position = pygame.mouse.get_pos()
                # Change the screen coordinates to grid coordinates and caps max values
                column = position[0] // (WIDTH + MARGIN)
                row = (position[1] - MENU_SIZE) // (HEIGHT + MARGIN)
                if row >= game.sqy:
                    row = game.sqy - 1
                if column >= game.sqx:
                    column = game.sqx - 1
                if row >= 0:
                    game.click(row, column, event.button)
                else:
                    menu.click(game)
        # Event for screen resize    
        elif event.type == pygame.VIDEORESIZE:
            if game.resize: 
                game.adjustGrid(event.w, event.h)
                game.reset()
            else:  
                game.resize = True
    game.draw()
    menu.draw(game)
    clock.tick(60)
    # Update the screen
    pygame.display.flip()
