import random
import time

number = random.randint(1, 100)

def intro():
    print("May I ask you for your name? ")
    name = input()
    print(name +", we are going to play a game. I am thinking of a number between 1 and 100")
    
    if (number%2 ==0):
        x = 'even'

    else:
        x = 'odd'

    print("\nThis is an {}number".format(x))
    time.sleep(.5)
    print("Go ahead. Guess!!")

def pick():
    guessesTaken = 0
    while guessesTaken < 6:
        time.sleep(.25)
    enter = input("Guess:")

    try:
        guess = int(enter)
        if guess <= 100 and guess >=1:
            guessesTaken = guessesTaken+1
            if guess<number:
                print("The guess of the number that you have enter is too low")
            if guess>number:
                print("The guess of the number that you have entered is too high")
            if guess != number:
                time.sleep(.5)
                print("Try again!!")
            if guess==number:
                break
        
        if guess > 100 and guess < 1:
            print("Silly goose, that number isn't is the range ")
            time. sleep(.25)
            print("Enter a number between 1 and 100")

    except:
        print("I don't think that"+enter+"is a number. Sorry")
    
    if guess == number:
        print("Good job, {}! You guessed my number in {} guesses".format(name,guessesTaken))




