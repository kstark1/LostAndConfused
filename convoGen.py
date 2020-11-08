import Conversation
import random

def generate_conversations(maze,screen, prompt, C1, C2, R1, R2, conversationCurrent):
    """generates and asssociates locations of convos as a dictionary. 
    keys are tuples of the location
    returns said dictionary
    all conversation writing should be done here!!"""

    #generating random non-wall locations as tuples
    random.shuffle(maze)
    convoLocations = []

    # adding each convo object paired with its location as a key
    conversationDic = {}

    for x in range(15):
            convoLocation = maze[x]
            convoLocations.append(tuple(convoLocation))
            conversationDic[convoLocations[x]] = Conversation.Base_conversation (prompt[conversationCurrent], C1[conversationCurrent], C2[conversationCurrent], "correctAns", R1[conversationCurrent], R2[conversationCurrent],screen)


    return conversationDic

def remove_convo(location,convoDictionary):
    """remove a conversation from the dictionary after it has been used"""
    convoDictionary.pop(location)

def rerandomize_convos(convoDictionary,maze):
    """ randomize convo placement again after having regenerated the maze"""
    random.shuffle(maze)
    convoLocations = []
    for x in range(15):
            convoLocation = maze[x]
           
            convoLocations.append(tuple(convoLocation))
    
    """take each convo object from the original convo dictionary and re assign it
    to  a new valid location from convolocations, then return a convo dictionary"""
    locationListIterator = 0
    newConvoDictionary ={}
    for location in convoDictionary:
        newConvoDictionary[convoLocations[locationListIterator]] = convoDictionary[location]
    return newConvoDictionary