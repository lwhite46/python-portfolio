#multiplication quiz - 5 questions

print("Welcome to the multiplication quiz!")
print("Answer these questions as best as you can.")
print("We will keep track of your score!")

import random
correct = 0
incorrect = 0
question_number = 1

while True:
    cont = str(input("Pick one - Continue (C) or quit (Q)"))
    if cont.upper() == "C" or cont.upper() == "CONTINUE":
        difficulty = str(input("Pick a difficulty - Easy (E), Medium (M), Hard (H), or Practice (P)"))
        if difficulty.upper() == "P" or difficulty.upper == "PRACTICE":
            print("At any time press 'Q' to end your endless session.")
            while True:
                num1 = random.randint(0,12)
                num2 = random.randint(0,12)
                ans = num1 * num2
                user_ans = str(input(str(num1) + " x " + str(num2) + " = ? "))
                if user_ans.upper() == "Q" or user_ans.upper() == "QUIT":
                    break
                elif int(user_ans) == int(ans):
                    print(" ")
                    print("Correct!")
                    correct += 1
                    print("Correct: " + str(correct) + " | Incorrect: " + str(incorrect))
                else:
                    print(" ")
                    print("Incorrect.")
                    incorrect += 1
                    print("Correct: " + str(correct) + " | Incorrect: " + str(incorrect))
        else:
            length = str(input("Pick a length - Short (S), Medium (M), Long (L)"))
            if difficulty.upper() == "E" or difficulty.upper() == "EASY":
                print("You selected 'EASY'. You will multiply numbers 1-5 together.")
                if length.upper() == "S" or length.upper() == "SHORT":
                    print("You selected 'SHORT'. Your quiz is 3 questions.")
                    for i in range(3):
                        print("Question " + str(question_number) + ":")
                        print(" ")
                        num1 = random.randint(0,5)
                        num2 = random.randint(0,5)
                        ans = num1 * num2
                        print(str(num1) + " x " + str(num2) + " = ")
                        print(" ")
                        user_ans = input(str(num1) + " x " + str(num2) + " = ? ")
                        question_number += 1
                        if int(user_ans) == int(ans):
                            print("Correct!")
                            print(" ")
                            correct += 1
                        else:
                            print("Incorrect.")
                            print(" ")
                            incorrect += 1
                    print("Correct: " + str(correct) + " | Incorrect: " + str(incorrect))
                elif length.upper() == "M" or length.upper() == "MEDIUM":
                    print("You selected 'MEDIUM'. Your quiz is 5 questions.")
                    for i in range(5):
                        print("Question " + str(question_number) + ":")
                        print(" ")
                        num1 = random.randint(0,5)
                        num2 = random.randint(0,5)
                        ans = num1 * num2
                        print(str(num1) + " x " + str(num2) + " = ")
                        print(" ")
                        user_ans = input(str(num1) + " x " + str(num2) + " = ? ")
                        question_number += 1
                        if int(user_ans) == int(ans):
                            print("Correct!")
                            print(" ")
                            correct += 1
                        else:
                            print("Incorrect.")
                            print(" ")
                            incorrect += 1
                    print("Correct: " + str(correct) + " | Incorrect: " + str(incorrect))
                elif length.upper() == "L" or length.upper() == "LONG":
                    print("You selected 'LONG'. Your quiz is 10 questions.")
                    for i in range(10):
                        print("Question " + str(question_number) + ":")
                        print(" ")
                        num1 = random.randint(0,5)
                        num2 = random.randint(0,5)
                        ans = num1 * num2
                        print(str(num1) + " x " + str(num2) + " = ")
                        print(" ")
                        user_ans = input(str(num1) + " x " + str(num2) + " = ? ")
                        question_number += 1
                        if int(user_ans) == int(ans):
                            print("Correct!")
                            print(" ")
                            correct += 1
                        else:
                            print("Incorrect.")
                            print(" ")
                            incorrect += 1
                    print("Correct: " + str(correct) + " | Incorrect: " + str(incorrect))
            elif difficulty.upper() == "M" or difficulty.upper() == "MEDIUM":
                print("You selected 'MEDIUM'. You will multiply numbers 1-12 together.")
                if length.upper() == "S" or length.upper() == "SHORT":
                    print("You selected 'SHORT'. Your quiz is 3 questions.")
                    for i in range(3):
                        print("Question " + str(question_number) + ":")
                        print(" ")
                        num1 = random.randint(0,12)
                        num2 = random.randint(0,12)
                        ans = num1 * num2
                        print(str(num1) + " x " + str(num2) + " = ")
                        print(" ")
                        user_ans = input(str(num1) + " x " + str(num2) + " = ? ")
                        question_number += 1
                        if int(user_ans) == int(ans):
                            print("Correct!")
                            print(" ")
                            correct += 1
                        else:
                            print("Incorrect.")
                            print(" ")
                            incorrect += 1
                    print("Correct: " + str(correct) + " | Incorrect: " + str(incorrect))
                elif length.upper() == "M" or length.upper() == "MEDIUM":
                    print("You selected 'MEDIUM'. Your quiz is 5 questions.")
                    for i in range(5):
                        print("Question " + str(question_number) + ":")
                        print(" ")
                        num1 = random.randint(0,12)
                        num2 = random.randint(0,12)
                        ans = num1 * num2
                        print(str(num1) + " x " + str(num2) + " = ")
                        print(" ")
                        user_ans = input(str(num1) + " x " + str(num2) + " = ? ")
                        question_number += 1
                        if int(user_ans) == int(ans):
                            print("Correct!")
                            print(" ")
                            correct += 1
                        else:
                            print("Incorrect.")
                            print(" ")
                            incorrect += 1
                    print("Correct: " + str(correct) + " | Incorrect: " + str(incorrect))
                elif length.upper() == "L" or length.upper() == "LONG":
                    print("You selected 'LONG'. Your quiz is 10 questions.")
                    for i in range(10):
                        print("Question " + str(question_number) + ":")
                        print(" ")
                        num1 = random.randint(0,12)
                        num2 = random.randint(0,12)
                        ans = num1 * num2
                        print(str(num1) + " x " + str(num2) + " = ")
                        print(" ")
                        user_ans = input(str(num1) + " x " + str(num2) + " = ? ")
                        question_number += 1
                        if int(user_ans) == int(ans):
                            print("Correct!")
                            print(" ")
                            correct += 1
                        else:
                            print("Incorrect.")
                            print(" ")
                            incorrect += 1
                    print("Correct: " + str(correct) + " | Incorrect: " + str(incorrect))
            elif difficulty.upper() == "H" or difficulty.upper() == "HARD":
                print("You selected 'HARD'. You will multiply numbers 1-25 together.")
                if length.upper() == "S" or length.upper() == "SHORT":
                    print("You selected 'SHORT'. Your quiz is 3 questions.")
                    for i in range(3):
                        print("Question " + str(question_number) + ":")
                        print(" ")
                        num1 = random.randint(0,25)
                        num2 = random.randint(0,25)
                        ans = num1 * num2
                        print(str(num1) + " x " + str(num2) + " = ")
                        print(" ")
                        user_ans = input(str(num1) + " x " + str(num2) + " = ? ")
                        question_number += 1
                        if int(user_ans) == int(ans):
                            print("Correct!")
                            print(" ")
                            correct += 1
                        else:
                            print("Incorrect.")
                            print(" ")
                            incorrect += 1
                    print("Correct: " + str(correct) + " | Incorrect: " + str(incorrect))
                elif length.upper() == "M" or length.upper() == "MEDIUM":
                    print("You selected 'MEDIUM'. Your quiz is 5 questions.")
                    for i in range(5):
                        print("Question " + str(question_number) + ":")
                        print(" ")
                        num1 = random.randint(0,25)
                        num2 = random.randint(0,25)
                        ans = num1 * num2
                        print(str(num1) + " x " + str(num2) + " = ")
                        print(" ")
                        user_ans = input(str(num1) + " x " + str(num2) + " = ? ")
                        question_number += 1
                        if int(user_ans) == int(ans):
                            print("Correct!")
                            print(" ")
                            correct += 1
                        else:
                            print("Incorrect.")
                            print(" ")
                            incorrect += 1
                    print("Correct: " + str(correct) + " | Incorrect: " + str(incorrect))
                elif length.upper() == "L" or length.upper() == "LONG":
                    print("You selected 'SHORT'. Your quiz is 10 questions.")
                    for i in range(10):
                        print("Question " + str(question_number) + ":")
                        print(" ")
                        num1 = random.randint(0,25)
                        num2 = random.randint(0,25)
                        ans = num1 * num2
                        print(str(num1) + " x " + str(num2) + " = ")
                        print(" ")
                        user_ans = input(str(num1) + " x " + str(num2) + " = ? ")
                        question_number += 1
                        if int(user_ans) == int(ans):
                            print("Correct!")
                            print(" ")
                            correct += 1
                        else:
                            print("Incorrect.")
                            print(" ")
                            incorrect += 1
                    print("Correct: " + str(correct) + " | Incorrect: " + str(incorrect))
    elif cont.upper() == "Q" or cont.upper() == "QUIT":
        print("Quitting...")
        break
    else:
        print("Invalid input. Please try again.")
