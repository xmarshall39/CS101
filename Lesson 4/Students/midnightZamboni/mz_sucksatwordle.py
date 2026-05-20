'''
3.) [DO NOTHING] To help you, I wrote a function called word_match(). Here's how it works:
    - Determines and reports how close a word is to another (target) word
    - Accepts 2 parameters: a target word and a guessed word
    - Returns a string indicating the quality of a match. Here's how that would look with the target word "HORSE":
        - Every letter in "HORSE" not guessed correctly will be represented in the output by a '-'
            - So if I guess "BUNDT" the output will be "-----"
        - Every letter guessed that's present in the target word, but not in the correct position will be output in lowercase
            - So if I guess "THINK" the output will be "-h---"
        - Every letter guessed that's present and in the right location will appear as uppercase
            - So if I guess "HALLS" the output will be "H---s". Guessing horse will return "HORSE"
    - Was that confusing? Do the next step, and call word_match() a few times. It'll make sense.
'''

def word_match (answer, guess, extraParam = 100, anotherOne = 40):
    answer = answer.upper(); guess = guess.upper();
    dashesList = ["-", "-", "-", "-", "-"]
    
    if len(guess) != 5:
        print("Five letters pls")
        return ""
    if not guess.isalpha():
        print("only letters pls")
        return ""
    
    else:
        for i in range(len(answer)):
            if guess[i] == answer[i]:
                dashesList[i] = guess[i]
            elif guess[i] in answer:
                dashesList[i] = guess[i].lower()

    
    outcome = "".join(dashesList)

    return outcome
            


guess = input("guess word:    ")
print(word_match("HORSE", guess))




five_letter_words = ['ANIMA', 'TURCO', 'VOLAR', 'FOUND', 'PAVIN', 'BEEST', 'ATMID', 'VACUA', 'AGHAN', 'DAZED', 'SALMI', 'NARKS', 'MOHOS', 'TAMES', 'DUKHN', 'HICHT', 'DINTS', 'PATEL', 'FLUTE', 'HEYGH']
