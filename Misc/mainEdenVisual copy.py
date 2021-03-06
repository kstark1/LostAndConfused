import pygame
import random
import convoGen
import Conversation

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
        self.corner = (x,y)

class MazeGen():
    def __init__(self):
        self.maze = []
        self.n = random.randrange(5, 8)
        self.connections = []
        self.row = 2
        self.col = 0
        self.dim = 20
    
    def empty_maze(self):
        for i in range(0, self.dim):
            self.maze.append([0]*self.dim)
        
    
    def set_start(self):
        self.connections.append([random.randrange(self.dim), 0])
        self.row = self.connections[0][0]
    
    def set_end(self):
        self.connections.append([random.randrange(self.dim), 19])
    
    def new_connection(self):
        for i in range(0, self.n):
            self.connections.append([random.randrange(0,self.dim), random.randrange(0, self.dim-1)])
    
    def connect_points(self):
        self.maze[self.connections[0][0]][0] = 1
        print(self.row, self.col)
        for j in range(0, len(self.connections)):
            # vertical movement
            diff_row = self.connections[j][0] - self.row
            if diff_row <= 0:
                for i in range(0, diff_row*-1):
                    self.row -= 1
                    self.maze[self.row][self.col] = 1
            if diff_row > 0:
                for i in range(0, diff_row):
                    self.row += 1
                    self.maze[self.row][self.col] = 1
                    
            print(self.row, self.col)
            # horizontal movement
            print(j)
            print("test", self.connections[j][1], self.col)
            diff_col = self.connections[j][1] - self.col
            if diff_col < 0:
                for i in range(0, diff_col*-1):
                    self.col -= 1
                    self.maze[self.row][self.col] = 1
            
            if diff_col >=0:
                for i in range(0, diff_col):
                    self.col += 1
                    self.maze[self.row][self.col] = 1
                
            print(self.row, self.col)
            # horizontal movement

    def print_maze(self):
        # use for debugging
        for row in self.maze:
            print(row)

    def get_maze(self):
        return self.maze

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

positionState = obj.get_maze()
for i in range(20):
    for j in range(20):
        if positionState[i][j] == 0:
            colour = DARK_GREEN
        else:
            colour = LIGHT_BLUE
        tile = Tile(i, j, positionState[i][j], colour)
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

player_sprite = pygame.sprite.Group()
player = Player()
player_sprite.add(player)

# Generate and group convo tiles
convoDictionary = convoGen.generate_conversations(obj.get_maze(),screen)
convo_tiles = pygame.sprite.Group()
for x in convoDictionary:
    convo_tiles.add(Tile(x[0],x[1],1,LIGHT_BLUE))

def check_convo_collision():
    collided_convo = pygame.sprite.spritecollideany(player, convo_tiles, collided = None)
    if not collided_convo == None:
        convoObj = (convoDictionary[collided_convo.corner])
        print(collided_convo.corner)
        print(type(convoObj))
        print(convoObj)
        convoObj.conversation_start()

    #redraw the maze    

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
                check_convo_collision()

            if event.key == pygame.K_RIGHT and (pygame.sprite.spritecollideany(player, wall_tiles, collided = None) == None):
                player_sprite.update(10, 0)
                if pygame.sprite.spritecollideany(player, wall_tiles, collided = None) != None:
                    player_sprite.update(-10, 0)
                check_convo_collision()

            if event.key == pygame.K_UP and (pygame.sprite.spritecollideany(player, wall_tiles, collided = None) == None):
                player_sprite.update(0, -10)
                if pygame.sprite.spritecollideany(player, wall_tiles, collided = None) != None:
                    player_sprite.update(0, 10)
                check_convo_collision()

            if event.key == pygame.K_DOWN and (pygame.sprite.spritecollideany(player, wall_tiles, collided = None) == None):
                player_sprite.update(0, 10)
                if pygame.sprite.spritecollideany(player, wall_tiles, collided = None) != None:
                    player_sprite.update(0, -10)
                check_convo_collision()

    # Testing out drawing the wall
    #pygame.draw.rect(display, white, wall.draw_wall())	
    
    pygame.display.update()
    screen.fill(GREY)
    
    wall_tiles.draw(screen)
    walk_tiles.draw(screen)
    
    player_sprite.draw(screen)