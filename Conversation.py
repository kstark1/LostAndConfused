import pygame
import time

class Base_conversation ():
    
    def __init__ (self,nPrompt,option1,option2, correctAns, nPositiveResponse, nNegativeResponse,screen):
        #Conversation strings
        self.nPrompt = nPrompt
        self.option1 = option1
        self.option2 = option2
        self.correctAns = correctAns
        self.nPositiveResponse = nPositiveResponse
        self.nNegativeResponse = nNegativeResponse

        #Misc fields
        self.screen = screen
        self.position = (75,600)
        self.width = 60
        self.height = 60
        self.font = pygame.font.Font(None, 50) 
        self.black = (0,0,0)
        self.white = (255,255,255)

        #dialog boxes info
        self.nRectHeight = 125
        self.nRectWidth = 500
        self.nRectx = 150
        self.nRecty = 375
        self.nRect = pygame.Rect(self.nRectx,self.nRecty,self.nRectWidth,self.nRectHeight)
        self.option1Rect = pygame.Rect(self.nRectx,
            self.nRecty + self.nRectHeight + 20,
            240, 100)
        self.option2Rect = pygame.Rect(self.nRectx - ,
             self.nRecty + self.nRectHeight + 20,
             240, 100)

    def conversation_start(self):
        """ Start of conversation 
        called on player collision by the player class
        returns nothing"""
    
        
        #stop_movement()
        self.create_dialog_boxes()
        self.write_n_to_screen(self.nPrompt)

        """throw visual prompt
        

        stop movement
        take response
        check ans
        return movemment"""

    def create_dialog_boxes(self):
        pygame.draw.rect(self.screen,self.black,self.nRect)

    def write_n_to_screen(self,text):
        textsurface = self.font.render(text, True,self.white)
        self.screen.blit(textsurface,self.position)
        pygame.display.update()

        #remove after
        time.sleep(2)
        
   # def write_options_to_screen(self,text):


    """def randomize_player_in_maze(self):

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
            negative response"""

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600 ))
    screen.fill((255,255,255)) 
    pygame.display.set_caption('Show Text')

    convo = Base_conversation("nPrompt","option1","option2", "correctAns", "nPositiveResponse", "nNegativeResponse",screen)
    convo.conversation_start() 

