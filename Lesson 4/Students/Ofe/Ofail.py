
import time
import random 
'''
for y in range(1,101):
    print(y)


while True:
    time.sleep(0.5)
    print("HELP THE TUCANS KILLING ME IT'S BOMBING ME AHHHHH")
    stop = input("say stop?\n")
    if stop == "stop": 
        break
     
    
''' 

trout = ["slooshed","dead to me","xavier aren't you","a chiwawa","stinkey","TROUT"]
num = [1,20,3,40,5,100]
firstElm = num[0]
lastElm = num[len(trout) - 1]
random_index = random.randint(0,len(trout) - 1)
print(f"you're {trout[random_index]}")