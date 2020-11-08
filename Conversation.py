import pygame
import time
import sys

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
        self.grey = (250,250,0)

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

        #selection indicator box
        self.indicator = pygame.Rect(self.nRectx+18,
            self.nRecty + self.nRectHeight + 35,
            5, 5)
        self.indicator2 = pygame.Rect(self.nRectx+18,
            self.nRecty + self.nRectHeight + 95,
            5, 5)

    def conversation_start(self):
        """ Start of conversation 
        called on player collision by the player class
        returns nothing"""
    
        # writing the first n prompt and creating boxes
        self.create_dialog_boxes()
        self.write_n_to_screen(self.nPrompt,[self.nRectx+20,self.nRecty+20],self.white)
        time.sleep(1.5)

        response = self.choose_option()
        
        self.check_ans(response)

    def create_dialog_boxes(self):
        #creates base bg boxes
        pygame.draw.rect(self.screen,self.black,self.nRect)
        pygame.draw.rect(self.screen,self.black,self.option1Rect)
        pygame.draw.rect(self.screen,self.black,self.option2Rect)

    def write_n_to_screen(self,text,position,color):
        #erases previous narrator message and replaces it
        pygame.draw.rect(self.screen,self.black,self.nRect)
        pygame.display.update()
        time.sleep(0.5)
    
        # text is less than 64 characters, no line splitting needed
        if len(text) < 64:
            textsurface = self.font.render(text, True,color)
            self.screen.blit(textsurface,tuple(position))
            pygame.display.update()
            return
               
        # text is more than 64 characters, line splitting needed
        end = 0
        for x in range(len(text)):
            if x % 64 == 0 and not x == 0 :
                textsurface = self.font.render(text[end:x+1], True,color)
                end = x+1
                self.screen.blit(textsurface,tuple(position))
                pygame.display.update()
                position[1] += 17
            
    
    def write_option_to_screen(self,text,position,color):
        textsurface = self.font.render(text, True,color)
        self.screen.blit(textsurface,position)
        pygame.display.update()

    def choose_option(self):
    #Initiate control of the options boxes, when enter is pushed exits control
        #default selection:option one, show options and indicator
        response = self.option1
        self.write_option_to_screen(self.option1,(self.nRectx + 30,  self.nRecty + self.nRectHeight + 30),self.white)
        self.write_option_to_screen(self.option2,(self.nRectx + 30,self.nRecty + self.nRectHeight + 90),self.white)
        time.sleep(0.3)
        pygame.draw.rect(self.screen,self.white,self.indicator)
        pygame.display.update()
       
        # allow player to choose btwn options, enter confirms, choice is returned
        exit_ = True
        while exit_:    
            for event in pygame.event.get(): # returns all inputs and triggers into an array
                if event.type == pygame.QUIT: # if the red x was clicked eg buttons in corner of the window
                    sys.exit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        response  = self.option1
                        pygame.draw.rect(self.screen,self.white,self.indicator)
                        pygame.draw.rect(self.screen,self.black,self.indicator2)
                        pygame.display.update()    
                           
                    if event.key == pygame.K_DOWN:
                        response = self.option2
                        pygame.draw.rect(self.screen,self.black,self.indicator)
                        pygame.draw.rect(self.screen,self.white,self.indicator2)
                        pygame.display.update()    

                    #confirm choice
                    if event.key == pygame.K_RETURN:
                        return response

    def check_ans(self,ans):
        if ans == self.correctAns:
            self.write_n_to_screen(self.nPositiveResponse,(self.nRectx+20,self.nRecty+20),self.white)
            time.sleep(2.5)
        else:
            self.write_n_to_screen(self.nNegativeResponse,(self.nRectx+20,self.nRecty+20),self.white)
            time.sleep(2.5)
            self.randomize_maze

    def randomize_maze(self):
        pass
 

class Always_wrong_conversation(Base_conversation):
    #conversation object that will always randomize

    def check_ans():
        self.randomize_maze

        

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600 ))
    screen.fill((255,255,255)) 
    pygame.display.set_caption('Show Text')

    convo = Base_conversation("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl\n"+
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl\n"+
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl\n",
    "option1","option2", "option1", "nPositiveResponse", "nNegativeResponse",screen)
    convo.conversation_start() 

