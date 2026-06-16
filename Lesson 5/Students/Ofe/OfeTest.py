'''
Warm Up:
1.) Create a function that takes in a word and returns a string with all vowels [a, e, i, o u] removed.
- A For loop and the string member function join() may help you solve this problem.
- Make sure your solution works for both uppercase and lowercase vowels
'''
vowels = ["a","e","i","o","u"]

def check(word):
    newWord = []
    for letter in word:
        if letter.lower() not in vowels:
            newWord.append(letter)
    
    return "".join(newWord)

word = input()

print(check(word))