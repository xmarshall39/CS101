import random
from .. import word_match

words_list = []
size_target = 20
five_letter_words = []

with open("../words_alpha.txt", encoding="utf-8") as f:
    while line := f.readline():
        if len(word := line.rstrip()) == 5:
            five_letter_words.append(word.upper())
    if len(five_letter_words) < size_target:
        print(f"Size target too large, only {len(five_letter_words)} words in the file")
    i = 0
    while i < size_target:
        word = five_letter_words[random.randint(0, len(five_letter_words) - 1)].upper()
        if word not in words_list:
            words_list.append(word)
            i += 1

print(words_list)


