#text-based adventure game
#player starts up tech company
#company can be successful or fail depending on user's choices
#needs a loop, conditional statements, variables, functions
#comments, structure, and must be functional
import random

print(" ")
print("Welcome to Startup Superstar!")
print("In this game you are a startup owner who is trying to become the next big thing.")
print("This game is choose-your-adventure styled, so choose wisely!")
print("Be careful! You start with $25,000 but it can run dry very quickly if you don't act wisely.")
print("Running out of money or your team getting unhappy will cause the game to end!")
print("You win by reaching 100,000 downloads on your app.")
print(" ")

funding = 25000 #startup capital
team_morale = 1 #team is slightly happy
downloads = 1000 #some people already support the project

while True:
    if funding < 0:
        print("Your ran out of money! Game over.")
        break #end loop if user is out of money
    if team_morale <= -10:
        print("Your team is too unhappy and quit. Game over.")
        break #end loop if team is too unhappy
    if downloads < 0:
        print("Your startup ran out of support. Maybe next time?")
        break #end loop if there aren't enough supporters
    if downloads >= 100000:
        print("You win! Your startup is a massive success. Well played!")
        break #end loop because user wins!
    if team_morale < -5:
        morale = "Dangerously Low"
    elif team_morale < 0:
        morale = "Low"
    elif team_morale == 0:
        morale = "Neutral"
    elif team_morale > 5:
        morale = "Extremely High"
    elif team_morale > 0:
        morale = "High"
    print("Funding: " + str(funding) + " | Downloads: " + str(downloads) + " | Morale: " + str(morale))
    question = random.randint(1,10) #picks one of ten questions to ask the user
    if question == 1:
        q1 = str(input("""Your startup company has been recognized by Elon Musk as extremely promising. Do you:
    A) Respond to Elon Musk and ask for money
    B) Thank Elon Musk for the praise
    C) Say Nothing
    D) Tell Elon to stick to Tesla
                    """))
        if q1.upper() == "A":
            print("Elon does not appreciate your funding, and criticizes your team. Morale lowers.")
            team_morale -= 1
        elif q1.upper() == "B":
            print("Elon appreciates the gratitude, and decides to invest in your company.")
            funding += 100000
        elif q1.upper() == "C":
            print("Your silence allows for Elon's praise to sink in, landing you some new users.")
            downloads += 2000
        elif q1.upper() == "D":
            print("Elon doesn't like the criticism and tells future investors to pull out. However, fans love it and you get new users as a result.")
            downloads += 10000
            funding -= 25000
        else:
            print("Invalid input. Skipping...")
    elif question == 2:
        q2 = str(input("""You promised users an early build of the startup, but it isn't ready yet. Do you:
    A) Tell users to wait and promise a quality product
    B) Release the startup with the bugs
    C) Force your team to work overtime to release the quality product on time
    D) Stay silent and continue working on the product
                       """))
        if q2.upper() == "A":
            print("Some users don't like having to wait longer after the promised release date and stop following the startup.")
            downloads -= 250
        elif q2.upper() == "B":
            print("Lots of people download the app but the bugs make the app unusable and heavy criticism follows.")
            downloads += 5000
            team_morale -= 2
        elif q2.upper() == "C":
            print("The product is released and it is very good. Lots of people like the product and investors throw their money at you. However, the developers are now overworked and tired.")
            downloads += 7500
            team_morale -= 3
            funding += 10000
        elif q2.upper() == "D":
            print("Fans, confused by no response from the developers, get angry and stop waiting for the product. Investors pull out.")
            funding -= 5000
            downloads -= 500
        else:
            print("Invalid input. Skipping...")
    elif question == 3:
        q3 = str(input("""Your startup has been gaining a lot of popularity recently. Do you:
    A) Run a lot of ads to increase hype even more
    B) Start putting more ads inside of the app
    C) Collaborate with famous artist Drake in a TV commercial
    D) Start a TikTok account to reach the younger audience
                       """))
        if q3.upper() == "A":
            print("Potential users are converted with the highly convincing advertisements.")
            funding -= 5000
            downloads += 10000
        elif q3.upper() == "B":
            print("Users, frustrated by the amount of advertisements inside your app, delete it from their phones.")
            funding += 5000
            downloads -= 10000
        elif q3.upper() == "C":
            print("Not enough people see the advertisement as people don't watch TV anymore. On the plus side, at least you met Drake!")
            funding -= 7500
            team_morale += 3
        elif q3.upper() == "D":
            print("The younger audience loves your account! They make fun of it a lot but it converts many new users.")
            downloads += 5000
        else:
            print("Invalid input. Skipping...")
    elif question == 4:
        q4 = str(input("""You are invited to a product showcase in Las Vegas with your team, but it coincides with a QnA session you are meant to have with loyal customers. Do you:
    A) Attempt to make both the showcase and QnA
    B) Leave the team behind to do the QnA while you go to the product showcase
    C) Bring the entire team to Vegas for the showcase
    D) Stay in the office for the QnA session
                       """))
        if q4.upper() == "A":
            print("You cannot make both and end up missing both sessions.")
            funding -= 5000
            team_morale -= 1
        elif q4.upper() == "B":
            print("Both sessions go very well, securing new funding and users! However, your team is very upset you went to Vegas and made them stay behind in the office.")
            funding += 5000
            team_morale -= 5
            downloads += 7500
        elif q4.upper() == "C":
            print("The QnA session is left unmanned and many fans are frustrated. However, the showcase goes well and you secure massive funding.")
            funding += 25000
            downloads -= 5000
        elif q4.upper() == "D":
            print("You secure a loyal fanbase and many new users, but the investors are livid that you skipped their showcase.")
            funding -= 10000
            downloads += 10000
        else:
            print("Invalid input. Skipping...")
    elif question == 5:
        q5 = str(input("""Your users are requesting you add AI to your startup, but your team doesn't know how. Do you:
    A) Ignore the users and their requests
    B) Tell them you don't know how to implement AI
    C) Force the developers to learn how to implement AI
    D) Hire new developers who know how to implement AI into the startup
                       """))
        if q5.upper() == "A":
            print("Users are annoyed at the lack of a proper response and leave the project.")
            downloads -= 5000
        elif q5.upper() == "B":
            print("Users are satisfied with the response, however, people criticize the inexperienced developers.")
            team_morale -= 3
        elif q5.upper() == "C":
            print("The users are very happy with the AI implementation! However, the team is unhappy after having to watch so many mind numbing videos.")
            team_morale -= 2
            downloads += 5000
        elif q5.upper() == "D":
            print("The users are happy with the successful AI implementation and the new developer team has a fresh morale.")
            downloads += 5000
            team_morale = 0
        else:
            print("Invalid input. Skipping...")
    elif question == 6:
        q6 = str(input("""Your senior developer's parents have passed away but the startup is about to release a major update. Do you:
    A) Allow him time off and step in to do his job temporarily
    B) Allow him time off and let the other workers take the lead
    C) Don't allow him time off due to the crucial update
    D) Fire him for asking and hire a better developer
                       """))
        if q6.upper() == "A":
            print("The developer is very relieved but you can't do his job as well as him so the update has some minor bugs.")
            downloads -= 2500
            team_morale += 2
        elif q6.upper() == "B":
            print("The developer is very happy and the inexperienced junior developers try to take charge, but they are very unprepared.")
            downloads -= 5000
            team_morale += 2
        elif q6.upper() == "C":
            print("The senior developer is very unhappy and gossips about you to the junior developers. However, the product is a success.")
            downloads += 10000
            team_morale -= 3
        elif q6.upper() == "D":
            print("You hire a better developer who can do the job very well. The fans are very pleased with the better product but some of your employees are starting to be unsettled.")
            downloads += 15000
            team_morale -= 1
        else:
            print("Invalid input. Skipping...")
    elif question == 7:
        q7 = str(input("""Famous artist Kanye West wants to collab with your startup but his public image is somewhat controversial. Do you:
    A) Do the collab but try to teach Kanye how to improve his public image
    B) Do the collab gratefully
    C) Don't do the collab and call out Kanye
    D) Leave Kanye on read and never respond to his request
                       """))
        if q7.upper() == "A":
            print("Many Kanye fans download your app as a result, but since you disrespected Kanye, he charges you double.")
            funding -= 50000
            downloads += 20000
        elif q7.upper() == "B":
            print("Many Kanye fans download your app because of the collab.")
            funding -= 25000
            downloads += 20000
        elif q7.upper() == "C":
            print("Kanye fans start mass reporting you for disrespecting their idol. You gain the respect of some small investors.")
            funding += 10000
            downloads -= 7500
        elif q7.upper() == "D":
            print("Kanye assumes you are busy and retracts his offer. Nothing major happens.")
        else:
            print("Invalid input. Skipping...")
    elif question == 8:
        q8 = str(input("""A suspicious company offers to buy a major share of your company and help fund your project. Do you:
    A) Accept the offer gratefully
    B) Accept the offer after doing a thorough background check
    C) Decline the offer respectfully
    D) Report the suspicious company to the SEC
                       """))
        if q8.upper() == "A":
            print("The suspicious company buys a major share into your company. You get a lot of funding but some users delete the app over suspicions of spyware being installed.")
            funding += 7500
            downloads -= 2500
        elif q8.upper() == "B":
            print("The suspicious company turns out to operated in Russia but there are no imminent signs of danger, so you accept the offer anyways.")
            funding += 5000
        elif q8.upper() == "C":
            print("The CEO is frustrated but understands. Nothing happens.")
        elif q8.upper() == "D":
            print("The company is livid after finding out you tried to report them! Many other investors pull out after hearing this news.")
            funding -= 15000
        else:
            print("Invalid input. Skipping...")
    elif question == 9:
        q9 = str(input("""Your fans want you to set up a meet n greet in New York City, but prices for the space needed are very expensive. Do you:
    A) Plan it anyways
    B) Cancel plans due to the price
    C) Plan it but move it to Baltimore, which has cheaper spaces
    D) Fundraise from your fans to raise money
                       """))
        if q9.upper() == "A":
            print("Your fans have a lot of fun and you have many new users! However, the bank account looks a bit dire after the event.")
            funding -= 25000
            downloads += 10000
        elif q9.upper() == "B":
            print("Your fans are angry that you cancelled their event! At least your funding looks good.")
            downloads -= 10000
        elif q9.upper() == "C":
            print("You don't have any fans in Baltimore! Maybe you should've listened to the fans.")
            funding -= 15000
        elif q9.upper() == "D":
            print("You successfully raise the money needed, although some comes from out of pocket. The event is a blast!")
            funding -= 10000
            downloads += 10000
        else:
            print("Invalid input. Skipping...")
    elif question == 10:
        q0 = str(input("""A rival company releases a feature that looks suspiciously close to one you were planning. Do you:
    A) Let it go
    B) Call them out on it publicly
    C) Release your unfinished product immediately to rival them
    D) Take them to court
                       """))
        if q0.upper() == "A":
            print("You let it go, since yours wasn't finished yet. Users go to the rival company as their prodcut is better.")
            downloads -= 5000
        elif q0.upper() == "B":
            print("Your fans attack their company, and their fans come over to you. A massive success in your books.")
            downloads += 5000
        elif q0.upper() == "C":
            print("It looks like you tried to copy them! Now your fans leave as they think you released a copied product that was inferior to the rival one.")
            downloads -= 10000
        elif q0.upper() == "D":
            print("You sue them and all of their earnings are now yours. They must also unrelease their product.")
            downloads += 2500
            funding += 25000
        else:
            print("Invalid input. Skipping...")
