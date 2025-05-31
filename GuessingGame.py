#importing random to generate random int
import random

random_num= random.randint(0,10)
#creating booleans for while loops
correct = False
playAgain = True

print("Welcome to the Guessing Game, the computer picks a number and you must guess the number until you are correct ")

#First loop runs the entire game
while playAgain:
    number = int(input("From a range of 0-10, pick your guess: "))
    if number == random_num :
        print("You guessed correctly!")
    elif number != random_num :
        #Nested loop runs true if the number is incorrect or if the game is still running
        while not correct or playAgain:
            newGuess=int(input("Guess Again!: "))
            if newGuess == random_num:
                print("You guessed correctly!")
                #change boolean values when the number is guessed correctly and end inside loop
                correct = True
                playAgain = False
            else:
                #continue running game
                correct = False
        play = input("Would you like to play again? (Y/N) ")
        if play == 'Y':
            playAgain = True
            #if user want to continue game regenerate a new random int
            random_num = random.randint(0, 10)
        elif play == 'N':
            #if user wants to stop the game stop outer loop
            playAgain = False
            print("Thanks for playing!")


