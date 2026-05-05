import time
import random

def reverseString(string):
    return string[::-1]



#print(reverseString(greet))
print("hi")
time.sleep(1)

def something():
    ans = input("say something \n")
    if ans == "something":
        print(reverseString("noice \n"))
    else:
        print("what are you doing? say SOMETHING! \n")
        something()

something()

#didn't work^
#???? didn't change anything and it works now. Beofre it would say "something" on it's own instead of me inputing it 

ans = int(input("Thanks. And how old are you? \n"))
if ans > 20:
    print("wow, you're old! \n")
else:
    print("wow, you're a baby! \n")

'''
ans = input("")

if ans == "apple":
    print("Correct Answer")
'''


