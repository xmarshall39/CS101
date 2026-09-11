
'''
Exericse 6: *The Dictionary We Have At Home*
For today's assignment, you'll be using file parsing and dictionaries to make a small tool that allows a user
to type a word and lookup its definition.

1.) Use the following link to download the English to Spanish dictionary you'll be using for this assignment
    Place it in the same folder as your solution .py file: 
    https://raw.githubusercontent.com/mananoreboton/en-es-en-Dic/refs/heads/master/src/main/resources/dic/en-es.xml
   
    - More information on the file's contents can be found here: 
    https://github.com/mananoreboton/en-es-en-Dic

2.) Use the file's contents to populate a dictionary used for looking up information on english words
    - Note that there's more information in the file than just the definition.
    - This should only be done ONCE when the program runs


3.) Prompt the user for input until they type "/quit" (becuase "quit" is in the dictionary)
    - If the user types a word not in either dictionary, alert them and ask again
    - If the user types a word present in the dictionary, show the definition and ask again
    - If the user types "/quit" say goodbye and end your program

4.) Add a command to find interlingual homographs (words spelled the same in two languages)
    - If the user types "/ih" or "/interlingual-homographs", show them a set of all homographs
      between Spanish and English (it should print out a few hundred)
    - The set should be calculated ONCE right after importing the dictonaries

4.) Add a "/history" command that's accepted when asking for input
    - By typing "/history" the user should be able to see every word they've searched in the past
      and how many times they've searched it
    
Bonus 1.) Filter the "/ih" command by starting letters according to the following format
    - If the user ends the "/ih" or "/interlingual-homographs" command with a "-", use all
      characters that follow as a search filter. 
    - For example, typing "/ih-a" will show homographs starting with 'a' and "/ih-ahz" will show
      homographs starting with 'a', 'h', and 'z'

Bonus 2.) (Potential) False Cognates
    - There are 3 types of interlingual homophones (AFAIK). Loanwords, Cognates, and False Cognates.
      We'd need to understand entymological origin to differentiate between loanwords and cognates, and
      this dataset doesn't contain that. But we CAN identify likely false cognates from the provided context
    - Your task is to find out how and label those False Cognates when printing out the IH list

Bonus 3.) Better definitions and more content.
    - In the provided file are contents from the Oxford English Dictionary:     
    https://raw.githubusercontent.com/sujithps/Dictionary/refs/heads/master/Oxford%20English%20Dictionary.txt
    - This dictionary contains better defintions and additional information for English words
    - Your task is to use the Oxford definitions whenever possible instead of those provided by the EN-ES dict
    - Additionally, please integrate at least one piece of extra information from the Oxford dict into your
      dictionary tool. For example, language of origin. 
      Maybe you can use this to distinguish cognates from loanwords?



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