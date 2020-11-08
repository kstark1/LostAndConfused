import pygame
pygame.init()
display = pygame.display.set_mode((800, 600)) # Game display
pygame.display.set_caption('Maze Game')   
surface = pygame.display.get_surface() 

# Will be used to determine the rect's position
add_x_pos = display.get_width() // 10
add_y_pos = display.get_height() // 10

# Colours that I'm playing around with
white = (255,255,255)
grey = (50, 50, 50)
blue =  ( 0,0, 255)
dark_green = (28,84,35) # Used to fill in the rest of the screen that does not contain rects
light_blue = (96, 166, 191) # Used for the walls (rects)

# ----------------------------------------------------------------------------------
class Wall:
    def __init__(self, x, y):
        self.wall = pygame.Rect(x,y,add_x_pos,add_y_pos) # Left, top, width, height 
    def get_wall(self):
        return self.wall # Will be used in pygame.draw.rect() later on
    def wall_pos(self):
        return (self.wall.x,self.wall.y) # returns the x and y coordinates of the rect

# ---------------------------------------------------------------------------------------
class Player: # Will be worked on later (for now, added attribute(s) that might be used??)
    def __init__(self,x,y):
        self.player = pygame.Rect(x,y,50,50)
    def get_pos(self):
        return (self.player.x, self.player.y)
# ---------------------------------------------------------------------------------------
# An array to test with
array = [[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,1,0,1,0,0,0],[1,1,0,0,0,1,0,0,0,0],
[1,1,0,1,0,0,0,1,0,0],[1,1,0,0,0,0,1,0,0,0],[1,1,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,1,0,1,0],[1,1,0,0,0,1,1,1,0,0],[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0]]
# ------------------------------------------------------------------------------------
class Board: 
    def __init__(self, array):
        self.array = array
    def draw_board(self): # Draws the board using the array given
        y = 0
        for row in array:
            x = 0
            for col in row:
                if col == 0:
                    wall = Wall(x,y) # Creates a wall
                    pygame.draw.rect(display, light_blue, wall.get_wall()) # Draws the wall
 
                x += add_x_pos
            y += add_y_pos

# ------------------------------------------------------------------------------------
# Used to run the game
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    display.fill(dark_green) # Fills the rest of the screen with dark green
    Board.draw_board(array) # Adds the rects(walls)
    pygame.display.update()



 
    
