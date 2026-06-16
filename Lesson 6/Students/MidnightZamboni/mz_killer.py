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
import time
import colorama
from colorama import Fore, Style

def move_room(funcName):
    globals()[funcName]()

def isLocked (door, key, inventory, used_inventory):
    unlocked = False
    if key in inventory:
        inventory.remove(key)
        used_inventory.append(key)
        unlocked = True
        print(f"{Fore.GREEN}You have unlocked {door} with {key}.{Style.RESET_ALL}")
    '''
    if not unlocked:
        f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}"

'''

def Ofelia_dialogue(choice, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker):
    while choice != "back":
        if choice == "who":
            input("'Who are you? What's your beef with  the deceased?'")
            input(f"{Fore.LIGHTBLACK_EX}I'm Ofelia, and I've got no 'beef' with Coli! I'm just a student, ok? I'm just here to learn some code, get better at game jams{Style.RESET_ALL}")
            input("'Alright then. Sure...'")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()
            if "ofeliaWho" not in npc_tracker:
                npc_tracker.append("ofeliaWho")
        if choice == "what":
            input("'What the hell happened here?'")
            input(f"{Fore.LIGHTBLACK_EX}We were working on our Computer Science finals when all of the sudden Coli starts coughing and sneezing all over the place.{Style.RESET_ALL}")
            input("'Ugh. Gross.'")
            input(f"{Fore.LIGHTBLACK_EX}Right? Well, she said she felt super sick, and before we knew it, she was on the floor. DEAD! Like, what the fuck?{Style.RESET_ALL}")
            input("'Watch the language, kid.'")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()
            if "ofeliaWhat" not in npc_tracker:
                npc_tracker.append("ofeliaWhat")
        if choice == "when":
            input("'When did this all go down?'")
            input(f"{Fore.LIGHTBLACK_EX}I dunno, like... 30-ish minutes ago???{Style.RESET_ALL}")
            input("'Love the accuracy, kid, thanks.'")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()
            if "ofeliaWhen" not in npc_tracker:
                npc_tracker.append("ofeliaWhen")
        if choice == "where":
            input("'Just you in here? Where's the rest of the coding crew?'")
            input(f"{Fore.LIGHTBLACK_EX}Once the cops showed up, we spread out through the house. We're all pretty shaken. Trout's in the bedroom, Chloe's on the patio, Julia's in the dining room, and Xavier's in the kitchen.{Style.RESET_ALL}")
            input("'Sure, sure. I'll make sure to check in on them, too.'")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()
            if "ofeliaWhere" not in npc_tracker:
                npc_tracker.append("ofeliaWhere")
        if choice == "why":
            input("'So, what do you think, huh? Why would someone do this?'")
            input(f"{Fore.LIGHTBLACK_EX}I've got no clue, and how could I?! We just wanted to make games, ok? Coli was in on it! I mean, sure, we made jokes, but she was part of the team, our FRIEND!{Style.RESET_ALL}")
            input(("'Whoa, 'jokes'? Whaddya mean 'jokes'?'"))
            input(f"{Fore.LIGHTBLACK_EX}Like... Trout made a 'Blow Up Coli' function, just for fun when she was giving out assignments he didn't want to do. It was funny! Harmless...{Style.RESET_ALL}")
            input("'Harmles, right...' I nudge Coli's body with my foot. Harmless indeed.")
            if "ofeliaWhy" not in npc_tracker:
                npc_tracker.append("ofeliaWhy")
            if "Trout made jokes about blowing Coli up when she gave him an assignment." not in notes_taken:
                print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                notes_taken.append("Trout made jokes about blowing Coli up when she gave him an assignment.")

            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()

        if choice == "back":
            input("'Thanks, Ofelia. Don't go anywhere, I might check back with you later.'")
            livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)
        else:
            print("English, Einstein! I didn't understand ya!")
            choice= input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()

