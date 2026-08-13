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

def isLocked (door, key, object, inventory, used_inventory):
    unlocked = False
    if object in inventory and key == object:
        inventory.remove(object)
        used_inventory.append(object)
        unlocked = True
        print(f"{Fore.GREEN}You have opened {door} with {object}.{Style.RESET_ALL}")

    elif object in used_inventory:
        unlocked = True
        print(f"{Fore.GREEN}You have already unlocked {door} with {key}.{Style.RESET_ALL}")
    
    elif key != object:
        print(f"{Fore.GREEN}It doesn't seem like you can unlock the {door} with {object}.{Style.RESET_ALL}")
    
    elif len(inventory)== 0:
        print(f"{Fore.GREEN}You don't have anything in your inventory to unlock {door}.{Style.RESET_ALL}")
        
    return unlocked

def Ofelia_dialogue(choice, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker, used_items):
    while choice != "back":
        if choice == "who":
            input("'Who are you? What's your beef with the deceased?'")
            input(f"{Fore.LIGHTBLACK_EX}I'm Ofelia, and I've got no 'beef' with Coli! I'm just a student, ok? I'm just here to learn some code, get better at game jams.{Style.RESET_ALL}")
            input("'Alright then. Sure...'")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()
            if "ofeliaWho" not in npc_tracker:
                npc_tracker.append("ofeliaWho")
        elif choice == "what":
            input("'What the hell happened here?'")
            input(f"{Fore.LIGHTBLACK_EX}We were working on our Computer Science finals when all of the sudden Coli starts coughing and sneezing all over the place.{Style.RESET_ALL}")
            input("'Ugh. Gross.'")
            input(f"{Fore.LIGHTBLACK_EX}Right? Well, she said she felt super sick, and before we knew it, she was on the floor. DEAD! Like, what the fuck?{Style.RESET_ALL}")
            input("'Watch the language, kid.'")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()
            if "ofeliaWhat" not in npc_tracker:
                npc_tracker.append("ofeliaWhat")
        elif choice == "when":
            input("'When did this sickness start? How long was she feeling under the weather?'")
            input(f"{Fore.LIGHTBLACK_EX}Literally five, maybe ten minutes MAX. She was fine until... this.{Style.RESET_ALL}")
            input("She gestures at the body. Never heard of a flu that could take down a person in minutes.")
            if "The sickness that killed Coli took her down within minutes of manifesting. Something stronger than the flu must be at work here." not in notes_taken:
                print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                notes_taken.append("The sickness that killed Coli took her down within minutes of manifesting. Something stronger than the flu must be at work here.")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()
            if "ofeliaWhen" not in npc_tracker:
                npc_tracker.append("ofeliaWhen")
        elif choice == "where":
            input("'Just you in here? Where's the rest of the coding crew?'")
            input(f"{Fore.LIGHTBLACK_EX}Once the cops showed up, we spread out through the house. We're all pretty shaken. Trout's in the bedroom, Chloe's on the patio, Julia's in the dining room, and Xavier's in the kitchen.{Style.RESET_ALL}")
            input("'Sure, sure. I'll make sure to check in on them, too.'")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()
            if "ofeliaWhere" not in npc_tracker:
                npc_tracker.append("ofeliaWhere")
        elif choice == "why":
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

        else:
            print("English, Einstein! I didn't understand ya!")
            choice= input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()

    if choice == "back":
        if "ofeliaWho" in npc_tracker:
            input("'Thanks, Ofelia. Don't go anywhere, I might check back with you later.'")
        else:
            input("There'll be more questions for ya later. Don't go too far.")
        livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

    else:
        print("English, Einstein! I didn't understand ya!")
        choice= input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()

def Julia_dialogue(choice, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker, used_items):
    while choice != "back":
        if choice == "who":
            if "juliaWho" not in npc_tracker:
                npc_tracker.append("juliaWho")

            input("'Alright, who have I got here? You another coding student?")
            input(f"{Fore.LIGHTBLACK_EX}Oh no, not really. I'm Julia! I guess I'm kind of a coding TA, but just, like, the moral support kind.{Style.RESET_ALL}")
            input("'Two whole TAs for a class of three?'")
            input(f"{Fore.LIGHTBLACK_EX}Well... Coli was actually trying to help the class. I was just there to be there. Maybe monitor cheating or attendance. It's really just a joke, though!{Style.RESET_ALL}")
            input("'Lotta jokes with you lot, huh?'")

            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHY   BACK\n{Style.RESET_ALL}").lower()
        
        elif choice == "what":
            input("'Explain to me EXACTLY what it is you do for this class.'")
            input(f"{Fore.LIGHTBLACK_EX}Honestly, nothing. I'd just pop in to hang out with my friends, see what they were up to! They just named me 'TA' because I was there. {Style.RESET_ALL}")
            input("'What about the attendence, assignments, cheating, those sorts of things?'")
            input(f"{Fore.LIGHTBLACK_EX}No one really took that seriously. I mean...{Style.RESET_ALL}")
            input("'What do you mean?'")
            input(f"{Fore.LIGHTBLACK_EX}I mean.. I'm sure SOMEONE kept track. Probably... I dunno!{Style.RESET_ALL}")
            if "Julia thinks someone probably kept track of the student's class contributions." not in notes_taken:
                print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                notes_taken.append("Julia thinks someone probably kept track of the student's class contributions.")
            if "juliaWhat" not in npc_tracker:
                npc_tracker.append("juliaWhat")

            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHY   BACK\n{Style.RESET_ALL}").lower()

        elif choice == "why":
            if "juliaWhat" in npc_tracker:
                input("'Why'd you get the TA moniker then, if you were just 'hanging out'?'")
                input(f"{Fore.LIGHTBLACK_EX}Well, it was funny, I guess! Coli was there trying to help. She was functionally a TA for that first class. \nThen I showed up and got named the 'Real TA' after Coli volunteered for it. Just a bit of irony. Funny, that's all!{Style.RESET_ALL}")
                input("'Sure... funny.'")
                if "Julia, an uninvolved friend, was named TA to spite Coli for wanting to be TA." not in notes_taken:
                    notes_taken.append("Julia, an uninvolved friend, was named TA to spite Coli for wanting to be TA.")
                    print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                if "juliaWhy" not in npc_tracker:
                    npc_tracker.append("juliaWhy")

                choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHY   BACK\n{Style.RESET_ALL}").lower()

            else:
                input("Don't think I have enough info to ask this question, yet. I oughtta keep looking around, come back later.")
                choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHY   BACK\n{Style.RESET_ALL}").lower()

        else:
            print("What was that?")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHY   BACK\n{Style.RESET_ALL}").lower()

    if choice == "back":
        input("'Alright, you'd better stay right where you are for now. Things out there are a little... sketchy.'")
        diningroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
            
    else:
        print("What was that?")
        choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHY   BACK\n{Style.RESET_ALL}").lower()

