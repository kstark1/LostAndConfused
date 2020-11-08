import pygame
pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Maze Game')   
surface = pygame.display.get_surface() 
add_x_pos = display.get_width() // 10
add_y_pos = display.get_height() // 10

# Colours
white = (255,255,255)
grey = (50, 50, 50)
blue =  ( 0,0, 255)

class Wall:
    def __init__(self, x, y):
        self.wall = pygame.Rect(x,y,add_x_pos,add_y_pos) # Left, top, width, height 
    def draw_wall(self):
        return self.wall
    def wall_pos(self):
        return (self.wall.x,self.wall.y)

class Player:
    def __init__(self,x,y):
        self.player = pygame.Rect(x,y,50,50)



array = [[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,1,0,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0]]

class Board: 
    def __init__(self, array):
        self.array = array
    def draw_board(self):
        y = 0
        for row in array:
            x = 0
            for col in row:
                if col == 0:
                    wall = Wall(x,y)
                    pygame.draw.rect(display, grey, wall.draw_wall(), 2)
                else:
                    wall = Wall(x,y)
                    pygame.draw.rect(display, blue, wall.draw_wall(), 2)


                x += add_x_pos
            y += add_x_pos


#wall = Wall(50,50) # Creating a wall
#width = display.get_width()
#print(wall.wall_pos())


running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    Board.draw_board(array)
    # Testing out drawing the wall
    #pygame.draw.rect(display, white, wall.draw_wall())	
    pygame.display.update()



 
    
