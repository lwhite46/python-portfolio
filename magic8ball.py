#magic 8 ball
import random
import time

print("""
Welcome to Magic 8 Ball!
Ask any yes or no question and recieve a 100 percent accurate answer!
""")

responses = ['Definitely', '100%', 'I feel confident', 'Signs point to yes', 'I think so', 'Results hazy', 'Unclear', 'Unsure', 'Maybe', "I don't know", 'No', 'Negative', 'Signs point to no', 'Definitely not', 'Under no circumstances', 'Affirmative', 'By all means', 'Never', 'No way']


while True:
    list_num = random.randint(1,15)
    user_question = str(input("Please enter a yes or no question: "))
    print(" ")
    if user_question.endswith("?") == True:
        print("You asked: " + user_question + " ")
        print("Shake... ")
        time.sleep(1)
        print("Shake... ")
        time.sleep(1)
        print("Shake... ")
        time.sleep(1)
        print("The MAGIC 8 BALL says: " + str(responses[list_num]) + " ")
        print(" ")
    else:
        print("ERROR: You did not ask a question, or it didn't end in a question mark. ")
        print(" ")
    play_again = str(input("Would you like to play again? (y/n) "))
    if play_again.upper() == "Y" or play_again.upper() == "YES":
        print("Great! Ask another question!")
        print(" ")
    elif play_again.upper() == "N" or play_again.upper() == "NO":
        print(" ")
        print("Quitting... ")
        print(" ")
        break
    else:
        print(" ")
        print("ERROR: Invalid input. Shutting down... ")
        print(" ")
        break
