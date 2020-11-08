import pygame
import random
from mazegen import *
import convoGen
import Conversation
import sys

### Display Variables
TITLE = 'Maze Game' # Title that appears in the window title
FPS = 30 # Frames per second
WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# Colour Variables
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
DARK_GREEN = (28,84,35)
LIGHT_BLUE = (96, 166, 191)
### Create the window

screen = pygame.display.set_mode(SCREENDIM) # creates the main surface where all other assets are place on top
pygame.display.set_caption(TITLE) # updates the window title w/ TITLE
screen.fill(GREY) # Fills the entire surface w/ the colour --> fill = erase/clear
screen_size = screen.get_size()

clock = pygame.time.Clock() # starts a clock obj to measure time

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, state, colour):
        pygame.sprite.Sprite.__init__(self)
        self.state = state #Can change to 1 to test over tile
        self.image = pygame.Surface((40, 30))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.center = (((x * 40) + 20), ((y * 30) + 15))
        self.corner = (x, y)


class Player(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (20, ((x * 30) + 15))

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def get_grid_pos(self):
        return [self.rect.y//30, self.rect.x//40]

    def get_pos(self):
        return [self.rect.x, self.rect.y]

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height


obj = MazeGen()
obj.empty_maze()
obj.set_start()
obj.new_connection()
obj.set_end()
obj.connect_points()


obj.set_dead_connects()
obj.dead_end_points()


wall_tiles = pygame.sprite.Group()
walk_tiles = pygame.sprite.Group()

positionState = obj.get_maze()
walkableTiles = []

for i in range(20):
    for j in range(20):
        if positionState[i][j] == 0:
            colour = DARK_GREEN
        else:
            colour = LIGHT_BLUE
            walkableTiles.append([j, i])
        tile = Tile(j, i, positionState[i][j], colour)
        if tile.state == 0:
            wall_tiles.add(tile)
        else:
            walk_tiles.add(tile)

startingX = obj.connections[0][0] 
player_sprite = pygame.sprite.Group()
player = Player(startingX)
player_sprite.add(player)

nprompts = []
nprompts.append("OH, well hello there. Pretty fine day, huh? Pretty fine maze?")
nprompts.append("HUH, look at that! It's almost like there's some_contingency plan to donk up fools like you who_think this place is simple. Wild days. ")
nprompts.append("Oh boy, you're still stuck in this *super* simple maze,_huh? It's almost like, I don't know, you've been asked to do some_sort of complex task that doesn't just happen in the blink of an eye._Sometimes you've got to spend like, 24 hours on this kind of thing._It's hard business.")
nprompts.append("from the Ether: Still here, loser? ")
nprompts.append("AHAHAHAHA, I TOTALLY GO YOU, YOU FOOL, YOU WAD.")
# template nprompts.append("")

choices1 = []
choices1.append("I mean, sure, yeah, it's a pretty fine maze, a bit simple maybe.")
choices1.append("It uh, still looks pretty easy, though.")
choices1.append("I'm only struggling because I've gotten little to no sleep.")
choices1.append("You're pretty blatantly unkind, you know that?")
choices1.append("Please make this hackathon stop. I mean... maze? What the...")
# template choices1.append("")

  
choices2 = []
choices2.append("THIS MAZE IS TRANCH, MAN.")
choices2.append("What the- let me out of here you dillweed!")
choices2.append("You're hard business.")
choices2.append("Shut the fu-")
choices2.append("Why aren't you a physical entity I can punch?")
# template choices2.append("")
 
correctAns = []
correctAns.append("I mean, sure, yeah, it's a pretty fine maze, a bit simple maybe.")
correctAns.append("It uh, still looks pretty easy, though.")
correctAns.append("I'm only struggling because I've gotten little to no sleep.")
correctAns.append("You're pretty blatantly unkind, you know that?")
correctAns.append("Please make this hackathon stop. I mean... maze? What the...")
# template correctAns.append("")

npos = []
npos.append(" Huh... that's... pretty bold of you, dog, to suggest_that this is a simple space. You know people have to like,_carve this junk out, right? Well, whatever, you should be out in a jiffy,_then. If it's so simple.")
npos.append("Thank goodness it probably only switches_things up on you once then, huh?")
npos.append("You and everyone else in this Ether, fool.")
npos.append("Right back at you my dude. You know what, get out of here,_this is as lame as the day you were born.")
npos.append(" My days, what sort of whacked out_astral plane are you on right now?_Alright dog, get out of here for real time. Get some sleep.")
# template npos.append("")

nneg = []
nneg.append("... Well you're about to get it right in the_exactly where it's coming to you, friend. ")
nneg.append("IT'S A SIMPLE MAZE, GET YOURSELF OUT, DILLWEED.")
nneg.append("NO YOU'RE HARD BUSINESS. ")
nneg.append("Right back at you my dude. You know what, get out of here,_this is as lame as the day you were born. ")
nneg.append(" Yeah, they didn't have time for that. Okay, okay, you can_actually go now. Even I'm bored.")
# template nneg.append("")

#Text lists
prompt = nprompts
C1 = choices1
C2 = choices2
R1 = npos
R2 = nneg
conversationCurrent = 0

# Generate and group convo tiles
if conversationCurrent < 5:
    convoDictionary = convoGen.generate_conversations(walkableTiles,screen, prompt, C1, C2, R1, R2, conversationCurrent)
    convo_tiles = pygame.sprite.Group()
    for x in convoDictionary:
        convo_tiles.add(Tile(x[0],x[1],1,LIGHT_BLUE))

used_convos = []
def check_convo_collision():
    collided_convo = pygame.sprite.spritecollideany(player, convo_tiles, collided = None)
    if not collided_convo == None and not collided_convo.corner in used_convos:
        convoObj = (convoDictionary[collided_convo.corner])
        regen =  convoObj.conversation_start()
        if regen == True:
            #used_convos.append(collided_convo.corner)
            #convoGenEdenCopy.remove_convo(collided_convo.corner,convoDictionary)
            return True
            
    return False

endpoint = obj.get_endpoint()
running = True
regen = False

while running:
    p_pos = player.get_pos()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and (pygame.sprite.spritecollideany(player, wall_tiles, collided = None) == None)and p_pos[0] > 39:
                player_sprite.update(-40, 0)
                if pygame.sprite.spritecollideany(player, wall_tiles, collided = None) != None:
                    player_sprite.update(40, 0)
                regen = check_convo_collision()
                if conversationCurrent == 4 and pygame.sprite.spritecollideany(player, convo_tiles, collided = None) != None:
                    convo_tiles.empty()

            if event.key == pygame.K_RIGHT and (pygame.sprite.spritecollideany(player, wall_tiles, collided = None) == None)and p_pos[0] <= screen_size[0] - player.get_width() - 39:
                player_sprite.update(40, 0)
                if pygame.sprite.spritecollideany(player, wall_tiles, collided = None) != None:
                    player_sprite.update(-40, 0)
                regen =check_convo_collision()
                if conversationCurrent == 4 and pygame.sprite.spritecollideany(player, convo_tiles, collided = None) != None:
                    convo_tiles.empty()

            if event.key == pygame.K_UP and (pygame.sprite.spritecollideany(player, wall_tiles, collided = None) == None)and p_pos[1] > 29:
                player_sprite.update(0, -30)
                if pygame.sprite.spritecollideany(player, wall_tiles, collided = None) != None:
                    player_sprite.update(0, 30)
                regen = check_convo_collision()
                if conversationCurrent == 4 and pygame.sprite.spritecollideany(player, convo_tiles, collided = None) != None:
                    convo_tiles.empty()

            if event.key == pygame.K_DOWN and (pygame.sprite.spritecollideany(player, wall_tiles, collided = None) == None)and p_pos[1] <= screen_size[1] - player.get_height() - 29:
                player_sprite.update(0, 30)
                if pygame.sprite.spritecollideany(player, wall_tiles, collided = None) != None:
                    player_sprite.update(0, -30)
                regen = check_convo_collision()
                if conversationCurrent == 4 and pygame.sprite.spritecollideany(player, convo_tiles, collided = None) != None:
                    convo_tiles.empty()

            endpoint = obj.get_endpoint()
            if player.get_grid_pos() == endpoint:
                winConvo = Conversation.Base_conversation("Finally leaving huh...","Absolutely","Yes", "None", "None","Nice knowing you, fool..._(thank the stars, this maze really is too small_for the two of us)." ,screen)
                winConvo.conversation_start()
                sys.exit()

        
        if regen == True and (conversationCurrent < 4):
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
            walkableTiles = []

            for i in range(20):
                for j in range(20):
                    if positionState[i][j] == 0:
                        colour = DARK_GREEN
                    else:
                        colour = LIGHT_BLUE
                        walkableTiles.append([j, i])
                    tile = Tile(j, i, positionState[i][j], colour)
                    if tile.state == 0:
                        wall_tiles.add(tile)
                    else:
                        walk_tiles.add(tile)  
            conversationCurrent += 1
            convoDictionary = convoGen.generate_conversations(walkableTiles, screen, prompt, C1, C2, R1, R2, conversationCurrent)
            convo_tiles = pygame.sprite.Group()
            for x in convoDictionary:
                convo_tiles.add(Tile(x[0],x[1],1,LIGHT_BLUE))
            regen = False
        


            


    pygame.display.update()
    screen.fill(GREY)
    
    wall_tiles.draw(screen)
    walk_tiles.draw(screen)
    
    convo_tiles.draw(screen)
    player_sprite.draw(screen)