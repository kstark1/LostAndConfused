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
        self.font = pygame.font.Font(None, 20) 
        self.black = (0,0,0)
        self.white = (255,255,255)

        #dialog boxes info
        self.nRectHeight = 125
        self.nRectWidth = 500
        self.nRectx = 150
        self.nRecty = 300
        self.nRect = pygame.Rect(self.nRectx,self.nRecty,self.nRectWidth,self.nRectHeight)
        self.option1Rect = pygame.Rect(self.nRectx,
            self.nRecty + self.nRectHeight + 20,
            self.nRectWidth, 40)
        self.option2Rect = pygame.Rect(self.nRectx,
            self.nRecty + self.nRectHeight + 80,
            self.nRectWidth, 40)

    def conversation_start(self):
        """ Start of conversation 
        called on player collision by the player class
        returns nothing"""
    
        
        #stop_movement()

        # writing the first n prompt and creating boxes
        self.create_dialog_boxes()
        self.write_n_to_screen(self.nPrompt,(self.nRectx+20,self.nRecty+20),self.white)
        time.sleep(2)

        self.choose_option()
        

        
        """
        stop movement
        take response
        check ans
        return movemment"""

    def create_dialog_boxes(self):
        pygame.draw.rect(self.screen,self.black,self.nRect)
        pygame.draw.rect(self.screen,self.black,self.option1Rect)
        pygame.draw.rect(self.screen,self.black,self.option2Rect)

    def write_n_to_screen(self,text,position,color):
        textsurface = self.font.render(text, True,color)
        self.screen.blit(textsurface,position)
        pygame.display.update()

    def choose_option(self):
    #Initiate control of the options boxes, when enter is pushed exits control
        #default selection:option one
        self.ans  = self.option1
        pygame.draw.rect(self.screen,self.white,self.option1Rect)
        self.write_n_to_screen(self.option1,(self.nRectx + 20,  self.nRecty + self.nRectHeight + 30),self.black)
        self.write_n_to_screen(self.option2,(self.nRectx + 20,self.nRecty + self.nRectHeight + 90),self.white)
        
        exit_ = True
        while exit_:    
            for event in pygame.event.get(): # returns all inputs and triggers into an array
                if event.type == pygame.QUIT: # if the red x was clicked eg buttons in corner of the window
                    exit_ = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        self.ans  = self.option1
                        pygame.draw.rect(self.screen,self.white,self.option1Rect)
                        pygame.draw.rect(self.screen,self.black,self.option2Rect)
                        self.write_n_to_screen(self.option1,(self.nRectx + 20,  self.nRecty + self.nRectHeight + 30),self.black)
                        self.write_n_to_screen(self.option2,(self.nRectx + 20,self.nRecty + self.nRectHeight + 90),self.white)
                        pygame.display.update()


                    if event.key == pygame.K_DOWN:
                        self.ans  = self.option2
                        pygame.draw.rect(self.screen,self.black,self.option1Rect)
                        pygame.draw.rect(self.screen,self.white,self.option2Rect)
                        self.write_n_to_screen(self.option1,(self.nRectx + 20,  self.nRecty + self.nRectHeight + 30),self.white)
                        self.write_n_to_screen(self.option2,(self.nRectx + 20,self.nRecty + self.nRectHeight + 90),self.black)
                        pygame.display.update()

                    #confirm choice
                    if event.key == pygame.K_RETURN:
                        exit_ = False
                        

  


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

    convo = Base_conversation("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl",
    "option1","option2", "correctAns", "nPositiveResponse", "nNegativeResponse",screen)
    convo.conversation_start() 

