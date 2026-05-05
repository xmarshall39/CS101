import time

# [0, 1, 2, 3, 4, 5]
def add(num, times):
    for i in range(1, times):
        num += 1
    return num
def addFiveWhile(num):
    i = 0
    while i < 5:
        x += 1
        i += 1
    while True:
        if i >= 5:
            break
        x += 1
        i += 1

def tellJoke():
    jokeNum = input("Which joke would you like to read? 1, 2, or 3 \n")
    if jokeNum == "1":
        jokeKnock = input("Knock knock. \n")
        jokeWho = input("Europe. \n")  
        jokeWait = print("... \n")
        time.sleep(1)
        print("No, you're a poo!")
    if jokeNum == "2":
        jokeKnock = input("Knock knock. \n")
        jokeWho = input("Oink Oink. \n")  
        jokeWait = print("... \n")
        time.sleep(1)
        print("Are you a pig or are you an owl?!?!")
    if jokeNum == "3":
        jokeKnock = input("Knock knock. \n")
        jokeWho = input("Bella. \n")  
        jokeWait = print("... \n")
        time.sleep(1)
        print("Bella not-a-work so I knock-a on da door!")

def retellJoke():
    ans = input("Would you like to read this joke one more time? Yes or No \n")


    if ans == "Yes":
        tellJoke();
        print("Goodbye!")
    else:
        print("Goodbye!")

tellJoke()
retellJoke()

        