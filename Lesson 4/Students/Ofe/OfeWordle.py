five_letter_words = ['ANIMA', 'TURCO', 'VOLAR', 'FOUND', 'PAVIN', 'BEEST', 'ATMID', 'VACUA', 'AGHAN', 'DAZED', 'SALMI', 'NARKS', 'MOHOS', 'TAMES', 'DUKHN', 'HICHT', 'DINTS', 'PATEL', 'FLUTE', 'HEYGH']
import random
import word_match


new_list = ["index 0", "index 1", "index 2", "index 3"]
first_elm = new_list[0]
last_elm = new_list[len(new_list) - 1]


def selectword(wordList):
    ans = random.randint(0, len(wordList) - 1)
    return wordList[ans]
    


def guess_validator(wordGuess):
    if wordGuess.isalpha() and len(wordGuess) == 5:
        return True 
    else:
        return False
    # return wordGuess.isalpha() and len(wordGuess) == 5
    #^ this will work because return gives boolean results
#not adding anything to wordNone rn

def try_guess(target, guess, absent):
    sdf

'''
guess = input("Now try to guess the word!!")
if guess_validator(guess):
    print("Provided a valid word guess!!")
    
#im just writing this here while i remember don't falme me for doing extra stuff
# 6 8

while True: 
    print("guess the word!")
    if guess_validator() == True:
        break 


def randint(x, y):
    return 100

rand_num = randint(0, 100)
'''

# 1
selectword(five_letter_words)

print(f"One of the following words will be selected \n {five_letter_words}")

ans = selectword(five_letter_words)

# 2
'''
playerAns = input("give me a word from the list above.\n") #This is not what #2 is asking for # get dunked on atte. trout

if guess_validator(playerAns) == True:
    print("loading answer")
else: 
    print("Guess a word from the list only!")
'''


(word_match.word_match("Trout","event")) #replace the perameters later