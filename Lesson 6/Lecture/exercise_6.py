
'''
Exericse 6: *The Dictionary We Have At Home*
For today's assignment, you'll be using file parsing and dictionaries to make a small tool that allows a user
to type a word and lookup its definition.

1.) Using the following links, download dictionaryorsomething.txt and spanishdict.txt. 
    Place it in the same folder as your solution .py file: 
    [LINK] [LINK]

2.) Use the files' contents to populate 2 dictionaries (1 for each language)
    where each key is a word from the dictionary and each value is a definition
    - Note that there's more information in the file than just the definition. Make sure you're pulling def only
    - Use the string member function split() to help solve this
        - You can split only a certain number of times: [LINK]
    - This should only be done ONCE when the program runs


3.) Prompt the user for input until they type "/quit" (becuase "quit" is in the dictionary)
    - If the user types a word not in either dictionary, altert them and ask again
    - If the user types a word present in the dictionary, show the definition and ask again
    - If the user types "/quit" say goodbye and end your program

4.) Add a command to find interlingual homographs (words spelled the same in both languages)
    - If the user types "/ih" or "/interlingual-homographs", show them a set of all homographs
      between Spanish and English (it should print out a few hundred)
    - The set should be calculated ONCE right after importing the dictonaries

4.) Add a "/history" command that's accepted when asking for input
    - By typing "/history" the user should be able to see every word they've searched in the past
      and how many times they've searched it
    

Bonus 1.) Add more content than just the definition.
    - Change the dictionary's values to be a list instead of a string
    - Make each element in the list strings containing the word's information
    - It might look like {"Palace": ["n", "pl", "An ornate building or whatever"]}

Bonus 2.) Filter the "/ih" command by starting letters according to the following format
    - If the user ends the "/ih" or "/interlingual-homographs" command with a "-", use all
      characters that follow as a search filter. In this case, we want to fiter our homographs


'''

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

def Room1():
    connected_rooms = ["Library", "Kitchen", "Ballroom"]
    selected_room = input(f"Choose a Room from this list: {connected_rooms}")
    if selected_room in connected_rooms:
        move_room(selected_room)
    print("Hi")
    move_room("Room2") # Room2()

def Library():
    print("Bye")