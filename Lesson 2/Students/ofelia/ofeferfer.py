import random
import time
'''
attack 
strike
rushdown
choose = random [attack, strike, rushdown]
'''
# This is the short version, essentially. You can't use it tho!
def win_or_lose(player, enemy):
    eval = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
    if eval[player][enemy] == -1:
        return "lose"
    if eval[player][enemy] == 0:
        return "tie"
    if eval[player][enemy] == 1:
        return "win"
'''


    if player != int:
        print("1 to 3 my good sir madam sir pal, try again")
        time.sleep(1)
        rock_papers_shoo()

  if player == "":
        print ("a number mate, do you know what a number is?")
        time.sleep(1)
        rock_papers_shoo()
'''
rps_names = ["1. ROCK", "2. PAPER", "3. SCISSORS"]

def again():
    responce = input ("would you like to play again? Yes or no \n")
    if responce.lower() == "yes":
        print("welp, time to resurrect... \n")
        time.sleep(2)
        rock_papers_shoo ()
    if responce.lower() == "no":
        print("damn... I'll see you never then \n")
        time.sleep(2)
        
    
def rock_papers_shoo():
    player = (input ("Will you choose 1. rock, 2. paper or 3. scissors? \nInput 1,2 or 3: \n"))
  
    player = int(player)
    enemy = random.randint(1,3) 

    print ("rock.... papers... shooo!!!!")
    time.sleep(2)
    print (f"your foe has chosen {rps_names[enemy-1]} !!")
    time.sleep(1)
    if player == enemy:
        print ("it's a tie! A TIE? unacceptable!!")
        time.print(1)
        print ("choose again! \n")
        time.sleep(2)
        rock_papers_shoo()
    if player == 1 and enemy == 2:
        print ("woah... you just blew that person up... you're amazing!")
    if player == 1 and enemy == 3:
        print ("winner! We have a winner! And it's not you...")
    if player == 2 and enemy == 1:
        print ("woah... you just blew that person up... you're amazing!")
    if player == 2 and enemy == 3:
        print ("winner! We have a winner! And it's not you...")
    if player == 3 and enemy == 1:
        print ("winner! We have a winner! And it's not you...")
    if player == 3 and enemy == 2:
        print ("woah... you just blew that person up... you're amazing!")
    time.sleep(2)
    again()

    

print ("\nColi is coming at you with a game of rock paper scissors! ")
time.sleep(1)
rock_papers_shoo()





