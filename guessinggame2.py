#init - liam white | random number game
import random
import time

#define user points
points = 100

#functions

def random_num():
    global points
    print(" ")
    print("---------------------------------")
    print("Welcome to Random Number Guesser!")
    print("You will need to guess a random number.")
    print("It costs points to play, so don't run out!")
    print("Easy [E] (1): 2, Medium [M] (2): 5, Hard [H] (5): 15, Impossible [I] (10): 150")
    print("---------------------------------")
    print(" ")
    print("Points total: " + str(points))
    time.sleep(1)
    dif = str(input("Please choose a difficulty. Easy (E), Medium (M), Hard (H), or Impossible (I)."))
    if dif == 'E':
        points = points - 1
        num = random.randint(1,5)
        for i in range(3):
            guess = int(input("Guess a number between 1 and 5: "))
            if num == guess:
                print("Correct. Maybe you should up the difficulty.")
                points = points + 2
                print(" ")
                print("Points: " + str(points))
                print(" ")
                time.sleep(1)
                break
            elif num != guess:
                if num > guess:
                    print("Too low!")
                elif guess > num:
                    print("Too high!")
                print("You got it wrong. " + str(2 - i) + " attempts remaining.")
                time.sleep(1)
    if dif == 'M':
        points = points - 2
        num = random.randint(1,10)
        for i in range(3):
            guess = int(input("Guess a number between 1 and 10: "))
            if num == guess:
                print("Correct!")
                points = points + 5
                print(" ")
                print("Points: " + str(points))
                print(" ")
                time.sleep(1)
                break
            elif num != guess:
                if num > guess:
                    print("Too low!")
                elif guess > num:
                    print("Too high!")
                print("You got it wrong. " + str(2 - i) + " attempts remaining.")

                time.sleep(1)
    if dif == 'H':
        points = points - 5
        num = random.randint(1,25)
        for i in range(3):
            guess = int(input("Guess a number between 1 and 25: "))
            if num == guess:
                print("Wow! You got it right!")
                points = points + 15
                print(" ")
                print("Points: " + str(points))
                print(" ")
                time.sleep(1)
                break
            elif num != guess:
                if num > guess:
                    print("Too low!")
                elif guess > num:
                    print("Too high!")
                print("You got it wrong. " + str(2 - i) + " attempts remaining.")
                time.sleep(1)
    if dif == 'I':
        points = points - 10
        num = random.randint(1,100)
        for i in range(5):
            guess = int(input("Guess a number between 1 and 100: "))
            if num == guess:
                print("Impossible! You must be cheating...")
                points = points + 150
                print(" ")
                print("Points: " + str(points))
                print(" ")
                time.sleep(1)
                break
            elif num != guess:
                if num > guess:
                    print("Too low!")
                elif guess > num:
                    print("Too high!")
                print("You got it wrong. " + str(4 - i) + " attempts remaining.")
                time.sleep(1)
    again()


def again():
    again = str(input("Would you like to try again (y/n?)"))
    if again == 'y':
        print(" ")
        print("Restarting...")
        time.sleep(1)
        random_num()
    else:
        print(" ")
        print("Terminating game...")
        print(" ")
        time.sleep(1)
        return


#main

random_num()
