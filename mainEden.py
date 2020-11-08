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

### Create the window

screen = pygame.display.set_mode(SCREENDIM) # creates the main surface where all other assets are place on top
pygame.display.set_caption(TITLE) # updates the window title w/ TITLE
screen.fill(GREY) # Fills the entire surface w/ the colour --> fill = erase/clear

clock = pygame.time.Clock() # starts a clock obj to measure time

running = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 4, HEIGHT / 4)

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y

player_sprite = pygame.sprite.Group()
player = Player()
player_sprite.add(player)


while running:
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # if the red x was clicked eg buttons in corner of the window
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_sprite.update(-10, 0)
            if event.key == pygame.K_RIGHT:
                player_sprite.update(10, 0)
            if event.key == pygame.K_UP:
                player_sprite.update(0, -10)
            if event.key == pygame.K_DOWN:
                player_sprite.update(0, 10)

    clock.tick(FPS)  # pause the game until the FPS time is reached
    pygame.display.flip()  # update the screen with changes, similar to sync() in AGK

    pressedKeys = pygame.key.get_pressed()

    screen.fill(GREY)
    player_sprite.draw(screen)
    