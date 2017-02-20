"""
    Kenneth Perry
    Location creates a list and uses this information to prompt the user and get
    command from the user in return
"""
import sys
from location import *
from NonPlayerCharacter import *

def make_characters():
    """Make a list of NonPlayerCharacters the user can interact with to test functionality."""

    #list characters

    characters = []
    characters.append(Shopkeeper("Fred", "humble shopkeeper", "How can I serve you?",\
                      ["Just doeth it!", "Low prices be just the beginning.", \
                       "Obey thine thirst.", "Think outside the loaf.", "What wouldst thou do for a potion of healing?"],\
                        "book seller's",\
                      [Item("bag of holding", 20), Item("mask of deceiving", 30),\
                       Item("vial of sleeping potion", 10)]))
    characters.append(Shopkeeper("Matilda", "poor alchemist", "In vino veritas.",\
                      ["Infinitus est numerus stultorum.", "Inopiae desunt multa, avaritiae omnia.", \
                       "De omnibus dubitandum.", "Docendo disco, scribendo cogito.",\
                       "Sapientia melior auro.", "Fred is a crook."],\
                        "town gate",\
                      [Item("water of sleeping", 20), Item("water of honesty", 30),\
                       Item("water of healing", 40)]))
  
    return characters

def instructions():
    print ("To play, type one of the following commands.")
    print ("N to move north.")
    print ("E to move east.")
    print ("S to move south.")
    print ("W to move west.")
    print ("T to talk to a character.")
    print ("Q to quit")
    print ("I to see these instructions again.\n")
    
def make_locs():
    """ hard-code a list of locations."""

    # list locations

    locations = []
    locations.append(make_locations("town gate",\
                                    "It is open during the day,\nbut you had to pay with your last gold piece to get in.",\
                                    "Ahead of you to the (N)orth is the town square, bright and bustling.\nTo the (E)ast is an alley running between the town wall and a shop.\nTo the (W)est is a similar alley between the wall and a shipyard.\n",\
                                    ["town square", "outside", "book seller's", "shipyard"]))

    locations.append(make_locations("town square",\
                                    "You step into the town square, and find there's little room to move. People bustle busily about.",\
                                    "To the (E)ast is a shipyard with much activity.\nTo the (S)outh is the town gate.\nTo the (W)est is a book seller's shop.\n",\
                                    ["court house", "book seller's", "shipyard", "town gate"]))
    locations.append(make_locations("book seller's",\
                                    "It takes your eyes a moment to adjust to the dim light in the shop.",\
                                    "Inside it is quiet and smells of mold.\nYou could spend decades simply reading all the titles in this shop,\nwhich has books in stacks and shelves from floor to ceiling.\nTo the (W)est is the exit to the town square.\n",\
                                    ["", "", "", "town square"]))
    locations.append(make_locations("shipyard",\
                                    "As you move forward you see a fleet of ships riddled with battlescars.",\
                                    "This is seems like a dead end.\nAs you move forward you hear something creeping forward.\nTo the (E)ast you can run back to town square\n",\
                                    ["", "", "town square", ""]))
    locations.append(make_locations("court house",\
                                    "When you walk up you see a huge building with hugedoors.",\
                                    "The door is locked. You can go (S)outh to head back to town square\n",\
                                    ["", "town square", "", ""]))
    locations.append(make_locations("outside",\
                                    "You walk past the gate and noticed that there's a boulder blocking your way.",\
                                    "You can not move forward head (N)orth back through the gate.\n",\
                                    ["town gate", "", "", ""]))

    return locations

def main():
    """This is the beginning of the game"""
    print ("Welcome to the old town!\n")
    instructions()
    
    print ("This is the town gate. It is open during the day,")
    print ("but you had to pay with your last gold piece to get in.")
    print ("To the (E)ast is an alley running between the town wall and a shop.")
    print ("To the (W)est is a similar alley between the wall and a shipyard.\n")

    choice = ""
    loc = make_locs()
    characters = make_characters()
    
    while (choice != "Q"):       
        choice = str(input("What is your command? "))
        while (choice != "N" and choice != "W" and choice != "E" and choice != "S" and choice != "Q" and choice != "I"):
            print ("I didn't understand that.")
            choice = str(input("What is your command? "))
            
        name = get_name(loc)
        room = get_loc_name(loc, choice)
        greet = get_location(loc)
        #npc_greet = greet()
        
        description = get_description(loc, room)
        direction = get_directions(loc, room)
        
        if room == "town gate":
            print ("This is the " + room + ".")#N
            print (description, direction)
        if room == "town square":
            print ("This is the " + room + ".")#S
            print (description, direction)
        if room == "book seller's":
            print ("This is the " + room + ".")#E
            print (description, direction)
        if room == "shipyard":
            print ("This is the " + room + ".")#W
            print (description, direction)
        if room == "court house":
            print ("This is the " + room + ".")#wtf
            print (description, direction)
        if room == "outside":
            print ("This is the " + room + ".")#wtf
            print (description, direction)
        if (choice == "I"):
            instructions()
            
        if (choice == "Q"):
            print ("Thank you for playing! Please come again!")
            sys.exit
        

main()
    
    
