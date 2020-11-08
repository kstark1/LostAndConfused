import pygame
import time

class Base_conversation ():
    
    __init__(self,position,nPrompt,option1,option2, correctAns, nPositiveResponse, nNegativeResponse):
        self.position = position
        self.nPrompt
        self.option1
        self.option2
        self.correctAns
        self.nPositiveResponse
        self.nNegativeResponse
        self.width =
        self.height = 
        self.font = pygame.font.Font(None, 50) 
        self.black = (0,0,0)
        self.white = (255,255,255)

    def conversation_start(self):
        """ called on player collision by the player class"""

        stop_movement()

        throw visual prompt
        

        stop movement
        take response
        check ans
        return movemment

    def write_to_screen(self,text):
        textrender = self.font.render(nPrompt, True,self.white)
        textRect = textrender.get_rect()
        textRect.center = ()

    def randomize_player_in_maze(self):

    def check_ans(ans):
        if ans = self.correctAns
            positive response
        else:
            random 
            negative response

    def stop_movement(self):
        call method from movement handling class

    def start_movement(self):
        call method from movement handling class

class Always_wrong_conversation(Base_conversation):
    #conversation that will always randomize

     def check_ans():
        if response = correct
            notrandom
            positive response
        else:
            random 
            negative response

if __name__ = "__main__":
    pygame.init()
    display_surface = pygame.display.set_mode((800, 800 ))
    pygame.display.set_caption('Show Text')

    convo = Base_conversation()
    convo.conversation_start() 