import pygame

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
### Create the window

screen = pygame.display.set_mode(SCREENDIM) # creates the main surface where all other assets are place on top
pygame.display.set_caption(TITLE) # updates the window title w/ TITLE
screen.fill(GREY) # Fills the entire surface w/ the colour --> fill = erase/clear

clock = pygame.time.Clock() # starts a clock obj to measure time

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.state = 0 #Can change to 1 to test over tile
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 6, HEIGHT / 6)

#Random tile to test collision
square = Tile()
wall_tiles = pygame.sprite.Group()
walk_tiles = pygame.sprite.Group()
if square.state == 0:
    wall_tiles.add(square)
else:
    walk_tiles.add(square)

#wall = Wall(50,50) # Creating a wall
#width = display.get_width()
#print(wall.wall_pos())

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

    # Testing out drawing the wall
    #pygame.draw.rect(display, white, wall.draw_wall())	
    
    pygame.display.update()
    screen.fill(GREY)
    
    wall_tiles.draw(screen)
    walk_tiles.draw(screen)
    
    player_sprite.draw(screen)
    