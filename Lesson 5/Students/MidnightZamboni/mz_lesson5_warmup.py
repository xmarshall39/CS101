'''
Warm Up:
1.) Create a function that takes in a word and returns a string with all vowels [a, e, i, o u] removed.
- A For loop and the string member function join() may help you solve this problem.
- Make sure your solution works for both uppercase and lowercase vowels
'''
# Now do consonants :)
# wowie >:)
# now do a backflip :)   (:   :)
# lmao

def remove_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    newword = []
    for i in range(len(word)):
        if word[i] not in vowels:
            newword.append(word[i])
    
    return "".join(newword)

def remove_consonants(word):
    vowels = ["a", "e", "i", "o", "u"]
    newword = []
    for i in range(len(word)):
        if word[i] in vowels:
            newword.append(word[i])
    
    return "".join(newword)

playerWord = input("Give me a heckin word: ").lower()

print("I took your vowels")
print(remove_vowels(playerWord))
