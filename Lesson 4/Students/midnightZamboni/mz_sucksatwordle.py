import random
import time
import colorama
from colorama import Fore, Style

colorama.init()

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
                absentees.add(guess[i])

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

        return False, guess_result

    if guess_Attempt and turnCount <=6 :
        '''print(Fore.GREEN + guess_result)'''
        print(f"{Style.RESET_ALL}Congratulations! The answer was {Fore.GREEN}{word_Answer}{Style.RESET_ALL}. You won after {turnCount} turns.")

        return True, guess_result
        

    
    elif turnCount == 6:
        '''print(guess_result)'''
        print(f"You've taken your 6 turns and have {Fore.RED} failed. {Style.RESET_ALL} The answer was {Fore.GREEN}{word_Answer}{Style.RESET_ALL}.")
        
        return False, guess_result

    else:
        colorResult = []
        for i in range(len(guess_result)):
            if guess_result[i].isupper():
                colorResult.append(f"{Fore.LIGHTGREEN_EX}{guess_result[i]}{Style.RESET_ALL} ")
            elif guess_result[i].islower():
                colorResult.append(f"{Fore.LIGHTYELLOW_EX}{guess_result[i]}{Style.RESET_ALL} ")
            else:
                colorResult.append(f"{Fore.LIGHTBLACK_EX}{guess_result[i]}{Style.RESET_ALL} ")
        

        for i in range(len(colorResult)):
            print(colorResult[i], end ='', flush=True)
            time.sleep(0.5)
            

        print(f"\n{absentees}")


        return False, guess_result
    

def results_line(attempt):
    results = ["-", "-", "-", "-", "-"]
    for i in range(len(attempt)):
        if attempt[i].isupper():
            results[i] = "*"
        if attempt[i].islower():
            results[i] = "/"
    
    line = " ".join(results)
    return line

language_choice = input("Choose a language: ENGLISH   FRENCH   GERMAN\n").lower()
five_letter_words = [] 

if language_choice == "english":
    dicto = open("words_alpha.txt", "r", encoding="utf-8")
    allWords = dicto.readlines()
if language_choice == "french":
    dicto = open("francais.txt", "r", encoding="utf-8")
    allWords = dicto.readlines()
if language_choice == "german":
    dicto = open("wordlist-german.txt", "r", encoding="utf-8")
    allWords = dicto.readlines()

for line in allWords:
    if len(line) == 6:
        five_letter_words.append(line.strip("\n").upper())

#five_letter_words = ['ANIMA', 'TURCO', 'VOLAR', 'FOUND', 'PAVIN', 'BEEST', 'ATMID', 'VACUA', 'AGHAN', 'DAZED', 'SALMI', 'NARKS', 'MOHOS', 'TAMES', 'DUKHN', 'HICHT', 'DINTS', 'PATEL', 'FLUTE', 'HEYGH']




absentee_Set = set()
word_Answer = select_word(five_letter_words)
turnCount = 1

base, guess = run_Wordle (word_Answer, turnCount, absentee_Set)
turnCount += 1

attempts = []
attempts.append(guess)


while turnCount <= 6 and not base:
    base, guess = run_Wordle (word_Answer, turnCount, absentee_Set)
    turnCount += 1
    attempts.append(guess)

print("Here are your results:")
for i in range(len(attempts)):
    print(results_line(attempts[i]))

print("* = Correct letter, correct place \n / = correct letter, wrong place \n - = wrong letter")
dicto.close()
