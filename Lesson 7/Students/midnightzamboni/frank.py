import re

file = open("frankenstein.txt", "r", encoding="utf-8")

wordCounter= {}


while True:
    frankLine = file.readline()
    lineWords = frankLine.split()
    for word in lineWords:
        strippedWord = word.strip(".,-'\"_ ( ) ;?!")
        match = re.match("^[a-zA-Z0-9_]*$", word)
        if not match:
            continue
        strippedWord = match.group().lower()
        if strippedWord not in wordCounter:
            wordCounter[strippedWord] = 1
        elif strippedWord in wordCounter:
            wordCounter[strippedWord] += 1

    if not frankLine:
        break

userWord = input("Find your word (type \\quit to quit):\n").lower()

while userWord != "\\quit":
    if userWord in wordCounter:
        print(f"{userWord} is in 'Frankenstein' {wordCounter[userWord]} times.")
        userWord = input("Find your word (type \\quit to quit):\n").lower()
    elif userWord == "\\quit":
        print("Goodbye.")
        file.close()
    else:
        print("Try again!")
        userWord = input("Find your word (type \\quit to quit):\n").lower()
