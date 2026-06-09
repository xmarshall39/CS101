import random 
import word_match
import time

five_letter_words = ['ANIMA', 'TURCO', 'VOLAR', 'FOUND', 'PAVIN', 'BEEST', 'ATMID', 'VACUA', 'AGHAN', 'DAZED', 'SALMI', 'NARKS', 'MOHOS', 'TAMES', 'DUKHN', 'HICHT', 'DINTS', 'PATEL', 'FLUTE', 'HEYGH']


#num_words = len(five_letter_words)

def select_word(wordlist):
    index = random.randint(0,len(wordlist)-1)
    # print(wordlist[index])
    return wordlist[index]


def guessvalidator(guessedword):
    if guessedword.isalpha() and len(guessedword) == 5:
        #print(f"damn")
        return True
    else:
        #print(f"FUCK")
        return False
target_word = select_word(five_letter_words)

def try_guess()
    


guess = input("make a guess for the target word!")
if not guessvalidator(guess):
    print("Please provide a valid guess!!")

match = word_match.word_match(target_word, guess)
print(match)


#5.) Create a function called try_guess()
#    - Read the player's validated guess and report its correctness using word_match()'s output
 #   - This function accepts 3 parameters: a target word, a guessed word, and a absentee list
  #  - If the player guesses correct, return 2 values: True and output of word_match()
   #   - Add any guessed letters not present in the target word to the absentee list
    #   - Return False and the output of word_match()
