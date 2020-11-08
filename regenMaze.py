import pygame
import random
from mazegen import *

### Display Variables
TITLE = 'Maze Game' # Title that appears in the window title
FPS = 30 # Frames per second
WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# Colour Variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
BLUE = (0, 0, 255)
DARK_GREEN = (28,84,35) # Used to fill in the rest of the screen that does not contain rects
LIGHT_BLUE = (96, 166, 191) # Used for the walls (rects)
### Create the window

screen = pygame.display.set_mode(SCREENDIM) # creates the main surface where all other assets are place on top
pygame.display.set_caption(TITLE) # updates the window title w/ TITLE
screen.fill(GREY) # Fills the entire surface w/ the colour --> fill = erase/clear

clock = pygame.time.Clock() # starts a clock obj to measure time

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, state, colour):
        pygame.sprite.Sprite.__init__(self)
        self.state = state #Can change to 1 to test over tile
        self.image = pygame.Surface((40, 30))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.center = (((x * 40) + 20), ((y * 30) + 15))


#Random tile to test collision
#square = Tile()
wall_tiles = pygame.sprite.Group()
walk_tiles = pygame.sprite.Group()

#if square.state == 0:
#    wall_tiles.add(square)
#else:
#    walk_tiles.add(square)

obj = MazeGen()
obj.empty_maze()
obj.set_start()
obj.new_connection()
obj.set_end()
obj.connect_points()
obj.print_maze()
print(obj.connections)
obj.set_dead_connects()
obj.dead_end_points()
obj.print_maze()


positionState = obj.get_maze()
for i in range(20):
    for j in range(20):
        if positionState[i][j] == 0:
            colour = DARK_GREEN
        else:
            colour = LIGHT_BLUE
        tile = Tile(j, i, positionState[i][j], colour)
        if tile.state == 0:
            wall_tiles.add(tile)
        else:
            walk_tiles.add(tile)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 8, HEIGHT / 8)

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y
    
    def get_grid_pos(self):
        return [self.rect.y//30, self.rect.x//40]

player_sprite = pygame.sprite.Group()
player = Player()
player_sprite.add(player)

running = True

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and (pygame.sprite.spritecollideany(player, wall_tiles, collided = None) == None):
                player_sprite.update(-10, 0)
                if pygame.sprite.spritecollideany(player, wall_tiles, collided = None) != None:
                    player_sprite.update(10, 0)

            if event.key == pygame.K_RIGHT and (pygame.sprite.spritecollideany(player, wall_tiles, collided = None) == None):
                player_sprite.update(10, 0)
                if pygame.sprite.spritecollideany(player, wall_tiles, collided = None) != None:
                    player_sprite.update(-10, 0)

            if event.key == pygame.K_UP and (pygame.sprite.spritecollideany(player, wall_tiles, collided = None) == None):
                player_sprite.update(0, -10)
                if pygame.sprite.spritecollideany(player, wall_tiles, collided = None) != None:
                    player_sprite.update(0, 10)

            if event.key == pygame.K_DOWN and (pygame.sprite.spritecollideany(player, wall_tiles, collided = None) == None):
                player_sprite.update(0, 10)
                if pygame.sprite.spritecollideany(player, wall_tiles, collided = None) != None:
                    player_sprite.update(0, -10)
            if event.key == pygame.K_r: ############################## regenerate maze
                # regenerate maze
                obj = MazeGen()
                obj.empty_maze()
                obj.set_start(player.get_grid_pos())
                obj.new_connection()
                obj.set_end()
                obj.connect_points()
                print(player.get_grid_pos())
                obj.set_dead_connects()
                obj.dead_end_points()
                obj.print_maze()

                walk_tiles.empty()
                wall_tiles.empty()
                positionState = obj.get_maze()
                for i in range(20):
                    for j in range(20):
                        if positionState[i][j] == 0:
                            colour = DARK_GREEN
                        else:
                            colour = LIGHT_BLUE
                        tile = Tile(j, i, positionState[i][j], colour)
                        if tile.state == 0:
                            wall_tiles.add(tile)
                        else:
                            walk_tiles.add(tile)

    # Testing out drawing the wall
    #pygame.draw.rect(display, white, wall.draw_wall())	
    
    pygame.display.update()
    screen.fill(GREY)
    
    wall_tiles.draw(screen)
    walk_tiles.draw(screen)
    
    player_sprite.draw(screen)
