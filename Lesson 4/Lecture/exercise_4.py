'''
Exercise 4: Wordle Pt.1
Objective: Get familiar with the basics of string comparison and manipulation
Today, we're gonna make a basic version of Wordle. If you haven't played before (or yet today)
a link to the web game can be found here: https://www.nytimes.com/games/wordle/index.html
The program we'll write today will randomly select a word from a mock "dictionary" of 5 letter words
and give the player 6 attempts at guessing the word correctly. The player will be told how many letters
they have correct and their positions. Characters not in the target word present in the player's guess
will be added to the absentee list, and the player won't be able to use those letters to guess.
Wordle has a lot of mechanics, so we'll be breaking this problem up into small chunks. This may
end up being a 2-session assignment, and that's okay!

Instructions are as follows:

0.) Copy this variable into your code:
five_letter_words = ['ANIMA', 'TURCO', 'VOLAR', 'FOUND', 'PAVIN', 'BEEST', 'ATMID', 'VACUA', 'AGHAN', 'DAZED', 'SALMI', 'NARKS', 'MOHOS', 'TAMES', 'DUKHN', 'HICHT', 'DINTS', 'PATEL', 'FLUTE', 'HEYGH']

1.) Create a function called select_word()
    - This function will accept one parameter: a list of words
    - A list of valid 5-letter words will be provided to you
    - This function will return a random word from that list
    - Why make this a function? Find out next week

1.) Create a function called guess_validator()
    - This function will evaluate if the player made a valid guess (return True or False)
    - The function must accept 2 parameters: a guessed word, and a absentee list
    - A guess is considered valid if it meets the following conditions:
        - The guess contains only letters from a-z
        - The guess is 5 letters long
        - For now, we WON'T worry about the guess being a valid english word

3.) [DO NOTHING] To help you, I wrote a function called word_match(). Here's how it works:
    - Determines and reports how close a word is to another (target) word
    - Accepts 2 parameters: a target word and a guessed word
    - Returns a indicating the quality of a match. Here's how that would look with the target word "HORSE":
        - Every letter in "HORSE" not guessed correctly will be represented in the output by a '-'
            - So if I guess "BUNDT" the output will be "-----"
        - Every letter guessed that's present in the target word, but not in the correct position will be output in lowercase
            - So if I guess "THINK" the output will be "-h---"
        - Every letter guessed that's present and in the right location will appear as uppercase
            - So if I guess "HALLS" the output will be "H---s". Guessing horse will return "HORSE"
    - Was that confusing? Do the next step, and call word_match() a few times. It'll make sense.

4.) To use word_match() import match.py at the top of your file
    - Try calling word_match() a few times to get a feel for how it works
    - I reccomend trying the same target word each time and fill in a few different gueses

2.) Create a function called try_guess()
    - Read the player's validated guess and report its correctness using word_match()'s output
    - This function accepts 3 parameters: a target word, a guessed word, and a absentee list
    - If the player guesses correct, return 2 values: True and output of word_match()
    - If the player guesses wrong, do the following:
        - Add any guessed letters not present in the target word to the absentee list
        - Return False and the output of word_match()

4.) Now let's connect it all together and make our "game loop"
    - First, select a word and reveal it to the player
    - In a while loop, you must do the following:
        - Show the absentee list to the player
        - Take a guess as an input
        - Validate that guess, and keep requesting input until the player provides a valid guess
        - Remember: Only valid guesses contribute to guess count
        - End the game on a correct guess
        - Otherwise, keep playing until they've made 6 guesses

Bonus 1.) Try changing your absentee list into a set object
            - More info on sets here: 
Bonus 2.) Add a splash of color
            - In Wordle, correct letters in correct positions are highlighted green,
              present letters in incorrect positions are highlighted yellow,
              and letters not present in the target word are grey
            - Using a library called Colorama, replicate this multi-color behavior
              when showing the result of word_match() to the player
            - I've been doing a lot of typing, so just lmk when you get here :)
Bonus 3.) Dramatic timing
            - Like in wordle, reveal correct letters one at a time, with a slight delay between reveals
Bonus 4.) Results
            - Show the results of your game in a grid of symbols, similar to the results you share with others
            - You could use something like (+, #, -) for (correct, almost, wrong) guesses
'''