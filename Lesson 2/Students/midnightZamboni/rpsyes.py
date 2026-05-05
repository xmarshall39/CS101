import time
import random
  
def rockPaperScissors():
    print ("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissors...")
    time.sleep(1)
    print("SHOOT!")
    
    options = [1, 2, 3, 3]
    
    playerPull = input ("Type your move! \n")
    compPull = options[random.randint(0,len(options)-1)]

    return playerPull, compPull

def compLoses( playerW, compL):
    if playerW == "Paper" and compL == 1:
        print ("I choose Rock!")
        time.sleep(1)
        print("You win!")
        return True

    if playerW == "Scissors" and compL == 2:
        print ("I choose Paper!")
        time.sleep(1)
        print ("You win!")
        return True

    if playerW == "Rock" and compL == 3:
        print ("I choose Scissors!")
        time.sleep(1)
        print ("You win!")
        return True

    else:
        return False

def compWins(playerL, compW):
    if playerL == "Scissors" and compW == 1:
        print ("I choose Rock!")
        time.sleep(1)
        print ("I win!")
        return True

    if playerL == "Rock" and compW == 2:
        print ("I choose Paper!")
        time.sleep(1)
        print ("I win!")
        return True

    if playerL == "Paper" and compW == 3:
        print ("I choose Scissors!")
        time.sleep(1)
        print("I win!")
        return True
    
    else:
        return False
    
def itsADraw(playerD, compD):
    if playerD == "Rock" and compD == 1:
        print ("I choose Rock!")
        time.sleep(1)
        print ("It's a draw!")

    if playerD == "Paper" and compD == 2:
        print ("I choose Paper!")
        time.sleep(1)
        print("It's a draw!")

    if playerD == "Scissors" and compD == 3:
        print ("I choose Scissors!")
        time.sleep(1)
        print ("It's a draw!")
        
def restartRPS(playerScore, computerScore):
    replayAns = input("Would you like to play again? Yes or No \n")
    if replayAns == "Yes":
        fullGame(playerScore, computerScore)
    else:
        print("Ok. Here are our final scores! \n Player: " + str(playerScore) + " Computer: " + str(computerScore) + " \n See ya next time!")

def fullGame(playerScore, computerScore):
    player, comp = rockPaperScissors()
    losses = compLoses(player, comp)
    wins = compWins(player, comp)
    itsADraw(player, comp)
    if losses:
        playerScore += 1
    elif wins:
        computerScore +=1
    
    restartRPS(playerScore, computerScore)

    return playerScore, computerScore

playerWins = 0
computerWins = 0

fullGame(playerWins, computerWins)