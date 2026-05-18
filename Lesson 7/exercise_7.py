'''
Exercise 7: Turn-Based RPG

Premsie: Use classes to create and modify the state of custom game objects

Today, we'll be making a basic simulation of turn-based rpg combat using classes to hold game data.
Our scope for today will be the creation of a single battle between the player and a Slime enemy.
Each turn, the player will use input to select an action from among two options: "Attack" and "Execute"
Attack will deal damage to the enemy based on player and enemy stats. "Execute" has a random chance to
insta-kill the enemy, and is more likely to succeed when enemies have reduced health.
Then, the enemy attacks the player, simply doing damage. If the player's health reaches 0, you lose.
If the enemy's health reaches 0, you win. The player will always attack first.

1.) For this assignment, you'll be required to create an use at minimum the following classes and 1 enum:
    
    1a.) enum Action
        - Has 2 values: Attack and Execute
    
    1b.) class Stats
        - This a property-only class that will, at minimum, contain info on
          Attack, Defense, Max HP, and Execution Chance values
        - Give some thought to what numbers you'll use to represent these values.
            - Will they all be integers? How large will the numbers be? What values should you decide first?
    
    1c.) class Entity
        - Parent class of the Player and Enemy
        - Contains a Stats object property called "baseStats"
        - Contains a "currentHP" property
        - Contains a "name" property

        - It's constructor should take a Stats object as a parameter
            - It will save the provided stats object into "baseStats"
            - Then set currentHP to the value of the stats' maxHP

        - Create a member function called GetCurrentStats()
            - For now, this will just return the saved "baseStats" value
            - Use this whenever you want to do calculations with Entity stats (like in the next func)

        - Enity has function for taking damage
            - This function should take 2 parameters: another entity and the Action selected by opponent
            - By comparing stats, this function will reduce currentHP depending on the Action
                - So attack is just a pure stat comparison
                - Execute is a dice roll that may or may not lead to damage depending on the Enity's currentHP
                  and Execution Chance stat
            - The formulas are up to you to decide and balance. You can always rework them later.
            - Return the amount of damage taken
    
    1d.) class Player
        - Inherits from Entity
        - Later we can add things like items to the player. For now, that's it
    
    1e.) class Enemy
        - Inherits from Entity
        - Later, we can imagine this may contain AI calculations. For now, that's it

2.) Initialize Objects and Game
    - Create variables for the Player and Slime objects
        - Provide the stats used to initialize them
    - Request the player name their character
    - Give some preamble and announce that a battle is about to begin

3.) Create the Battle Loop
    - Define a function called StartBattle() that takes two parameters, the Player and an Enemy
    - It should return who won
    - While both the Player and Enemy have health over 0, simulate battle turns
    - On each turn do the following:
        - Show Player and Enemy HP totals
        - [Bonus] - Say something funny about the Player or Enemy randomly, perhaps based on currentHP
        - Ask the player what Action they'd like to pick
        - Damage the enemy based on the selection and announce the damage result
        - If the enemy dies, exit the battle and declare the Player the winner (return)
        - Otherwise, have the enemy damage the Player
        - If the player dies, exit the battle and declare the Enemy the winner (return)

4.) Connect it all
    - After initializing your game, call StartBattle() and announce victory or game over depending on the winner
    - Ask the player if they'd like to play again

Bonus 1.) Enemies from Without
            - Let's say that rather than a slime defined in code, we want text files to define enemy names
              and stats. This way, you don't need code to change enemy stats
            - Create a new file called slime.txt
                - In that file, put each of its stats on a separate line
            - Create a function that will read a given text file and return a Stats object reflective of
              that file's contents
            - Call that function on Slime.txt to get the slime's stats and use those for initialization

Bonus 2.) Everybody Wants to Be... My Enemy
            - Now, we don't just want a slime to be the only enemy you can battle
            - Make 3 more .txt files for different enemies
                - They must all have different stats and different names
                - Make sure the enemy name is a value in all text files if it's not already
            - Randomly select one enemy file use for initialization
            - Make sure your output properly shows the enemy name and stats
'''

