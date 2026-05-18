def word_match(target, guess):
    target = target.upper(); guess = guess.upper();
    if len(target) != len(guess):
        print("Error: Target String and Guess String should be the same length!!")
        return ""
    result_list = ['-'] * len(guess)
    for i in range(len(guess)):
        if guess[i] == target[i]:
            result_list[i] = guess[i]
        elif guess[i] in target:
            result_list[i] = guess[i].lower()
    return "".join(result_list)

# This is a special if statement we can use to write code that runs only when executing this file directly
# This lets us run test code that gets ignored when imported
if __name__ == "__main__":
    '''
    word = input("Give me a 5 letter word")
    while len(word) != 5:
        word = input("Please make it 5 letters:")
    '''
    words = ["HORSE", "TROUT", "HAPPY", "MAKES", "ZUMBA", "QUIET", "HOUSE"]

    #for every word, try guessing every other word
    for target in words:
        print("\nTarget: " + target)
        for guess in words:
            print(word_match(target, guess) + f"\t({guess})")