'''
Exercise 6: Text Adventure - Who Killed Coli???

Premise: For this assignment we'll be making a simple text-adventure game where you play as a detective summoned to a
mansion in the countryside to determine who killed Coli. When starting the game, the player is met with a brief
synopsis of who The detective is and why you're there. You can travel from room to room, talk to NPC's and
search for clues. Once they determine who the murderer is, they must return to the living room and announce
the name of the killer. This ends the game and shows text to the player indicating if their guess was correct,
saying what happens to the killer, and closing out the game. Finally, gameplay stats will be shown to the player.

Code Design: Every Room is a Function
There are multiple ways to represent discreet locations in games, and this assignment is not gonna use any of the
"good" ones. Instead, we'll be using what you've already learned and pushing it to its limits.
To that end, every room in the game will be represented by its own function. That room function will declare
what rooms you can go to, and what options are available to you in that room. To help you, I've included a
function you can use

'''

def move_room(funcName):
    globals()[funcName]()


def take_object (objects, location, inventory):
    print (f"In this {location}, you find a {objects}")
    take_affirm = input("Would you like to add one of these objects to your inventory?   YES   NO\n").lower()
    if take_affirm == "yes":
        object_take = input(f"Which object will you take? {objects}\n").lower()
        if object_take in objects:
            inventory.append(object_take)
            objects.remove(object_take)
            print(f"In your pockets, you now have {inventory}")
        else:
            print(f"What was that? Your choices are {objects}")

    if take_affirm == "no":
        print("You return to solving the crime.")

def check_stats(inventory, visited_rooms, npcs_spoken, notes_taken):
    print("You take some time to collect your thoughts, review what you know.")
    check = input("Check   INVENTORY   ROOMS   NPCS   NOTES\n or you can    GO BACK\n").lower()
    
    if check != "go back":
        if check == "inventory":
          print(f"In your pockets, you now have {inventory}")
          check_stats(inventory, visited_rooms, npcs_spoken, notes_taken)
        if check == "npcs":
            print(f"So far, you have spoken to {npcs_spoken}")
            check_stats(inventory, visited_rooms, npcs_spoken, notes_taken)
    if check == "go back":
        livingroom(inventory, visited_rooms, npcs_spoken, notes_taken)

def livingroom(inventory, visited_rooms, npcs_spoken, notes_taken):
    print("LivingRoom paragraph")
    action = input("What would you like to do?\n TALK  LOOK  MOVE  NOTES\n").lower()
    if action != "move":
        if action == "talk":
            print("Ofelia Dialogue")
            npc_LR = "Ofelia"
            if npc_LR not in npcs_spoken:
                npcs_spoken.append(npc_LR)
            livingroom(inventory, visited_rooms, npcs_spoken, notes_taken)

        if action == "look":
            print("In this living room, you see a body on the floor, someone standing over them, a desk, a coffee table, and a cabinet.")
            look_choice = input("What would you like to look at first? \n BODY   PERSON   DESK   TABLE   CABINET\n").lower()
            if look_choice == "cabinet":
                location = "cabinet"
                cab_contents = ["pen", "paper", "pencil", "stapler", "tape"]
                take_object(cab_contents, location, inventory)

            livingroom(inventory, visited_rooms, npcs_spoken, notes_taken)


        if action == "notes":
            check_stats(inventory, visited_rooms, npcs_spoken, notes_taken) 


    if action == "move":
        print("Move Options")


def start_mystery(inventory, visited_rooms, npcs_spoken, notes_taken):
    print("Starting Paragraph")
    livingroom(inventory, visited_rooms, npcs_spoken, notes_taken)

inventory  = []
visited_rooms = []
npcs_spoken = []
notes_taken = []

start_mystery(inventory, visited_rooms, npcs_spoken, notes_taken)
#actions you can take: Look, Talk, Take, Use
#Rooms: Living room, bedroom, bathroom, kitchen, dining room, patio
#NPCs: Chloe, Ofelia, Trout, Xavier, Julia