#name generator
#liam white

#init

#functions
def name_generator():
    print("Welcome to Sports Name Generator")
    print("Answer the questions to get your sports name")
    print("Answer exactly as put in apostrophe and use capital letters")
    ans = input("'Team' or 'Individual':")
    if ans == "Team":
        ans = input("'Use Hand' or 'Use Foot':")
        if ans == "Use Hand":
            ans = input("'Basketball' or 'Football':")
            if ans == "Basketball":
                print("Your name is 'LeBron'")
            elif ans == "Football":
                print("Your name is 'Patrick Mahomes'")
        if ans == "Use Foot":
            ans = input("'Tall' or 'Short':")
            if ans == "Tall":
                print("Your name is 'Cristiano Ronaldo'")
            elif ans == "Short":
                print("Your name is 'Lionel Messi'")
    elif ans == "Individual":
        ans = input("'Has Ball' or 'No Ball':")
        if ans == "Has Ball":
            ans = input("'Tennis' or 'Golf':")
            if ans == "Tennis":
                print("Your name is 'Serena Williams'")
            elif ans == "Golf":
                print("Your name is 'Tiger Woods'")
        elif ans == "No Ball":
            ans = input("'Water' or 'Land'")
            if ans == "Water":
                print("Your name is 'Micheal Phelps'")
            elif ans == "Land":
                print("Your name is 'Usain Bolt'")
    else:
        ans = input("You did not answer correctly. Would you like to 'restart' or 'exit'?")
        if ans == "Restart":
            name_generator()
        elif ans == "Exit":
            print("You selected 'Exit'. Shutting down...")
            return
        else:
            print("You made another mistake. Shutting down...")
            return

#main
name_generator()