def Chloe_dialogue(choice, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker, used_items):
    while choice != "back":
        if choice == "who":
            input("'You must be another one of the coders, huh?'")
            input(f"{Fore.LIGHTBLACK_EX}Yeah. Chloe.{Style.RESET_ALL}")
            input("'Coli? Isn't that the name of the deceased?'")
            input(f"{Fore.LIGHTBLACK_EX}NO! That's COLI, I'm CHLOE! C - H - L - {Style.RESET_ALL}")
            input("'Alright, alright, cut the spellin', kid. This is an investigation, not an English class.'")
            input(f"{Fore.LIGHTBLACK_EX}Sorry, sorry. It's just, everyone always gets that confused. Even the people who've known us forever!{Style.RESET_ALL}")
            input("'And that really gets your goat, don't it?'")
            input("She sighs, obviously embarassed at her little tantrum.")
            input(f"{Fore.LIGHTBLACK_EX}I guess it does. But in my defense, it's been a bit of a stressful night. And anyways, you're a cop! Precision is important, make sure you get it right in your notes!{Style.RESET_ALL}")
            if "Col- er, uh - Chloe hates it when people get her name mixed up with Coli's." not in notes_taken:
                notes_taken.append("Col- er, uh - Chloe hates it when people get her name mixed up with Coli's.")
                print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
            if "chloeWho" not in npc_tracker:
                npc_tracker.append("chloeWho")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   BACK\n{Style.RESET_ALL}").lower()

        elif choice == "what":
            input("'What are you doing out here? Don't you know there's a murderer on the loose?'")
            input(f"{Fore.LIGHTBLACK_EX} I'm just... sqeamish. Like, REALLY squeamish. So when Coli went down, I had to get outta there before a fainting spell came on. Had to get some fresh air, and quick.{Style.RESET_ALL}")
            input("'Get some air and start tearing up the landscaping?'")
            input(f"{Fore.LIGHTBLACK_EX}I'm just picking out the dead flowers, mostly. It looked like they could use it.{Style.RESET_ALL}")
            input("'Ah so you know a bit about plants, huh? Any of these potentially poisonous? I'm talking flu-like symptoms, bad enough to kill a gamer.'")
            input(f"{Fore.LIGHTBLACK_EX}Kill a gamer? You think one of us took Coli out?? That's crazy!{Style.RESET_ALL}")
            input("'They bring in a detective and suddenly everyone's shocked when I start asking questions.'")
            input(f"{Fore.LIGHTBLACK_EX}Jeez. Well, it was tragic but it was NOT murder. Especially not by petunia.{Style.RESET_ALL}")
            input("'You know of any plant that might? Work with me, kid.'")
            input(f"{Fore.LIGHTBLACK_EX}I mean, maybe a mold or fungus? But death by a flu-fungus would take weeks, I've never heard about a fast-acting one. And whatever did that to Coli was quick to it.{Style.RESET_ALL}")
            input("'Interesting.'")
            if "Chloe said that there might exist a fungus or mold that could cause a death by flu-like symptoms." not in notes_taken:
                print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                notes_taken.append("Chloe said that there might exist a fungus or mold that could cause a death by flu-like symptoms.")
            if "chloeWhat" not in npc_tracker:
                npc_tracker.append("chloeWhat")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   BACK\n{Style.RESET_ALL}").lower()

        else:
            print("Listen, I can't understand ya when you type like that.")
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT  BACK\n{Style.RESET_ALL}").lower()

    if choice == "back":
        if "chloeWho" in npc_tracker:
            input("'Well, that's all I've got for you now, Cleo-'")
            input(f"{Fore.LIGHTBLACK_EX}IT'S CHLO-{Style.RESET_ALL}")
            input("'Yeah, yeah. Stay where I can find ya. I might be back later.'")
            patio(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        else:
            input("'Stay where I can find ya. I might be back later.'")
            patio(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
    else:
        print("Listen, I can't understand ya when you type like that.")
        choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT  WHY   BACK\n{Style.RESET_ALL}").lower()

def Trout_dialogue(choice, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker, used_items):
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

        elif choice == "when":
            input("'When did you guys get here? I mean, how long have you been staying here?'")
            input(f"{Fore.LIGHTBLACK_EX}Two days ago. We've just been hanging out, only got to the final tonight.{Style.RESET_ALL}")
            input("'Anything happen while you kids were just 'hanging out'?'")
            input(f"{Fore.LIGHTBLACK_EX}Not that I can think of... We had a great time, no problems.{Style.RESET_ALL}") 
            choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHEN   WHY   BACK\n{Style.RESET_ALL}").lower()
            if "troutWhen" not in npc_tracker:
                npc_tracker.append("troutWhen")

        elif choice == "why":
            if "ofeliaWhy" in npc_tracker:
                input("'Alright, I'll be outta your hair in a second. Just a question.. or a few.'")
                input("'Why did you write a 'Blow Up Coli' function into your code?'")
                input("At this, Trout jumps to his feet, defensive, paler than a terminal in light mode.")
                input(f"{Fore.LIGHTBLACK_EX}That's what this is? You're interrogating me for murder?? She got sick! Yeah, it was weird but... c'mon, man.{Style.RESET_ALL}")
                input(("'Just answer the question, will ya?'"))
                input("He sits back down, head in his hands.")
                input(f"{Fore.LIGHTBLACK_EX}During the first ever lecture Xavier hosted, Coli was there. Xavier was teaching, but she jumped in to try and explain something we weren't really understanding. \nShe appointed herself TA, and then she told us to try and write functions for the first time on our own. Just to be funny, as a little protest, I named my function 'Blow Up Coli'.{Style.RESET_ALL}")
                input("'I see.'")
                input(f"{Fore.LIGHTBLACK_EX}I swear to God that's all it was! I mean, she's out there in one piece, isn't she?! No one really blew her up!{Style.RESET_ALL}")
                input("'Calm down, kid. I'm trying to get a firm shake on the whole thing. I don't know enough to start making accusations... yet.'")
                if "troutWhy" not in npc_tracker:
                    npc_tracker.append("troutWhy")
                if "Trout made jokes about blowing Coli up when she gave him an assignment." not in notes_taken:
                    print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                    notes_taken.append("Trout made jokes about blowing Coli up when she gave him an assignment.")

                choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHEN   WHY   BACK\n{Style.RESET_ALL}").lower()
            else:
                input("Don't think I have enough info to ask this question, yet. I oughtta keep looking around, come back later.")
                choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHEN   WHY   BACK\n{Style.RESET_ALL}").lower()

        else:
            print("I got no idea what that means.")
            choice= input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHEN   WHY   BACK\n{Style.RESET_ALL}").lower()


    if choice == "back":
        input("'Well, I'm gonna get on with it. Be careful out there, Trout. You don't wanna be the next one swimming with the fishes.'")
        bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

    else:
        print("English, Einstein! I didn't understand ya!")
        choice= input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY   BACK\n{Style.RESET_ALL}").lower()

def Xavier_dialogue(choice, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker, used_items):
    while choice != "back":
        if choice == "who":
            if "xavierWho" not in npc_tracker:
                npc_tracker.append("xavierWho")
            input("'Alright, Chef Boyardee, you got a real name?")
            input(f"{Fore.LIGHTBLACK_EX}Xavier, I was the one teaching all the coding classes.{Style.RESET_ALL}")
            input("'Ah, so a chef AND a professor.'")
            input(f"{Fore.LIGHTBLACK_EX}Just a chef right now, if you have to put it that way. It's late, no one's eaten, and after everything with Coli, I think we can pretty much call the classes quits.{Style.RESET_ALL}")
            input("'Makes sense for being down a whole TA.")
        elif choice == "what":
            if "xavierWho" in npc_tracker:
                if "xavierWhat" not in npc_tracker:
                    npc_tracker.append("xavierWhat")
                input("'Tell me about these 'classes'. What's teaching it been like?'")
                input(f"{Fore.LIGHTBLACK_EX}A lot of work, but pretty fine overall. Well, until...{Style.RESET_ALL} He gestures towards the living room with his spoon.")
                input("'Expound on that: 'pretty fine'?'")
                input(f"{Fore.LIGHTBLACK_EX} Started out strong. Everyone, plus Julia, showed up. Coli dropped out around the second week. Then Trout, thenm Ofelia. Turned into just Chloe and me until we all got together here.{Style.RESET_ALL}")
                input("'And you were fine with that? Everyone bailing?'")
                input(f"{Fore.LIGHTBLACK_EX}Bailing on a free, voluntary coding class that I hosted to help with free, voluntary game jams? Yeah, I think I'll be alright.{Style.RESET_ALL}.")
                if "Xavier kept track of attendance to his classes, and Coli was the first to drop out." not in notes_taken:
                    notes_taken.append("Xavier kept track of attendance to his classes, and Coli was the first to drop out.")

            else:
                input("Don't think I have enough info to ask this question, yet. I oughtta keep looking around, come back later.")
                choice = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHEN   WHY   BACK\n{Style.RESET_ALL}").lower()

        elif choice == "when":
            if "xavierWhen" not in npc_tracker:
                npc_tracker.append("xavierWhen")
            input("'When did you all eat last?'")
            input(f"{Fore.LIGHTBLACK_EX}Lunch, I guess. A few snacks here and there.{Style.RESET_ALL}")
            input("'Anybody have any allergies? I'm thinking the 'spontaneously keel over and die' sort.'")
            input(f"{Fore.LIGHTBLACK_EX}We cleared up all of the allergies when we went grocery shopping. Coli never mentioned anything, not sure what would have done that to her.{Style.RESET_ALL}")


        
    if choice == "back":
        kitchen(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
    else:
        print("If I don't get it, he won't get it. Try that again.")
        



def take_object (objects, location, inventory):
    print (f"Ah, theres some stuff in this {location}. Looks like a\n {objects}")
    take_affirm = input(f"{Fore.BLUE}Would you like to add one of these objects to your inventory?   YES   NO\n{Style.RESET_ALL}").lower()
    while take_affirm !="no":
        if take_affirm == "yes":
            object_take = input(f"{Fore.BLUE}Which object will you take? {objects}\n{Style.RESET_ALL}").lower()
            if object_take in objects:
                inventory.append(object_take)
                objects.remove(object_take)
                input(f"Could be helpful, I think I'll put this {object_take} in my pocket.")
                print(f"{Fore.GREEN} You have added {object_take} to your inventory.{Style.RESET_ALL}")
                take_affirm = input(f"{Fore.BLUE}Would you like to add one of these objects to your inventory?   YES   NO\n{Style.RESET_ALL}").lower()
            else:
                print(f"Did I ever mention {object_take}? NO!")
                object_take = input(f"{Fore.BLUE}Which object will you take? {objects}\n{Style.RESET_ALL}").lower()
        else:
            print("It's a yes or no question. Try again.")
            take_affirm = input(f"{Fore.BLUE}Would you like to add one of these objects to your inventory?   YES   NO\n{Style.RESET_ALL}").lower()

    if take_affirm == "no":
        input("Back to the matter at hand.")
        
    else:
        print("Type clearly, would ya?!?")
        take_affirm = input(f"{Fore.BLUE}Would you like to add one of these objects to your inventory?   YES   NO\n{Style.RESET_ALL}").lower()

def check_stats(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    check = input(f"{Fore.BLUE}Check   INVENTORY   ROOMS   NPCS   NOTES   BACK\n{Style.RESET_ALL}").lower()

    while check != "back":
        if check == "inventory":
          if len(inventory)<1:
              print("Nothin in my pockets. Yet.")
              check = input(f"{Fore.BLUE}Check   INVENTORY   ROOMS   NPCS   NOTES   BACK\n{Style.RESET_ALL}").lower()
          else:
             print(f"In my pockets, I've got a {inventory}")
             check = input(f"{Fore.BLUE}Check   INVENTORY   ROOMS   NPCS   NOTES   BACK\n{Style.RESET_ALL}").lower()
        if check == "rooms":
            print(f"So far, looks like I've visited {visited_rooms}")
            check = input(f"{Fore.BLUE}Check   INVENTORY   ROOMS   NPCS   NOTES   BACK\n{Style.RESET_ALL}").lower()
        if check == "npcs":
            if len(npcs_spoken)<1:
                print("Haven't spoken to anyone. I should get on that.")
                check = input(f"{Fore.BLUE}Check   INVENTORY   ROOMS   NPCS   NOTES   BACK\n{Style.RESET_ALL}").lower()
            else:
                print(f"So far, I've talked to {npcs_spoken}")
                check = input(f"{Fore.BLUE}Check   INVENTORY   ROOMS   NPCS   NOTES   BACK\n{Style.RESET_ALL}").lower()
        if check == "notes":
            if len(notes_taken)<1:
                print("Notebook's empty.")
                check = input(f"{Fore.BLUE}Check   INVENTORY   ROOMS   NPCS   NOTES   BACK\n{Style.RESET_ALL}").lower()
            else:
                print(f"Let's see what I jotted down so far...")
                for i in range(len(notes_taken)):
                    print("-" + notes_taken[i])
                check = input(f"{Fore.BLUE}Check   INVENTORY   ROOMS   NPCS   NOTES   BACK\n{Style.RESET_ALL}").lower()
        else:
            print("...try that again...")
            check = input(f"{Fore.BLUE}Check   INVENTORY   ROOMS   NPCS   NOTES   BACK\n{Style.RESET_ALL}").lower()

    if check == "back":
        return check   

def livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    input(f"\n{Fore.RED} THE LIVING ROOM {Style.RESET_ALL}")
    input("It's a small room, unassuming. Signs of nerds doing computer things everywhere. Noisy from all the laptop fans running nonstop. A coffee table, a cabinet, and a desk fill the bulk of the space. \nTwo bodies: one upright, breathing. The other, not so much.")
    input("Time to make my move.")
    if "living room" not in visited_rooms:
        visited_rooms.append("living room")
    action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()
    if action != "move":
        if action == "talk":
            if "Ofelia" not in npcs_spoken:
                npcs_spoken.append("Ofelia")

            input("I approach the only living person in the room. My first suspect and, potentially, my first crack in the case. She stops poking at the body long enough to glance at me. I've got no time for pleasantries. I dive right in.")
            nextStep = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHEN   WHERE   WHY  BACK\n{Style.RESET_ALL}").lower()
            Ofelia_dialogue(nextStep, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker, used_items)

        if action == "look":
            look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

            while look_choice != "back":

                if look_choice == "cabinet":
                    location = "cabinet"
                    cab_contents = ["pen", "paper", "pencil", "stapler", "tape"]
                    take_object(cab_contents, location, inventory)
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

                elif look_choice == "desk":
                    input("There's a laptop sitting on the desk. I'm looking at a Visual Studio window open to 'Lecture 1'. Lecture 1? Weren't they here for the final? There are only a few lines of code to boot, an unfinished excercise.")
                    if "On the desk in the living room, there is an open laptop with unfinished work from Lecture 1." not in notes_taken:
                        input("I oughtta write this down.")
                        print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                        notes_taken.append("On the desk in the living room, there is an open laptop with unfinished work from Lecture 1.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

                elif look_choice == "table":
                    input("Four whole laptops, open and running. No wonder it felt hot in here. Not a single coder at any of them, though. They're all open to a Visual Studio tab called 'Final', but only one has an 'Assignments' tab open, too.")
                    input("I can tell by the error messages that either this final's dense, or these students are. Either way, I know one of 'em didn't make it out alive.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

                elif look_choice == "body":
                    input("Dead, no doubt about it, but I can still see signs of the last moments of her poor, short life. I was expecting wounds, a gruesome scene like some of the other coding murders in my portfolio. But this... this one's different.")
                    input("Green in the face, sweat on the brow, two puffy eyes, and the glisten of a runny nose. Poor kid. Must've been a sudden sickness. Real sudden. Strange.")
                    if "Coli was killed by a sudden attack of sickness." not in notes_taken:
                        input("Seems worth writing down.")
                        print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                        notes_taken.append("Coli was killed by a sudden attack of sickness.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

                elif look_choice == "person":
                    input("She looks agitated, perplexed, unsure, like someone staring down the barrel of an infinite while loop. Every once in a while she pokes the body with the toe of her shoe, probably just to pass the time.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

                else:
                    print("What was that? Type it again!")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()

            if look_choice == "back":
                action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()

            else:
                print("What was that? Type it again!")
                look_choice = input(f"{Fore.BLUE}What would you like to look at? \n BODY   PERSON   DESK   TABLE   CABINET   BACK\n{Style.RESET_ALL}").lower()


        if action == "notes":
            print("Alright, alright. I gotta take a time out, collect my thoughts.")
            check_command = check_stats(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items) 
            if check_command == "back":
                livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

        else:
            print("No clue what you just said, kid.")
            livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

    if action == "move":
        move_choice = input(f"{Fore.BLUE}Where would you like to go? \n BEDROOM   PATIO   DINING   BACK\n{Style.RESET_ALL}").lower()
        if move_choice == "bedroom":
            bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        elif move_choice =="patio":
            patio(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        elif move_choice == "dining":
            diningroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        elif move_choice == "back":
            livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        else:
            print("...try that again...")
            move_choice = input(f"{Fore.BLUE}Where would you like to go? \n BEDROOM   PATIO   DINING   BACK\n{Style.RESET_ALL}").lower()

def bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    input(f"\n{Fore.RED} THE BEDROOM {Style.RESET_ALL}")
    input("Nothing worse than an AirBnB bedroom. Stale air, Live Laugh Love signs, and two twin beds that they probably listed as being able to sleep 4 adults. Whata racket.")
    input("To step into this particular bedroom, I've gotta tip-toe around a pile of suitcases. There's also a bureau and a guy lounging on one of the beds, scrolling on his phone. Lets get to work.")
    action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()
    if "bedroom" not in visited_rooms:
        visited_rooms.append("bedroom")
    while action != "move":
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
            Trout_dialogue(nextStep, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker, used_items)

        if action =="look":
             look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BUREAU   SUITCASES   BACK\n{Style.RESET_ALL}").lower()
             while look_choice != "back":
                 if look_choice == "person":
                     input("He's laying on the bed, doomscrolling, no doubt. We've all got our coping vices. Even as I trip my way over all of the junk on the floor, he doesn't bat an eye.")
                     look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BUREAU   SUITCASES   BACK\n{Style.RESET_ALL}").lower()
                 elif look_choice == "bureau":
                     input("There's random things strewn around here. A phone charger, a bobby pin, and a new one for game developers: deoderant. The typical detritus of a traveling troupe.")
                     location = "Bureau"
                     contents = ["charger", "pin", "deoderant"]
                     take_object(contents, location, inventory)
                     look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BUREAU   SUITCASES   BACK\n{Style.RESET_ALL}").lower()
                 elif look_choice == "suitcases":
                     input("Six bags make a sort of obstacle course between the door and everything else in the goddamn room. Clothes spilling out everywhere. There's a few notebooks and bits of art supplies to add to the tripping hazards. Seems like they've been here for a hot second.")
                     look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BUREAU   SUITCASES   BACK\n{Style.RESET_ALL}").lower()
                 elif look_choice == "back":
                     bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
                 else:
                     print("...try that again...")
                     look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BUREAU   SUITCASES   BACK\n{Style.RESET_ALL}").lower()
             if look_choice == "back":
                action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()
             else:
                print("...try that again...")
                look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BUREAU   SUITCASES   BACK\n{Style.RESET_ALL}").lower()


        if action == "notes":
            print("Alright, alright. I gotta take a time out, collect my thoughts.")
            check_command = check_stats(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
            if check_command == "back":
                bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

        else:
            print("What's the matter with you, huh? Speak up!")
            action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()

    if action == "move":
        move_choice = input(f"{Fore.BLUE}Where would you like to go? \n BATHROOM   LIVINGROOM   BACK\n{Style.RESET_ALL}").lower()
        if move_choice == "bathroom":
            bathroom_door(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        elif move_choice =="patio":
            patio(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        elif move_choice == "dining":
            diningroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        elif move_choice == "livingroom":
            livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

    else:
        print("C'mon, kid, answer the question.")
        action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()

def patio(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    input(f"\n{Fore.RED} THE PATIO {Style.RESET_ALL}")
    input("The night is hot, sticky, buggier than a text-based adventure coded by an artist in Python.")
    input("It's a small patio opening up to an even smaller yard. There's a number of planters taking up most of the floor space, all teeming with life, unlike a certain TA.")
    input("There's another coding student there, fidgeting with the foliage. Might offer me some good info if I ask the right questions.")
    if "patio" not in visited_rooms:
        visited_rooms.append("patio")
    action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()

    while action != "move":
        if action == "look":
            look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PATIO   PLANTERS   PERSON   BACK\n{Style.RESET_ALL}").lower()
            while look_choice != "back":
                if look_choice == "patio":
                    input("Concrete pad, mostly. Looks like someone tried to powerwash it but didn't bother to move the planters. Figures.")
                    input("Whoever did the washing left big swaths of green and black grime here and there. Algae, dirt, and maybe... mold? There's a few smaller bare patches, too. Was someone scraping up this stuff? Why'd they do that?")
                    if "The patio has some suspicious spots where a moldy substance has been scraped away." not in notes_taken:
                        notes_taken.append("The patio has some suspicious spots where a moldy substance has been scraped away.")
                        print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PATIO   PLANTERS   PERSON   BACK\n{Style.RESET_ALL}").lower()

                elif look_choice == "planters":
                    input("I've never been one for gardening, to tell ya the truth. These plants are just leaves and flowers to me. Green spikes, pink trumpets, your typical Home Depot Garden Center fair. Pretty, you could say.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PATIO   PLANTERS   PERSON   BACK\n{Style.RESET_ALL}").lower()

                elif look_choice == "person":
                    input("She looks pale, sweaty, and I don't think that's just the stress of a coding final. She keeps rifling through the flowers, picking out brown and green bits just to throw them on the lawn.")
                    input("She's got a shaky hand, but a steadfast pruning method. Might be plant's aren't the only thing she's chopped tonight.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PATIO   PLANTERS   PERSON   BACK\n{Style.RESET_ALL}").lower()

                else:
                    print("Gonna need ya to slow down and type more clearly, kid.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PATIO   PLANTERS   PERSON   BACK\n{Style.RESET_ALL}").lower()

            if look_choice == "back":
                action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()

            else:
                print("Gonna need ya to slow down and type more clearly, kid.")
                look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PATIO   PLANTERS   PERSON   BACK\n{Style.RESET_ALL}").lower()

        if action == "talk":
            if "Chloe" not in npcs_spoken:
                npcs_spoken.append("Chloe")
            input("She must've heard me come outside. Didn't seem to startle her too much when I walked up, though she certainly didn't look happy that I was interrupting her weeding. Too bad. There's someone else pushing up daisies tonight..")
            nextStep = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   BACK\n{Style.RESET_ALL}").lower()
            Chloe_dialogue(nextStep, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker, used_items)

        else:
            print(f"Look, if I knew what '{action}' was, then sure. But I don't.")
            action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()

    if action == "move":
        move_choice = input(f"{Fore.BLUE}Where would you like to go? \n LIVINGROOM   BACK\n{Style.RESET_ALL}").lower()
        if move_choice == "back":
            patio(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        elif move_choice == "livingroom":
            livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        else:
            "Huh? Where?"
            move_choice = input(f"{Fore.BLUE}Where would you like to go? \n LIVINGROOM   BACK\n{Style.RESET_ALL}").lower()

    if action =="notes":
        print("Alright, alright. I gotta take a time out, collect my thoughts.")
        check_command = check_stats(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items) 
        if check_command == "back":
            bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

    else:
        print(f"Look, if I knew what '{action}' was, then sure. But I don't.")
        action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()

def diningroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    input(f"\n{Fore.RED} THE DINING ROOM {Style.RESET_ALL}")
    input("Ah, so this is where everyone who didn't fit in the bedroom is bunking. Pillows and blankets litter the floor around the 4-seater dining table. Looks like I've got another suspect to question, too. She's sitting, pre-occupied. I'll have to disturb her.")
    action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()

    while action != "move":
        if action == "look":
            look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BEDS   BACK\n{Style.RESET_ALL}").lower()
            while look_choice != "back":
                if look_choice == "person":
                    input("She seems... content. Strange when there's a body in the other room.")
                    input("She's sitting, sketching in a book that's already nearly full. Magical girls in every color on the spread she's working on, all wearing witch hats... spooky.")
                elif look_choice == "beds":
                    input("There's nont much to these so-called 'beds'. Its pretty clear that they were expecting more sleeping spaces than they got. These beds are looking like a game jam game with no artists: random assets thrown together to try and make something work.")
                    input("Couch cushions, towels, curtains, all to fill in where the bed count failed. They've been spending the nights in here, sure, but with beds like this, no one's been getting any shuteye.")
                elif look_choice=="back":
                    action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()
                else:
                    print("I'm going to level with ya, I have no clue what that means.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BEDS   BACK\n{Style.RESET_ALL}").lower()
            if look_choice == "back":
                diningroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
            else:
                print("I'm going to level with ya, I have no clue what that means.")
                look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   BEDS   BACK\n{Style.RESET_ALL}").lower()
        
        if action == "talk":
            if "Julia" not in npcs_spoken:
                npcs_spoken.append("Julia")
            input("'Evening.'")
            input("My new suspect doesn't even turn. She's still doodling.")
            input("'Hello?'")
            input("Nothing.")
            input("I tap on the lady's shoulder, none to gently. She jumps nearly outta her skin, and takes out one of her ear buds.")
            input("'Good,' I say. 'I was starting to think I had two stiffs on my hands'.")
            nextStep = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHY   BACK\n{Style.RESET_ALL}").lower()
            Julia_dialogue(nextStep, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker, used_items)

        if action == "notes":
            print("Alright, alright. I gotta take a time out, collect my thoughts.")
            check_command = check_stats(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items) 
            if check_command == "back":
                livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

    if action == "move":
        move_choice = input(f"{Fore.BLUE}Where would you like to go? \n LIVINGROOM   KITCHEN   BACK\n{Style.RESET_ALL}").lower()
        if move_choice == "livingroom":
            livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        elif move_choice =="kitchen":
            kitchen(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        elif move_choice == "back":
            diningroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        else:
            print("...try that again...")
            move_choice = input(f"{Fore.BLUE}Where would you like to go? \n BEDROOM   PATIO   DINING   BACK\n{Style.RESET_ALL}").lower()

def bathroom_door(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    if "pin" not in used_items:
        input("Should I have been surprised that the bathroom door is locked? I don't know, but I was. I rattle the knob, at the very least expecting an 'Occupied!' or 'Get lost!' but no one answers.")
        input("'Hey!' I knock. And again, this time like I mean business. 'HEY! Anyone in there?' Nothin'. Figures.")
        input("I inspect the knob. Looks like a simple lock, landlord grade for sure. I could probably pick it if I had the right perscription lenses on... and the right tool.")
        door_choice = input(f"{Fore.BLUE}What would you like to do?\nUSE   BACK\n{Style.RESET_ALL}").lower()
        while door_choice != "back":
            if door_choice == "use" and len(inventory) >0:
                use_choice = input(f"{Fore.BLUE}What would you like to use on the bathroom door?\n {inventory}{Style.RESET_ALL}\n").lower()
                doorStat = isLocked ("bathroom door", "pin", use_choice, inventory, used_items)
                if doorStat:
                    input("Aha! Of course, the bobby pin from the bedroom bureau. I adjust my glasses, take a good look, and fit it into the bathroom keyhole. Unlocked, an easy picking job. Now to see what's inside.")
                    bathroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
                    break
                else:
                    input("Damn. Gonna be tougher than I thought. Might need to look around more.")
                    door_choice = input(f"{Fore.BLUE}What would you like to do?\nUSE   BACK\n{Style.RESET_ALL}").lower()

            elif door_choice == "use" and len(inventory) == 0:
                print("Nothing in my pockets but lint. Looks like I'll have to look around some more to get through here.")
                door_choice = input(f"{Fore.BLUE}What would you like to do?\nUSE   BACK\n{Style.RESET_ALL}\n").lower()

            else:
                print("No clue what that means.")
                door_choice = input(f"{Fore.BLUE}What would you like to do?\nUSE   BACK\n{Style.RESET_ALL}\n").lower()

        if door_choice == "back":
            bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

        else:
            print("No clue what that means.")
            use_choice = input(f"{Fore.BLUE}What would you like to use on the bathroom door?\n {inventory}{Style.RESET_ALL}").lower()
    
    if "pin" in used_items:
        bathroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

def secret_door(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    if "knife" not in used_items:
        input("I kneel down to get a good look at the thing. How's the grout still so black with all that bleach? I dunno, not the problem. I press on the panel in the wall, and it gives way just a little.")
        input("I try and get it off the wall, but my fingernails and my patience are too short. I'm gonna need something to pry open this door.")
        door_choice = input(f"{Fore.BLUE}What would you like to do?\nUSE   BACK{Style.RESET_ALL}\n").lower()
        while door_choice != "back":
            if door_choice == "use":
                use_choice = input(f"{Fore.BLUE}What would you like to use on the wall panel? {inventory}{Style.RESET_ALL} \n").lower()
                doorStat = isLocked ("wall panel", "knife", use_choice, inventory, used_items)
                if doorStat:
                    input("Perfect. This knife ougtta do the job. I slip the blade into the crack between the wall and the panel. It comes loose with a waft of damp, stale air. It's a tunnel. What kinda pervert house...")
                    bathroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
                    break
                else:
                    input("Damn. Gonna be tougher than I thought. Might need to look around more.")
                    door_choice = input(f"{Fore.BLUE}What would you like to do?\nUSE   BACK{Style.RESET_ALL} \n").lower()
        if door_choice == "back":
            bathroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
            
    if "knife" in used_items:
        secrettunnel(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        visited_rooms.append("secret tunnel")

def kitchen_panel(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    if "knife" not in used_items:
        input("I press on the panel and it shifts just a bit, doesn't do much more. It'll have to come off the wall if I wanna get behind it. Should be something around here I can use to break the seal.")
        door_choice = input(f"{Fore.BLUE}What would you like to do?\nUSE   BACK{Style.RESET_ALL}\n").lower()
        while door_choice != "back":
            if door_choice == "use" and len(inventory)>0:
                use_choice = input(f"{Fore.BLUE}What would you like to use on the wall panel? {inventory}{Style.RESET_ALL} \n").lower()
                doorStat = isLocked ("kitchen panel", "knife", use_choice, inventory, used_items)
                if doorStat:
                    input("Perfect. This knife ougtta do the job. I slip the blade into the crack between the wall and the panel. It comes loose with a waft of damp, stale air. It's a tunnel. What kinda pervert house...")
                    bathroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
                else:
                    input("Damn. Gonna be tougher than I thought. Might need to look around more.")
                    door_choice = input(f"{Fore.BLUE}What would you like to do?\nUSE   BACK{Style.RESET_ALL} \n").lower()
            elif door_choice == "use" and len(inventory)==0:
                print("Nothing in my pockets. I'll have to remember this when I find something useful.")
                door_choice = input(f"{Fore.BLUE}What would you like to do?\nUSE   BACK{Style.RESET_ALL}\n").lower()
            
            else:
                print("What did you type?")
                door_choice = input(f"{Fore.BLUE}What would you like to do?\nUSE   BACK{Style.RESET_ALL}\n").lower()

        if door_choice == "back":
            kitchen(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
            
    if "knife" in used_items:
        secrettunnel(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        visited_rooms.append("secret tunnel")

def bathroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    input(f"\n{Fore.RED} THE BATHROOM {Style.RESET_ALL}")
    input("The door didn't even have to open half way before the smell to hit me. Bleach. Must've been been buckets of it to burn my nose hairs this bad. Once my eyes stopped watering, I could finally see the room in its entirety.")
    input("A one-window bathroom as shoddily constructed as a student's murder-mystery code assignment. Uneven walls, exposed plumbing, and a leaky sink. Ugh.")
    if "bathroom" not in visited_rooms:
        visited_rooms.append("bathroom")
    action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  MOVE  NOTES   BACK\n{Style.RESET_ALL}").lower()
    if action =="look":
        look_choice = input(f"{Fore.BLUE}What would you like to look at? \n WINDOW   WALLS   PLUMBING   BACK\n{Style.RESET_ALL}").lower()
        while look_choice != "back":
            if look_choice == "window" and "troutWhen" in npc_tracker:
                input("It's open, probably to deal with the bleach aroma. If they moved in here days ago, like Trout mentioned, then this can't be the same cleaning job from the AirBnb hosts. No... It's gotta be more recent.")
                input("Much more recent.")
                if "A strong bleach smell in the bathrom indicates a very recent cleaning job." not in notes_taken:
                    print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                    notes_taken.append("A strong bleach smell in the bathrom indicates a very recent cleaning job.")
                look_choice = input(f"{Fore.BLUE}What would you like to look at? \n WINDOW   WALLS   PLUMBING   BACK\n{Style.RESET_ALL}").lower()

            elif look_choice == "window" and "troutWhen" not in npc_tracker:
                input("It's open, probably to deal with the bleach aroma. Would AirBnb hosts use THIS much chemical to clean a bathroom, with new guests coming in so soon? I would hate to see what happened in here if that's the case.")
                input("No, can't be the case. There must be something else here.")
                if "A strong bleach smell in the bathrom indicates a very recent cleaning job." not in notes_taken:
                    print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                    notes_taken.append("A strong bleach smell in the bathrom indicates a very recent cleaning job.")
            
                look_choice = input(f"{Fore.BLUE}What would you like to look at? \n WINDOW   WALLS   PLUMBING   BACK\n{Style.RESET_ALL}").lower()

            elif look_choice == "walls":
                input("They certainly did a number on this paint job. Drips of off-white paint on every surface. Streaky roller marks from floor to ceiling. There's one squarish-patch of drywall that's a slightly different color.")
                look_choice = input(f"{Fore.BLUE}What would you like to look at? \n WINDOW   WALLS   PATCH   PLUMBING   BACK\n{Style.RESET_ALL}").lower()
            elif look_choice == "patch":
                secret_door(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
            elif look_choice == "plumbing":
                input("A pretty standard fair plumbing job. Pex on the sink, chrome on the tub, that sorta thing. Messy finishing, but, I guess, functional. There is one thing that sticks out, literally and figuratively.")
                input("About a half inch of CPVC pokes out of the wall, uncapped, open to all the bathroom elements. Or... opening the bathroom to all the pipe elements. What sorta plumbing job is that...")
                if "There is an uncapped and unexplained pipe in the wall of the bathroom." not in notes_taken:
                    print(f"{Fore.GREEN}You have added this to your notes.{Style.RESET_ALL}")
                    notes_taken.append("There is an uncapped and unexplained pipe in the wall of the bathroom,")
                look_choice = input(f"{Fore.BLUE}What would you like to look at? \n WINDOW   WALLS   PLUMBING   BACK\n{Style.RESET_ALL}").lower() 

            else:
                print("...try that again...")
                look_choice = input(f"{Fore.BLUE}What would you like to look at? \n WINDOW   WALLS   PLUMBING   BACK\n{Style.RESET_ALL}").lower()

        if look_choice == "back":
            bathroom_door(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

    if action == "notes":
        print("Alright, alright. I gotta take a time out, collect my thoughts.")
        check_stats(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

    if action == "move":
        if "secret tunnel" in visited_rooms:
            move_choice = input(f"{Fore.BLUE}Where would you like to go? \nBEDROOM   TUNNEL   BACK\n{Style.RESET_ALL}").lower()
            if move_choice == "bedroom":
                bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
            elif move_choice =="tunnel":
                secrettunnel(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
            elif move_choice == "back":
                bathroom_door(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        else:
            move_choice = input(f"{Fore.BLUE}Where would you like to go? \nBEDROOM   BACK\n{Style.RESET_ALL}").lower()
            if move_choice == "bedroom":
                bedroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
            elif move_choice =="back":
                bathroom_door(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

def kitchen(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    input(f"\n{Fore.RED} THE KITCHEN {Style.RESET_ALL}")
    input("So this is where all of the square footage went in this AirBnb. I'm impressed.")
    input("Spacious, lots of counterspace, windows, cabinetry to the ceiling but enough wall space for some art. Certainly the nicest room I've seen so far. And maybe the most interesting part of the kitchen is my new suspect making use of it. Why don't I see what's cooking.")
    if "kitchen" not in visited_rooms:
        visited_rooms.append("kitchem")
    action = input(f"{Fore.BLUE}What would you like to do?\n LOOK  TALK  MOVE  NOTES\n{Style.RESET_ALL}").lower()
    if action != "move":
        if action == "look":
            look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   COUNTERS   WALLS   BACK\n{Style.RESET_ALL}").lower()

            while look_choice != "back":
                if look_choice == "counters":
                    location = "counters"
                    counter_contents = ["spatula", "ladle", "knife", "bowl", "napkins"]
                    input("Formica, new. Plenty of gadgets on there, I guess laid out so our coding chef here can make quicker work of his dish. Let's see what we've got here.")
                    take_object(counter_contents, location, inventory)
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   COUNTERS   WALLS   BACK\n{Style.RESET_ALL}").lower()

                elif look_choice == "person":
                    input("He's hard at work, stirring here, chopping there. All with his back to me, so I can't quite grok what he's cooking, but I know it smells good.")
                    input("His focus is unbroken when I walk in. He's stress cooking, I'm sure of it, and while I hope it doesn't throw off his flavor game, I wouldn't mind if it tripped him up on the interrogation front.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   COUNTERS   WALLS   BACK\n{Style.RESET_ALL}").lower()

                elif look_choice == "walls":
                    input("Slightly grease-stained, HGTV Grey, figures.")
                    input("Lots of cabinets, though. Tools, pots, pans, all hanging from hooks for easy access. Stock images of scenery framed in tasteful spaces. But...")
                    if "bathroom" in visited_rooms:
                        input("There it is again. Another loose drywall panel, just like the one in the bathroom. Either these hosts need a handy man or something odd is going on here.")
                    else:
                        input("There's an odd panel of drywall over there. Looks like it's been patched and repatched, but recently loosened again.")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \n PERSON   COUNTERS   WALLS   PANEL   BACK\n{Style.RESET_ALL}").lower()

                elif look_choice == "panel":
                    kitchen_panel(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

                else:
                    print("What was that? Type it again!")
                    look_choice = input(f"{Fore.BLUE}What would you like to look at? \nPERSON   COUNTERS   WALLS   BACK\n{Style.RESET_ALL}").lower()

            if look_choice == "back":
                kitchen(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        if action == "talk":
            if "Xavier" not in npcs_spoken:
                npcs_spoken.append("Xavier")

            input("I decide it's my time to interject: 'Whatcha cookin?'")
            input(f"{Fore.LIGHTBLACK_EX}Chili. It'll probably be done in... 10 minutes?{Style.RESET_ALL}")
            input("'You still hungry on a night like this? With a body in your living room?'")
            input("He turns from the stove to look at me, takes a lick off his tasting spoon.")
            input(f"{Fore.LIGHTBLACK_EX}It's not my living room.{Style.RESET_ALL}")
            nextStep = input(f"{Fore.BLUE}Pick a topic to talk about,\n WHO   WHAT   WHY   BACK\n{Style.RESET_ALL}").lower()
            Xavier_dialogue(nextStep, notes_taken, inventory, visited_rooms, npcs_spoken, npc_tracker, used_items)

        else:
            print("What does that even mean? Let's try this all again.")
            kitchen(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)


    elif action == "move":
        move_choice = input(f"{Fore.BLUE}Where would you like to go? \nDINING   BACK\n{Style.RESET_ALL}").lower()
        if move_choice == "dining":
            diningroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        elif move_choice == "back":
            kitchen(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
        else:
            print("What was that? Type it again!")
            move_choice = input(f"{Fore.BLUE}Where would you like to go? \nDINING   BACK\n{Style.RESET_ALL}").lower()
        
def secrettunnel(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    print("tunnel")
    input(f"\n{Fore.RED} THE TUNNEL {Style.RESET_ALL}")

def start_mystery(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items):
    input("Figures...")
    input("I'm curled up in bed, cozier than a grandma in her bunny slippers on Christmas morning. I even kissed my cockapoo goodnight for God's sake, and I get a call.")
    input("Another coding class gone sour. Three students, two TAs, and a lecturer under one roof, taking their final test. Their first face-to-face meeting and, for one of them, their last. Now I've gotta go and straighten out the details.")
    input("...")
    input("It's gonna be a long night.\n")

    print(f"\n{Fore.RED} CODE RED MYSTERIES {Style.RESET_ALL}presents...")
    input(f"{Fore.BLUE} THE CASE OF THE TA TERMINATOR {Style.RESET_ALL}\n")

    input("The flatfoots are already stationed outside the AirBnb by the time I roll up, standing around like a bunch of unused variables in a begginner's CS1 project. I spot the chief leaning against her cruiser.")
    input("I ask her what's on everyone's mind. 'What's the situation in there, chief?' \nShe sighs, pulls out a pack of cigs from her shirt pocket.")
    input(f"{Fore.LIGHTBLACK_EX}One dead, five suspects. Victim up and keeled over with sudden flu-like symptoms.{Style.RESET_ALL}")
    input("'And that's grounds for a murder investigation? The flu?'")
    input(f"{Fore.LIGHTBLACK_EX}Get in there, start asking around. You'll see it ain't so cut and dry, detective.\nWe've got the perimeter covered, you just have to go in and figure out who to book. \nOnce you've spoken to all the suspects, gather us up in the living room and make your case. Easy right?{Style.RESET_ALL}")
    input("'As python.' I chuckle. She takes a drag. Figures.")
    input("I guess that's my cue to get the investigation started.\n")
    livingroom(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)

inventory  = []
visited_rooms = []
npcs_spoken = []
npc_tracker =[]
notes_taken = []
used_items = []

start_mystery(inventory, visited_rooms, npcs_spoken, notes_taken, npc_tracker, used_items)
#actions you can take: Look, Talk, Take, Use
#Rooms: Living room, bedroom, bathroom, kitchen, dining room, patio
#NPCs: Chloe, Ofelia, Trout, Xavier, Julia