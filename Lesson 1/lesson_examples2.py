import time
import random

def reverseString(string):
    return string[::-1]

def functionWithReturn():
    return 5

def addSix(num):
    return num + 6

def addSeven(num):
    return addSix(num) + 1

def repeat_list(ls, numTimes):
    ret = []
    for i in range(numTimes):
        for x in ls:
            ret.append(x)
    return ret

y = 5
x = functionWithReturn()

#print(y == x)

y = addSix(y)
#print(y)

y = addSeven(y)
#print(y)

arr = [0, 1, 2, 3, 4]

#print(repeat_list(arr, 8))

name = input("Tell me your name: \n")
#print("Oh, " + name + " is a really...")

'''
print("Oh...")
time.sleep(2)
print(f"{name} is a really strange name")
time.sleep(2)
print("You should change it")
'''
randNum = random.randint(0, 2)
print(randNum)

name = "zamboni"
print(reverseString(name))