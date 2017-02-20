from NonPlayerCharacter import *

def make_characters():
    """Make a list of NonPlayerCharacters the user can interact with to test functionality."""

    #list characters

    characters = []
    characters.append(Shopkeeper("Fred", "humble shopkeeper", "How can I serve you?",\
                      ["Just doeth it!", "Low prices be just the beginning.", \
                       "Obey thine thirst.", "Think outside the loaf.", "What wouldst thou do for a potion of healing?"],\
                      [Item("bag of holding", 20), Item("mask of deceiving", 30),\
                       Item("vial of sleeping potion", 10)]))
    characters.append(Shopkeeper("Matilda", "poor alchemist", "In vino veritas.",\
                      ["Infinitus est numerus stultorum.", "Inopiae desunt multa, avaritiae omnia.", \
                       "De omnibus dubitandum.", "Docendo disco, scribendo cogito.",\
                       "Sapientia melior auro.", "Fred is a crook."],\
                      [Item("water of sleeping", 20), Item("water of honesty", 30),\
                       Item("water of healing", 40)]))
  
    return characters

def main():
    """Display NPC's to user, have user select a character and interact."""

    #list characters
    #NonPlayerCharacter npc
    #bool done, talking
    #list commands
    #str choice
    #int npc_index, count

    characters = make_characters()

    done = False

    while not done:

        # List all characters
        print("\nMeet our cast of characters...")
        count = 1
        for npc in characters:
            print(str(count)+". ", end = "")
            npc.greet()
            count += 1

        # Have the user select a character to interact with
        npc_index = -1
        while npc_index <0 or npc_index > len(characters):
            npc_index = int(input("\nType the number of the character you'd like to talk to, 0 to quit: "))
        if npc_index != 0:
            npc = characters[npc_index-1]

            talking = True
            while talking:
                # Get commands from the character and display to the user
                commands = npc.get_commands()
                print("\nI can do the following:")
                for command in commands:
                    print("\t" + command)
                print("\tleave")
                choice = input("Please enter your choice: ")

                # Have the user choose a command and npc executes command
                if choice.upper() == "LEAVE":
                    talking = False
                elif choice in commands:
                    print("")
                    npc.follow_command(choice)
                else:
                    print("I didn't understand that.")
        else:
            done = True

main()
    
