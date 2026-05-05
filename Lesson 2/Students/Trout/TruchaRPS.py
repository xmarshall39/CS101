import random
import time
import math

def RPS():
    print("You should really know better than to challenge a master rock paper scissors player")
    time.sleep(1)
    print("rock")
    time.sleep(0.4)
    print("paper")
    time.sleep(0.4)
    print("scissors")
    time.sleep(0.4)
    print("shoot!")
    time.sleep(1)
    
    
    movelist = ["rock", "paper", "scissors"]
    move = input("Form your hand into any of the typical RPS signs, 1 for Rock, 2 for paper, and 3 for scissors \n")
    
    cpu_index = random.randint(0,2) 
    cpu_move = movelist[cpu_index]
    print (f"It seems the master champion ultimate RPS player has morphed their hand into a {cpu_move}")

    if move == cpu_move:
        print("well this is just embarassing")
        
    if move == movelist[0] and cpu_move == movelist[1]:
        print("the hand covers yours, you are consumed infinitely by grief")
    if move == movelist[0] and cpu_move == movelist[2]:
        print("you CRUSH the master ultimate champion's hand in cold blood, congratulations")
    if move == movelist[1] and cpu_move == movelist[0]:
        print("you cover around the champion master's hand with your warm touch, you fall in love")
    if move == movelist[1] and cpu_move == movelist[2]:
        print("The master champion does a cutesy motion with his hand like he's cutting you with it, your hand splits, very gore")
    if move == movelist[2] and cpu_move == movelist[0]:
        print("Dick move, it seems your oponent has just straight up hit you in the face and ran away")
    if move == movelist[2] and cpu_move == movelist[1]:
        print("Instead of turning your hand into a scissor liek a normal person, you bite onto the Master champion's hand, he lets out a slight moan")


RPS()