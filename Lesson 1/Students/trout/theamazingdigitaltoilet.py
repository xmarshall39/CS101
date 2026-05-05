import time
import random
# love this


print("it's a nice day for a walk")
print("(you take a few steps, it seems every time you take a step you feel something approach)")
step = input("take another step, yes or no? \n")


def enocunter():
    print("you find youself in front of the creature")
    time.sleep(3)
    print("it seems to be asleep damn lazy ass")
    time.sleep(0.5)
    print("wanna poke it with a stick?")
    ans = input("yes or no \n")
    if ans == "yes":
        print("you shouldn't be poking people with sticks")
    if ans == "no" :
        print("thank you for not poking the creechur, it shall now sleep for a year")
        time.sleep(316536000)



enocunter()