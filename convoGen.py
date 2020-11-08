import Conversation
import random

def generate_conversations(maze,screen):
    """generates and asssociates locations of convos as a dictionary. 
    keys are tuples of the location
    returns said dictionary
    all conversation writing should be done here!!"""

    #generating random non-wall locations as tuples
    random.seed()
    convoLocations = []
    for x in range(3):
        while True:
            convoLocation = [random.randint(0,19),random.randint(0,19)]
            if maze[convoLocation[0]][convoLocation[1]] == 1 :
                convoLocations.append(tuple(convoLocation))
                break

    
    # adding each convo object paired with its location as a key
    conversationDic = {}

    """ create a new:

            conversationDic[convoLocations[n]] = Conversation.Base_conversation
            (nPrompt,option1,option2, correctAns, nPositiveResponse, nNegativeResponse,screen)

        for each conversation we want added. ADD ONE TO N EACH TIME, AND MAKE SURE RANGE IN
        LINE 15 IS THE TOTAL NUMBER OF CONVERSATIONS)"""

    #convo 1
    conversationDic[convoLocations[0]] = Conversation.Base_conversation ("nPrompt","option1","option2", "correctAns", "nPositiveResponse", "nNegativeResponse",screen)

    #convo 2
    conversationDic[convoLocations[1]] = Conversation.Base_conversation ("nPrompt","option1","option2", "correctAns", "nPositiveResponse", "nNegativeResponse",screen)

    #convo 3
    conversationDic[convoLocations[2]] = Conversation.Base_conversation ("nPrompt","option1","option2", "correctAns", "nPositiveResponse", "nNegativeResponse",screen)


    return conversationDic

def remove_convo(location,convoDictionary):
    """remove a conversation from the dictionary after it has been used"""
    convoDictionary.pop(location)

def rerandomize_convos(convoDictionary,maze):
    """ randomize convo placement again after having regenerated the maze"""
    random.seed()
    convoLocations = []
    for x in range(len(convoDictionary)):
        while True:
            convoLocation = [random.randint(0,19),random.randint(0,19)]
            if maze[convoLocation[0]][convoLocation[1]] == 0 :
                convoLocations.append(tuple(convoLocation))
                break
    
    """take each convo object from the original convo dictionary and re assign it
    to  a new valid location from convolocations, then return a convo dictionary"""
    locationListIterator = 0
    newConvoDictionary ={}
    for location in convoDictionary:
        newConvoDictionary[convoLocations[locationListIterator]] = convoDictionary[location]
    return newConvoDictionary