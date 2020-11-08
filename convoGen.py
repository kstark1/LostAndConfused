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
    for x in range(5):   # Fix me before end
        while True:
            convoLocation = [random.randint(0,19),random.randint(0,19)]
            if maze[convoLocation[0]][convoLocation[1]] == 1 :
                convoLocations.append(tuple(convoLocation))
                break

    
    # adding each convo object paired with its location as a key
    conversationDic = {}

    """ create a new:

            conversationDic[convoLocations[n]] = Conversation.Base_conversation
            ("nPrompt","option1","option2", "correctAns", "nPositiveResponse", "nNegativeResponse",screen)

        for each conversation we want added. ADD ONE TO N EACH TIME, AND MAKE SURE RANGE IN
        LINE 15 IS THE TOTAL NUMBER OF CONVERSATIONS)"""

    #convo 1
    conversationDic[convoLocations[0]] = Conversation.Base_conversation ("OH, well hello there. Pretty fine day, huh? Pretty fine maze?","I mean, sure, yeah, it's a pretty fine maze, a bit simple maybe.","THIS MAZE IS TRANCH, MAN.", "I mean, sure, yeah, it's a pretty fine maze, a bit simple maybe.", "Huh... that's... pretty bold of you, dog, to suggest_that this is a simple space. You know people have to like,_carve this junk out, right? Well, whatever, you should be out in a jiffy,_then. If it's so simple.", "... Well you're about to get it right in the_exactly where it's coming to you, friend.",screen)

    #convo 2
    conversationDic[convoLocations[1]] = Conversation.Base_conversation ("HUH, look at that! It's almost like there's some_contingency plan to donk up fools like you who_think this place is simple. Wild days.","It uh, still looks pretty easy, though.","What the- let me out of here you dillweed!", "It uh, still looks pretty easy, though.", "Thank goodness it probably only switches_things up on you once then, huh?", "IT'S A SIMPLE MAZE, GET YOURSELF OUT, DILLWEED",screen)

    #convo 3
    conversationDic[convoLocations[2]] = Conversation.Base_conversation ("Oh boy, you're still stuck in this *super* simple maze,_huh? It's almost like, I don't know, you've been asked to do some_sort of complex task that doesn't just happen in the blink of an eye._Sometimes you've got to spend like, 24 hours on this kind of thing._It's hard business.","I'm only struggling because I've gotten little to no sleep.","You're hard business.", "I'm only struggling because I've gotten little to no sleep.", "You and everyone else in this Ether, fool.", "NO YOU'RE HARD BUSINESS.",screen)

    #convo 4
    conversationDic[convoLocations[3]] = Conversation.Always_wrong_conversation ("Still here, loser?","You're pretty blatantly unkind, you know that?","Shut the fu-", "correctAns", "Right back at you my dude. You know what, get out of here,_this is as lame as the day you were born.", "Right back at you my dude. You know what, get out of here,_this is as lame as the day you were born.",screen)

    #convo 5 
    conversationDic[convoLocations[4]] = Conversation.Base_conversation  (" AHAHAHAHA, I TOTALLY GO YOU, YOU FOOL, YOU WAD.","Please make this hackathon stop. I mean... maze? What the...","Why aren't you a physical entity I can punch? ", "Please make this hackathon stop. I mean... maze? What the...", "My days, what sort of whacked out_astral plane are you on right now?_Alright dog, get out of here for real time. Get some sleep.", "Voice from the Ether: Yeah, they didn't have time for that. Okay, okay, you can actually go now. Even I'm bored.",screen)



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