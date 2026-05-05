apple = "apple"

def printHello():
    fruit = "fruit"
    print("hello")
    print(apple)

'''
Adds 1 to the provided number. i should be an integer.
'''
def countUp(i):
    print(apple)
    if type(i) == int:
        i += 1
        print(apple)
        print("counting up " + str(i))
    else:
        print(apple)
        print("gimme a goddamn integer!!")


def killColi(): 
    i = 34.5
    print("OH NO COLI DIED")
    print(i*2) 


def coliBlowUp(AHHHHH):
    if AHHHHH == True: 
        print("coli has been blown UP")
    else:
        print("Coli has slightly survived... not really")


def takeName(n):
    print("This player's name is "+ str(n) + "." )
    

# I love calling functions!
# Wow this can be solved with prettier but sure man

print("hello world")
x = 7
print(x)
y = 6+5+x
print(y)
z = 2.1 * 0.7 
print(z)
b = "This is Chloe's String!"
print(b)


# DATA TYPES:
x = 7 # integer
y = 0.5 # float
yes = True #boolean - true or false
why = "why not" # string

# CONTAINER TYPES:
l = [1, 2, 3, 4, 5, 6, 7] # list: a list of things
s = {0, 2, 4, 6, 7} #set: all data unique

# Operators
# +, -, *, /, < , >, ==, ^

# ^btw is % an operator in python 
x = 5 * 5 / pow(3 + 8, 2)
y = 10000
x = y
print(x)
printHello()
countUp(8)
countUp("hello")
takeName("Joe")
takeName("julia") #:))
takeName("Back")
print(apple)
coliBlowUp(False)
print(apple)