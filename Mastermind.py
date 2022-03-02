# < Project Mastermind >
# < Kazi Islam >
# < pd - 7 >


# requirement(70) : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# additional tasks: 1, 4, 6


# import randint
from random import randint


# print a welcome message with beautiful borders
name = input("What is your name?")
print('''
 _______________________________
|                               |
|           WELCOME             |
|_______________________________|
'''
      )
welcome = '''
 ________________________________________________________________________________
|                                                                                | 
|   to a game of mastermind. In this game the computer will be selecting four    |
|   number in random from 1 through 6. You will have tries depended on the       |
|  diffuculty level that you chose. easy = 15 med = 10, hard = 8 to get pattern  |
|  of the numbers. After each guess the computer will output what numbers you    |
|      got correct and the number of spots the digits are in. Good Luck!         |
|________________________________________________________________________________|
'''
print("Welcome", name + ",", welcome)


# this picks random 4 digit number form 1 to 6 not repeating
solution = []
while len(solution) != 4:
    number = randint(1, 6)
    if number in solution:
        continue
    else:
        solution.append(number)



# this creates a new variable and stores the random
# number generted before in here for later purposes
new_variable = []
for i in solution:
    new_variable.append(i)

# if u wann test the game then remove the #
# print(new_variable)

# this keep record of the plyers moves
moves = []

# this asks the user for a diffuculty level
level = input("What diffculty do you wanna play on: easy, medium, hard")
if (level == "easy"):
    guess = 15
if (level == "medium"):
    guess = 10
if (level == "hard"):
    guess = 8

# this makes the game running untill condition is met
game = True
while (game == True):

# this are variables that stores all values for correct
# position and number and guess
    correct_numbers = 0
    correct_spots = 0
    for i in range(len(new_variable)):
        solution[i] = new_variable[i]

# this asks the user for a input and turns the input into a interger
# (I had to research this up)
    user_input = input("Please enter 4 numbers of your choice: ")
    moves.append(user_input)
    user_input = list(map(int, user_input))

# this makes sure all the numbers that the user puts is an interger
    for i in range(len(user_input)):
        user_input[i] = int(user_input[i])
    print(user_input)

# this sees if the user input matches the numbers and ups the
# the guess by one if user input doesnt match all the numbers
    if user_input != solution:
        guess -= 1

# if guess goes to zero it ends the game and user looses
    if guess == 0:
        print('''
     _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
    |                                                   |
    |       You Lost. The corrct answer was:            |
    |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
       '''
              , solution
        )
        break
    print()

# this compares the user input with the numbers to
# and ends the loop if it matches making the user win
    if user_input == solution:
        print('''
     _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
    |                                                   |
    |      You Won. Congrats. The corrct answer was:    |
    |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
       '''
          , solution
    )
        break
    print()

# this compares the each and every number and checks
# which one is in the correct spot
    for i in range(len(new_variable)):
        if new_variable[i] == user_input[i]:
            correct_spots += 1

# this checks for correct number regardless of the position
    for i in range(len(new_variable)):
        for j in range(len(user_input)):
            if user_input[j] == new_variable[i]:
                correct_numbers += 1
                solution[i] = "x"
                user_input[j] = "y"

# this print out all the end statement
    print("You got", correct_spots, "correct places")
    print("You got", correct_numbers, "numbers correct")
    print("You have", guess, "guess left")
    print(moves)
    print()
