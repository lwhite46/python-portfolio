#slots machine

import random
import time

slots_output = ["🤑", "😂", "👴", "😡", "7"]
chips = 100


print(" ")
print("===== Welcome to the 3-Slot machine =====")
print(" ")
print("Slot Machine Symbols: [🤑] [😂] [7] [😡] [👴]")
print(" ")
print("You have 100 credits. You pick how much you bet.")
print(" ")
print("Press 'S' to spin and 'Q' to quit.")

while True:
    if chips >= 10:
        print(" ")
        print("Chips: " + str(chips))
        print(" ")
        user_input = str(input("Spin the slots? (S/Q): "))
        print(" ")
        if user_input.upper() == "S":
            try:
                bet_amount = int(input("Please enter your bet amount: "))
                print(" ")
                if bet_amount <= chips:
                    chips -= bet_amount
                    print("Spinning... ")
                    time.sleep(2)
                    print(" ")
                    slot1 = slots_output[random.randint(0,4)]
                    slot2 = slots_output[random.randint(0,4)]
                    slot3 = slots_output[random.randint(0,4)]
                    print(slot1 + " | " + slot2 + " | " + slot3)
                    print(" ")
                    if slot1 == "7":
                        if slot2 == "7":
                            if slot3 == "7":
                                print("Congratulations! You won the jackpot! ")
                                print("+" + str(bet_amount * 20) + " chips ")
                                chips += bet_amount * 20
                            else:
                                print("Congratulations! You got two 7s. ")
                                print("+" + str(bet_amount * 5) + " chips ")
                                chips += bet_amount * 5
                        elif slot3 == "7":
                                print("Congratulations! You got two 7s. ")
                                print("+" + str(bet_amount * 5) + " chips ")
                                chips += bet_amount * 5
                        else:
                            print("Congratulations! You got one 7. ")
                            print("+" + str(bet_amount * 2) + " chips ")
                            chips += bet_amount * 2
                    elif slot2 == "7":
                        if slot3 == "7":
                            print("Congratulations! You got two 7s! ")
                            print("+" + str(bet_amount * 5) + " chips ")
                            chips += bet_amount * 5
                        else:
                            print("Congratulations! You got one 7. ")
                            print("+" + str(bet_amount * 2) + " chips ")
                            chips += bet_amount * 2
                    elif slot3 == "7":
                        print("Congratulations! You got one 7. ")
                        print("+" + str(bet_amount * 2) + " chips ")
                        chips += bet_amount * 2
                    else:
                        print("Unfortunately, you didn't find any 7 this time. Try again! ")
                else:
                    print("You cannot afford that. Try a lower number or leave. ")
            except:
                print(" ")
                print("ERROR: Please enter a number. ")
        elif user_input.upper() == "Q":
            print("==== Thank you for playing. ====")
            print(" ")
            print("Final Chip Total: " + str(chips))
            print(" ")
            break
        else:
            print("ERROR: Invalid input. ")
    else:
        print(" ")
        print("ERROR: Insufficient funds. You must leave the slots machine. ")
        print(" ")
        break
