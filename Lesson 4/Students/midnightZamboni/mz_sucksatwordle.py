import random
'''
6.) Now let's connect it all together and make our "game loop"
    - First, select a word and reveal it to the player
    - In a while loop, you must do the following:
        - Show the absentee list to the player
        - Take a guess as an input
        - Validate that guess, and keep requesting input until the player provides a valid guess
        - Remember: Only valid guesses contribute to guess count
        - End the game on a correct guess
        - Otherwise, keep playing until they've made 6 guesses
'''
def select_word (words):
    chosenIndex = random.randrange(0, len(words))

    return words[chosenIndex]

def guess_validator(guess, abesntees):
        
        if len(guess) != 5:
            print("Five letters pls")
            return False
        
        if not guess.isalpha():
            print("only letters pls")
            return False
        
        else:
            return True

def try_guess(answer, guess, absentees):
    if answer == guess:
        return True, word_match(answer, guess)
    
    elif guess_validator(guess, absentees):
        for i in range (len(answer)):
            if guess[i] not in answer:
                absentees.append(guess[i])

        return False, word_match(answer, guess)
    
    else:
        return False, word_match(answer, guess)



def word_match (answer, guess):
    dashesList = ["-", "-", "-", "-", "-"]
    
    if len(guess) == 5:
        for i in range(len(answer)):
            if guess[i] == answer[i]:
                dashesList[i] = guess[i]
            elif guess[i] in answer:
                dashesList[i] = guess[i].lower()

    
    outcome = "".join(dashesList)

    return outcome

def run_Wordle (answer, turnCount, absentees):
    
    guess = input("Guess Word:    ").upper()
    guess_Attempt, guess_result = try_guess(answer, guess, absentees)

    while not guess_validator(answer, absentees):
        print("Guesses must be a string of FIVE LETTERS.")
        guess = input("Guess word:    ").upper()

        return False

    if guess_Attempt and turnCount <=6 :
        print(guess_result)
        print(f"Congratulations! The answer was {word_Answer}. You won after {turnCount} turns.")

        return True
        

    
    elif turnCount == 6:
        print(guess_result)
        print(f"You've taken your 6 turns and have failed. The answer was {word_Answer}.")
        
        return False

    else:
        print(guess_result)
        print(absentees)

        return False
    
    

    

five_letter_words = ['ANIMA', 'TURCO', 'VOLAR', 'FOUND', 'PAVIN', 'BEEST', 'ATMID', 'VACUA', 'AGHAN', 'DAZED', 'SALMI', 'NARKS', 'MOHOS', 'TAMES', 'DUKHN', 'HICHT', 'DINTS', 'PATEL', 'FLUTE', 'HEYGH']


absentee_List = []
word_Answer = select_word(five_letter_words)
turnCount = 1

base = run_Wordle (word_Answer, turnCount, absentee_List)
turnCount += 1

while turnCount <= 6 and not base:
    base = run_Wordle (word_Answer, turnCount, absentee_List)
    turnCount += 1