def Trout_dialogue(choice, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker):
    while choice != "back":
        if choice == "who":
            input("'Tell me, Trout. Who was in the room to actually witness the murder?'")
            input(f"{Fore.LIGHTBLACK_EX}Well, I saw Coli go down after she got up from her desk. Ofelia was quick to her feet, though. She was the first to see what was wrong. \nXavier got on the phone with 911 as soon as he could. And Chloe went outside. Said something about feeling faint.{Style.RESET_ALL}")
            input("'That's all well and good, kid, but your math ain't addin' up. You only accounted for five coders, where's the sixth?'")
            input(f"{Fore.LIGHTBLACK_EX}Oh yeah, Julia. She was in the bathroom at the time, came out just before the police came.{Style.RESET_ALL}")

            if "Julia was in the bathroom when Coli met her untimely demise." not in notes_taken:
                print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                notes_taken.append("Julia was in the bathroom when Coli met her untimely demise.")
            if "Chloe left the room when Coli hit the ground." not in notes_taken:
                notes_taken.append("Chloe left the room when Coli hit the ground.")

            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHEN   WHY   BACK\n{Style.RESET_ALL}").lower()
            if "troutWho" not in npc_tracker:
                npc_tracker.append("troutWho")

        if choice == "when":
            input("'When did you guys get here? I mean, how long have you been staying here?'")
            input(f"{Fore.LIGHTBLACK_EX}Two days ago. We've just been hanging out, only got to the final tonight.{Style.RESET_ALL}")
            input("'Anything happen while you kids were just 'hanging out'?'")
            input(f"{Fore.LIGHTBLACK_EX}Not that I can think of... We had a great time, no problems.{Style.RESET_ALL}") 
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHEN   WHY   BACK\n{Style.RESET_ALL}").lower()
            if "troutWhen" not in npc_tracker:
                npc_tracker.append("troutWhen")

        if choice == "why":
            if "ofeliaWhy" in npc_tracker:
                input("'Alright, I'll be outta your hair in a second. Just one more question.'")
                input("'Why did you write a 'Blow Up Coli' function into your code?'")
                input("At this, Trout jumps to his feet, defensive, paler than a terminal in light mode.")
                input(f"{Fore.LIGHTBLACK_EX}C'mon, man, you can't be serious! That was a joke! It has nothing to do with this!{Style.RESET_ALL}")
                input(("'The way I see it, it could have everything to do with this.'"))
                input("He sits back down, head in his hands.")
                input(f"{Fore.LIGHTBLACK_EX}During the first ever lecture Xavier hosted, Coli was there. Xavier was teaching, but she jumped in to try and explain something we weren't really understanding. \nShe appointed herself TA, and then she told us to try and write functions for the first time on our own. Just to be funny, as a little protest, I named my function 'Blow Up Coli'.{Style.RESET_ALL}")
                input("'I see.'")
                input(f"{Fore.LIGHTBLACK_EX}I swear to God that's all it was! I mean, she's out there in one piece, isn't she?! No one really blew her up!{Style.RESET_ALL}")
                input("'Calm down, kid. I'm trying to get a firm shake on the whole thing. I don't know enough to start making accusations... yet.'")
                if "ofeliaWhy" not in npc_tracker:
                    npc_tracker.append("ofeliaWhy")
                if "Trout made jokes about blowing Coli up when she gave him an assignment." not in notes_taken:
                    print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                    notes_taken.append("Trout made jokes about blowing Coli up when she gave him an assignment.")

                choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()
            else:
                input("Don't think I have enough info to ask this question, yet. I oughtta keep looking around, come back later.")
                choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()

        if choice == "back":
            input("'Well, I'm gonna get on with it. Be careful out there, Trout. You don't wanna be the next one swimming with the fishes.'")
            bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)
        else:
            print("English, Einstein! I didn't understand ya!")
            choice= input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()


def take_object (objects, location, inventory):
    input (f"Ah, theres some stuff in this {location}. Looks like a\n {objects}")
    take_affirm = input(f"{Fore.BLUE}Would you like to add one of these objects to your inventory?   YES   NO\n{Style.RESET_ALL}").lower()
    if take_affirm == "yes":
        object_take = input(f"{Fore.BLUE}Which object will you take? {objects}\n{Style.RESET_ALL}").lower()
        if object_take in objects:
            inventory.append(object_take)
            objects.remove(object_take)
            input(f"Could be helpful, I think I'll put this {object_take} in my pocket.")
            print(f"{Fore.GREEN} You have added {object_take} to your inventory.{Style.RESET_ALL}")
            take_affirm = input(f"{Fore.BLUE}Would you like to add one of these objects to your inventory?   YES   NO\n{Style.RESET_ALL}").lower()

    if take_affirm == "no":
        input("Back to the matter at hand.")


def check_stats(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker):
    check = input(f"{Fore.BLUE}Check   INVENTORY   ROOMS   NPCS   NOTES   BACK\n{Style.RESET_ALL}").lower()
    
    if check != "go back":
        if check == "inventory":
          print(f"In my pockets, I've got a {inventory}")
          check_stats(inventory, visited_rooms, npcs_spoken, notes_taken)
        if check == "npcs":
            print(f"So far, I've talked to {npcs_spoken}")
            check_stats(inventory, visited_rooms, npcs_spoken, notes_taken)
        if check == "notes":
            print(f"Let's see what I jotted down so far...")
            for i in range(len(notes_taken)):
                print("-" + notes_taken[i])

    if check == "go back":
        livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)

def livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker):
    input(f"\n{Fore.RED} THE LIVING ROOM {Style.RESET_ALL}")
    input("It's a small room, unassuming. Signs of nerds doing computer things everywhere. Noisy from all the laptop fans running nonstop. A coffee table, a cabinet, and a desk fill the bulk of the space. \nTwo bodies: one upright, breathing. The other, not so much.")
    input("Time to make my move.")
    action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()
    if action != "move":
        if action == "talk":
            if "Ofelia" not in npcs_spoken:
                npcs_spoken.append("Ofelia")

            input("I approach the only living person in the room. My first suspect and, potentially, my first crack in the case. She stops poking at the body long enough to glance at me. I've got no time for pleasantries. I dive right in.")
            nextStep = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY  BACK\n{Style.RESET_ALL}").lower()
            Ofelia_dialogue(nextStep, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker)

        if action == "look":
            look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

            while look_choice != "back":
                if look_choice == "cabinet":
                    location = "cabinet"
                    cab_contents = ["pen", "paper", "pencil", "stapler", "tape"]
                    take_object(cab_contents, location, inventory)
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

                if look_choice == "desk":
                    input("There's a laptop sitting on the desk. I'm looking at a Visual Studio window open to 'Lecture 1'. Lecture 1? Weren't they here for the final? There are only a few lines of code to boot, an unfinished excercise.")
                    input("Ah, interesting. This coder also had a notebook. It's filled with... bullet points on how to make the class better. A coupla notes on the lecturer's... teaching style, lets say. A little bit of animosity brewing here?")
                    if "On the desk in the living room, there is an open laptop with unfinished work from Lecture 1, and a notebook critiquing Xavier, the lecturer." not in notes_taken:
                        input("I oughtta write this down.")
                        print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                        notes_taken.append("On the desk in the living room, there is an open laptop with unfinished work from Lecture 1, and a notebook critiquing Xavier, the lecturer.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

                if look_choice == "table":
                    input("Four whole laptops, open and running. No wonder it felt hot in here. Not a single coder at any of them, though. They're all open to a Visual studio tab called 'Final', but only one has a 'Lecture Notes' tab open, too.")
                    input("I can tell by the error messages that either this final's dense, or these students are. Either way, I know one of 'em didn't make it out alive.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

                if look_choice == "body":
                    input("Dead, no doubt about it, but I can still see signs of the last moments of her poor, short life. I was expecting wounds, a gruesome scene like some of the other coding murders in my portfolio. But this... this one's different.")
                    input("Green in the face, sweat on the brow, two puffy eyes, and the glisten of a runny nose. Poor kid. Must've been a sudden sickness. Real sudden. Strange.")
                    if "Coli was killed by a sudden attack of sickness." not in notes_taken:
                        input("Seems worth writing down.")
                        print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                        notes_taken.append("Coli was killed by a sudden attack of sickness.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

                if look_choice == "person":
                    input("She looks agitated, perplexed, unsure, like someone staring down the barrel of an infinite while loop. Every once in a while she pokes the body with the toe of her shoe, probably just to pass the time.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

                if look_choice == "back":
                    livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)
            
            livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)


        if action == "notes":
            print("Alright, alright. I gotta take a time out, collect my thoughts.")
            check_stats(inventory, visited_rooms, npcs_spoken, notes_taken) 


    if action == "move":
        move_choice = input(f"{Fore.BLUE}Where would you like to go? \n BEDROOM   PATIO   DINING   BACK\n{Style.RESET_ALL}").lower()
        if move_choice == "bedroom":
            bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)
        if move_choice =="patio":
            patio(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)
        if move_choice == "dining":
            diningroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)
        if move_choice == "back":
            livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)

def bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker):
    input(f"\n{Fore.RED} THE BEDROOM {Style.RESET_ALL}")
    input("Nothing worse than an AirBnB bedroom. Stale air, Live Laugh Love signs, and two twin beds that they probably listed as being able to sleep 4 adults. Whata racket.")
    input("To step into this particular bedroom, I've gotta tip-toe around a pile of suitcases. There's also a bureau and a guy lounging on one of the beds, scrolling on his phone. Lets get to work.")
    action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()

    if action != "move":
        if action == "talk":
            if "Trout" not in npcs_spoken:
                npcs_spoken.append("Trout")
            if "ofeliaWhere" in npc_tracker:
                input("'You must be Trout, huh?' I ask, tripping over the baggage on the floor.")
                input(f"{Fore.LIGHTBLACK_EX}What? Oh... yeah, I'm Trout.{Style.RESET_ALL}")
                input("I'm looking into the murder of Coli. Y'know, your friend.")
                input("He finally puts down his phone and sits up. Now, I've got his attention.")
            else:
                input("'You must be Mr...'")
                input(f"{Fore.LIGHTBLACK_EX}Trout. Just Trout. {Style.RESET_ALL}")
                input("'Right. Trout. Well, Trout, I'm looking into the murder of Coli. Y'know, your friend.'")
                input("He finally puts down his phone and sits up. Now, I've got his attention.")
            
            nextStep = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHEN  WHY   BACK\n{Style.RESET_ALL}").lower()
            Trout_dialogue(nextStep, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker)

        if action =="look":
             look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BUREAU   SUITCASES   BACK\n{Style.RESET_ALL}").lower()
             while look_choice != "back":
                 if look_choice == "person":
                     input("He's laying on the bed, doomscrolling, no doubt. We've all got our coping vices. Even as I trip my way over all of the junk on the floor, he doesn't bat an eye.")
                     look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BUREAU   SUITCASES   BACK\n{Style.RESET_ALL}").lower()
                 if look_choice == "bureau":
                     input("There's random things strewn around here. A phone charger, a bobby pin, and a new one for game developers: deoderant. The typical detritus of a traveling troupe.")
                     location = "Bureau"
                     contents = ["charger", "pin", "deoderant"]
                     take_object(contents, location, inventory)
                     look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BUREAU   SUITCASES   BACK\n{Style.RESET_ALL}").lower()
                 if look_choice == "suitcases":
                     input("Six bags make a sort of obstacle course between the door and everything else in the goddamn room. Clothes spilling out everywhere. There's a few notebooks and bits of art supplies to add to the tripping hazards. Seems like they've been here for a hot second.")
                     look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BUREAU   SUITCASES   BACK\n{Style.RESET_ALL}").lower()
                 if look_choice == "back":
                     bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)

        if action == "notes":
            print("Alright, alright. I gotta take a time out, collect my thoughts.")
            check_stats(inventory, visited_rooms, npcs_spoken, notes_taken) 

    if action == "move":
        move_choice = input(f"{Fore.BLUE}Where would you like to go? \n BATHROOM   LIVINGROOM   BACK\n{Style.RESET_ALL}").lower()
        if move_choice == "bathroom":
            bathroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)
        if move_choice =="patio":
            patio(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)
        if move_choice == "dining":
            diningroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)
        if move_choice == "back":
            livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)

def patio(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker):
    input(f"\n{Fore.RED} THE PATIO {Style.RESET_ALL}")
    input("")





def diningroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker):
    input(f"\n{Fore.RED} THE DINING ROOM {Style.RESET_ALL}")

def bathroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker):
    input(f"\n{Fore.RED} THE BATHROOM {Style.RESET_ALL}")
    

def start_mystery(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker):
    input("Figures...")
    input("I'm curled up in bed, cozier than a grandma in her afghan on Christmas morning. I even kissed my cockapoo goodnight for God's sake, and I get a call.")
    input("Another coding class gone sour. Three students, two TAs, and a lecturer under one roof, taking their final test. Their first face-to-face meeting and, for one of them, their last. Now I've gotta go and straighten out the details.")
    input("...")
    input("It's gonna be a long night.\n")

    print(f"\n{Fore.RED} CODE RED MYSTERIES {Style.RESET_ALL}presents...")
    input(f"{Fore.BLUE} THE CASE OF THE TA TERMINATOR {Style.RESET_ALL}\n")

    input("The flatfoots are already there by the time I roll up, standing around outside like a bunch of unused variables in a begginner's CS1 project. I spot the chief leaning against her cruiser.")
    input("I ask her what's on everyone's mind. 'What's the situation in there, chief?' \nShe sighs, pulls out a pack of cigs from her shirt pocket.")
    input(f"{Fore.LIGHTBLACK_EX}One dead, five suspects. We've got the perimeter covered, you just have to go in and figure out who to book. Easy right?{Style.RESET_ALL}")
    input("'As python.' I chuckle. She takes a drag. Figures.")
    input("I guess that's my cue to get the investigation started.\n")
    livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)

inventory  = []
visited_rooms = []
npcs_spoken = []
npc_tracker =[]
notes_taken = []

start_mystery(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker)
#actions you can take: Look, Talk, Take, Use
#Rooms: Living room, bedroom, bathroom, kitchen, dining room, patio
#NPCs: Chloe, Ofelia, Trout, Xavier, Julia