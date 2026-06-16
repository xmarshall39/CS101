
 

file = open("words_alpha.txt", "r", encoding="utf-8")
lists = file.readlines()
five_letter_words = []
for line in lists:
    line = line.strip("\n").upper()
    if len(line) == 5:
        five_letter_words.append(line)

absent_list = []
import random
import word_match
import time


new_list = ["index 0", "index 1", "index 2", "index 3"]
first_elm = new_list[0]
last_elm = new_list[len(new_list) - 1]


def selectword(wordList):
    ans = random.randint(0, len(wordList) - 1) and len(wordList) == 5
    return wordList[ans]
    


def guess_validator(wordGuess):
    if wordGuess.isalpha() and len(wordGuess) == 5 and wordGuess in five_letter_words:
        return True 
    else:
        return False
    # return wordGuess.isalpha() and len(wordGuess) == 5
    #^ this will work because return gives boolean results
#not adding anything to wordNone rn

def try_guess(target, guess, absent):
    if target == guess:
        return True 
    else:
        absent.append(guess)
        return False
    




def newFunc(parm1, parma2, optional1 = "hello", optional2 = 100):
    print(optional1)
    print(optional2 * 1000)

#newFunc("hello", "boo", optional2=500)
#newFunc("hello", "boo", optional1="goodbye", optional2=500)

counter = 0
stupidMeter = 0 

ans = selectword(five_letter_words)

print("the most game of all games, Wordle.", flush=True)
time.sleep(2)
print(f"in 6 chances, guess a 5 letter word or explode... ", flush=True)
time.sleep(2.5)
print("and if you guess it wrong, you'll explode as well.", flush=True)
time.sleep(2)
print(f"\nReady...?", flush=True)
time.sleep(1)
print("GOo@oOo0ooo0")
time.sleep(1)

while counter < 6:
    print(f"\n\nYou still have {6 - counter} chance", flush=True)
    print(f"words you guessed: {absent_list}", flush=True)
    #print(f"One of the following words is selected: \n {five_letter_words}") 

    playerAns = input("\nGuess a 5 lettered word:\n").upper() 

    if playerAns in absent_list:
        print("\nDon't guess the same word twice you scoundrel", flush=True)
        time.sleep(1)
        stupidMeter += 5
        print(f"Stupid Meter: {stupidMeter} (plus one for each letter)", flush=True)
        time.sleep(2)
        continue 

    if guess_validator(playerAns) == True:
        print("\nLoading answer", flush=True)
        time.sleep(1)
        print(f"\nYOU GOT:{word_match.word_match(ans,playerAns)}\n(lower case = right letter, UPPER CASE = right placement)", flush=True) 
        time.sleep(2)
    else:
        print("\nGIVE ME SOMETHING VALID!", flush=True)
        time.sleep(1)
        stupidMeter += 1
        print(f"Stupid Meter: {stupidMeter}", flush=True)
        time.sleep(2)
        continue


    if try_guess(ans, playerAns, absent_list) == True:
        print("\nYou did it!!!", flush=True)
        break     
    else:
        print("Wrong answer... EXPLODE. Try again!", flush=True)
        counter += 1
        time.sleep(2)
        
print(f"\noh... well, I guess you can't try again. You're all out of body parts to explode with.", flush=True)
time.sleep(1)
print(f"The answer was {ans}. Let's play Wordle again in your next life!", flush=True)
time.sleep(1)
