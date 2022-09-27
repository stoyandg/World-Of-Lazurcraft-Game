#### IMPORTS ####
import time
from datetime import datetime
import csv
import pandas as pd
import getpass
import random
import sys

startTime = time.time()

def register_account():
    now = datetime.now()

    def distribute_skillpoints():
        global characterStartingSkills
        global characterStrength
        global characterAgility
        global characterIntelligence
        while True:
            try:
                characterStrength = int(input("How many points would you like to allocate to Strength?"))
                print("Your character's Strength is now set to ", characterStrength)
                break;
            except ValueError:
                print("Your answer can only be a number.")

        while True:
            try:
                characterAgility = int(input("How many points would you like to allocate to Agility?"))
                print("Your character's Agility is now set to ", characterAgility)
                break;
            except ValueError:
                print("Your answer can only be a number.")

        while True:
            try:
                characterIntelligence = int(input("How many points would you like to allocate to Intelligence?"))
                print("Your character's Agility is now set to ", characterIntelligence)
                break;
            except ValueError:
                print("Your answer can only be a number.")
        characterStartingSkills = characterStrength + characterAgility + characterIntelligence
        if int(characterStartingSkills) <= 5:
            print("Your character was successfully created.")
            time.sleep(2)
            print("Name: ", characterName)
            print("Date of birth: ", characterDateAndTimeOfBirth)
            print("Strength: ", characterStrength)
            print("Agility: ", characterAgility)
            print("Intelligence: ", characterIntelligence)
        else:
            print(
                "You spent more than 5 skill points, thus your character wasn't created! Please re-distribute NO more than 5 skill points accordingly.")
            time.sleep(2)
            distribute_skillpoints()

    print("Welcome to World of LazurCraft Character Creation panel!")

    time.sleep(1)

    ####CharacterName Creation
    characterName = input(
        "Please write down your character's name (it is recommended to use a 1-word name that starts with a capital letter for the best gaming experience.):")
    print("Your character's name has been set to " + characterName)

    time.sleep(1)
    ###Set Password + Confirm
    while True:
        characterPassword = getpass.getpass(prompt="Please set your password. Minimum password length is 6 characters and maximum password length is 20 characters.")
        if len(characterPassword) < 6:
            print("Make sure your password is at least 6 characters long.")
        elif len(characterPassword) > 20:
            print("Make sure your password is not longer than 20 characters.")
        else:
            print("Your password was set.")
            break

    time.sleep(1)

    while True:
        characterPasswordConfirm = getpass.getpass(prompt="Please write down your password once again to confirm it.")
        if characterPasswordConfirm != characterPassword:
            print("The passwords you've provided don't match.")
        else:
            print("Your password was successfully registered.")
            break

    time.sleep(1)

    characterQuestion = input(
        "Please set a secret question that will help you recover your password in case you forget it.")

    time.sleep(1)

    characterAnswer = input(
        "Please set an answer to the secret question. The question will be presented to you in case you forget your password.")

    time.sleep(1)
    while True:
        try:
            characterDateAndTimeOfBirth = datetime.strptime(
                input("Please select your character's date and time of birth. (Ex. 1997-11-06 16:00)"),
                '%Y-%m-%d %H:%M')
            break;
        except ValueError:
            print("Please abide to the format: YYYY-MM-DD HH:MM")

    print("Your character's date and time of birth has been set to", characterDateAndTimeOfBirth)

    time.sleep(1)

    print(
        "Your character starts as Level 1 and has 5 skill points to allocate between Strength, Agility and Intelligence. Choose wisely as you can only do this once.")

    time.sleep(2)

    # DISTRIBUTE SKILLPOINTS
    distribute_skillpoints()

    print("Welcome to World of Lazurcraft, ", characterName, " !")
    time.sleep(4)
    print("**DATE AND TIME**:", characterDateAndTimeOfBirth)
    time.sleep(3)
    print("**LOCATION**: A hospital in Burgas, Bulgaria")
    time.sleep(5)
    print("DOCTOR: Push harder, miss! Push harder!")
    time.sleep(3)
    print("RANDOM MOTHER: Ugh-...Ugh-..")
    time.sleep(4)
    print("**A FEW MOMENTS LATER**")
    time.sleep(5)
    print("DOCTOR: There it is-.. How are you going to call this lovely boy?")
    time.sleep(4)
    print("RANDOM MOTHER: I'll call him ", characterName)
    time.sleep(4)
    print("DOCTOR: That's such a beautiful name! I'm sure he'll make you proud!")
    time.sleep(4)
    print("RANDOM MOTHER: I hope he does.")
    time.sleep(4)
    print("**FAST FORWARDING TIME...**")
    time.sleep(4)
    print("**DATE AND TIME**: 12th July, 2010")
    time.sleep(3)
    print("**LOCATION**: Bench in front of Acho, Lazur.")
    time.sleep(3)
    print("You will now be sent to the starting screen where you can login with your newly created account.")
    time.sleep(3)
    characterSave = open("character.csv", 'w', encoding='UTF8', newline='')

    characterNameSave = [characterName]
    characterDateAndTimeOfBirthSave = [characterDateAndTimeOfBirth]
    characterStrengthSave = [characterStrength]
    characterAgilitySave = [characterAgility]
    characterIntelligenceSave = [characterIntelligence]
    characterQuestionSave = [characterQuestion]
    characterAnswerSave = [characterAnswer]

    writer = csv.writer(characterSave)
    writer.writerow(['Character Data'])
    writer.writerow(characterNameSave)  # Name
    writer.writerow(characterDateAndTimeOfBirthSave)  # DOB
    writer.writerow(characterStrengthSave)  # Strength
    writer.writerow(characterAgilitySave)  # Agility
    writer.writerow(characterIntelligenceSave)  # Intelligence
    writer.writerow(['Bench in front of Acho'])  # Location
    writer.writerow([1])  # Level
    writer.writerow([5])  # Coins
    writer.writerow([100])  # Reputation
    writer.writerow([characterPassword])  # Password
    writer.writerow([0])  # Played Time
    writer.writerow(characterQuestionSave)  # Secret Question
    writer.writerow(characterAnswerSave)  # Secret Answer

    characterSave.close()

def recover_account():
    loadsave = pd.read_csv("character.csv")
    characterName = loadsave.iloc[0, 0]  # Name
    characterDateAndTimeOfBirth = loadsave.iloc[1, 0]  # DOB
    characterStrength = loadsave.iloc[2, 0]  # Strength
    characterAgility = loadsave.iloc[3, 0]  # Agility
    characterIntelligence = loadsave.iloc[4, 0]  # Intelligence
    characterLocation = loadsave.iloc[5, 0]  # Location
    characterLevel = loadsave.iloc[6, 0]  # Level
    characterCoins = loadsave.iloc[7, 0]  # Coins
    characterReputation = loadsave.iloc[8, 0]  # Reputation
    characterPassword = loadsave.iloc[9, 0]  # Password
    characterPlayed = loadsave.iloc[10, 0]  # Played Time
    characterQuestion = loadsave.iloc[11, 0]  # Secret Question
    characterAnswer = loadsave.iloc[12, 0]  # Secret Answer
    print("Welcome to the World of Lazurcraft Recovery Panel!")
    time.sleep(2)
    while True:
        checkCharacterName = input("Please enter your character's name.")
        if checkCharacterName == characterName:
            print("Alright, entering recovery mode for ", characterName)
            time.sleep(2)
            print("The Secret Question for ", characterName, "is - ", characterQuestion)
            time.sleep(2)
            while True:
                checkCharacterAnswer = input("Please enter your character's secret answer")
                if checkCharacterAnswer == characterAnswer:
                    print("Alright. You can now set a new password for your character.")
                    while True:
                        characterPassword = getpass.getpass(prompt="Please set a NEW password. Minimum password length is 6 characters and maximum password length is 20 characters.")
                        if len(characterPassword) < 6:
                            print("Make sure your password is at least 6 characters long.")
                        elif len(characterPassword) > 20:
                            print("Make sure your password is not longer than 20 characters.")
                        else:
                            print("Your NEW password was set.")
                            break
                    while True:
                        characterPasswordConfirm = getpass.getpass(prompt="Please write down your NEW password once again to confirm it.")
                        if characterPasswordConfirm != characterPassword:
                            print("The passwords you've provided don't match.")
                        else:
                            print("Your NEW password was successfully set.")
                            endTimeSave = time.time()
                            totalPlayedNow = endTimeSave - startTime
                            characterPlayedNew = int(characterPlayed) + int(totalPlayedNow)
                            characterSave = open('character.csv', 'w', encoding='UTF8', newline='')
                            characterNameSave = [characterName]  # Name
                            characterDateAndTimeOfBirthSave = [characterDateAndTimeOfBirth]  # DOB
                            characterStrengthSave = ([characterStrength])  # Strength
                            characterAgilitySave = ([characterAgility])  # Agility
                            characterIntelligenceSave = ([characterIntelligence])  # Intelligence
                            characterLocationSave = [characterLocation]  # Location
                            characterLevelSave = ([characterLevel])  # Level
                            characterCoinsSave = ([characterCoins])  # Coins
                            characterReputationSave = ([characterReputation])  # Reputation
                            characterPasswordSave = ([characterPassword])  # Password
                            characterPlayedSave = ([characterPlayedNew])  # Total Played
                            characterQuestionSave = [characterQuestion]  # Secret Question
                            characterAnswerSave = [characterAnswer]  # Secret Answer

                            writer = csv.writer(characterSave)

                            writer.writerow(['Character Data'])
                            writer.writerow(characterNameSave)  # Name
                            writer.writerow(characterDateAndTimeOfBirthSave)  # DOB
                            writer.writerow(characterStrengthSave)  # Strength
                            writer.writerow(characterAgilitySave)  # Agility
                            writer.writerow(characterIntelligenceSave)  # Intelligence
                            writer.writerow(characterLocationSave)  # Location
                            writer.writerow(characterLevelSave)  # Level
                            writer.writerow(characterCoinsSave)  # Coins
                            writer.writerow(characterReputationSave)  # Reputation
                            writer.writerow(characterPasswordSave)  # Password
                            writer.writerow(characterPlayedSave)  # Time Played
                            writer.writerow(characterQuestionSave)  # Secret Question
                            writer.writerow(characterAnswerSave)  # Secret Answer

                            characterSave.close()
                            print("You'll now be sent to the starting screen where you can login with your NEW password.")
                            time.sleep(3)
                            return
        else:
            print("There's no character with this name. Please write down your character's name correctly.")
            continue

##LOGIN, REGISTER OR PASSWORD RECOVERY

while True:
    print("*** Welcome to World of Lazurcraft! Would you like to login in your account, register a new account or recover your lost password? ***")
    time.sleep(3)
    loginRegisterOrRecover = input("Type !login, !register or !recover")
    if loginRegisterOrRecover == "!login":
        loadsave = pd.read_csv("character.csv")
        characterName = loadsave.iloc[0, 0]  # Name
        characterDateAndTimeOfBirth = loadsave.iloc[1, 0]  # DOB
        characterStrength = loadsave.iloc[2, 0]  # Strength
        characterAgility = loadsave.iloc[3, 0]  # Agility
        characterIntelligence = loadsave.iloc[4, 0]  # Intelligence
        characterLocation = loadsave.iloc[5, 0]  # Location
        characterLevel = loadsave.iloc[6, 0]  # Level
        characterCoins = loadsave.iloc[7, 0]  # Coins
        characterReputation = loadsave.iloc[8, 0]  # Reputation
        characterPassword = loadsave.iloc[9, 0]  # Password
        characterPlayed = loadsave.iloc[10, 0]  # Played Time
        characterQuestion = loadsave.iloc[11, 0]  # Secret Question
        characterAnswer = loadsave.iloc[12, 0]  # Secret Answer


        ###### LISTS ######

        actionsList = ['!visitginko', '!visitgorskiq', '!visitprimo', '!visittheliar', '!visitcrazyblondewoman',
                       '!visitshitthrower', '!visitthejupiter', '!visithatman', '!runfromyani', '!greetyani',
                       '!workout']
        utilitiesList = ['!stats', '!location', '!save', '!help', '!quit', '!played']

        ###### DICTIONARIES ######

        locationsList = {
            "!achobench": "Bench in front of Acho",
            "!mesta": "Mesta Street",
            "!koprivshtitsa": "Koprivshtitsa Street",
            "!yavorov": "Yavorov Primary School",
            "!perla": "Perlata",
            "!seagarden": "The Sea Garden"
        }

        ######################### ############################## FUNCTIONS ############################################

        ################################# UTILITY ########################

        # SAVE game with !save

        def save_game():
            endTimeSave = time.time()
            totalPlayedNow = endTimeSave - startTime
            characterPlayedNew = int(characterPlayed) + int(totalPlayedNow)
            characterSave = open('character.csv', 'w', encoding='UTF8', newline='')
            characterNameSave = [characterName]  # Name
            characterDateAndTimeOfBirthSave = [characterDateAndTimeOfBirth]  # DOB
            characterStrengthSave = ([characterStrength])  # Strength
            characterAgilitySave = ([characterAgility])  # Agility
            characterIntelligenceSave = ([characterIntelligence])  # Intelligence
            characterLocationSave = [characterLocation]  # Location
            characterLevelSave = ([characterLevel])  # Level
            characterCoinsSave = ([characterCoins])  # Coins
            characterReputationSave = ([characterReputation])  # Reputation
            characterPasswordSave = ([characterPassword])  # Password
            characterPlayedSave = ([characterPlayedNew])  # Total Played
            characterQuestionSave = [characterQuestion]  # Secret Question
            characterAnswerSave = [characterAnswer]  # Secret Answer

            writer = csv.writer(characterSave)

            writer.writerow(['Character Data'])
            writer.writerow(characterNameSave)  # Name
            writer.writerow(characterDateAndTimeOfBirthSave)  # DOB
            writer.writerow(characterStrengthSave)  # Strength
            writer.writerow(characterAgilitySave)  # Agility
            writer.writerow(characterIntelligenceSave)  # Intelligence
            writer.writerow(characterLocationSave)  # Location
            writer.writerow(characterLevelSave)  # Level
            writer.writerow(characterCoinsSave)  # Coins
            writer.writerow(characterReputationSave)  # Reputation
            writer.writerow(characterPasswordSave)  # Password
            writer.writerow(characterPlayedSave)  # Time Played
            writer.writerow(characterQuestionSave)  # Secret Question
            writer.writerow(characterAnswerSave)  # Secret Answer

            characterSave.close()


        # PRINT !played command
        def played_time():
            TotalTimeNow = time.time() - startTime
            characterPlayedCheck = int(characterPlayed) + int(TotalTimeNow)
            print('Your total played time is: ', time.strftime("%H:%M:%S", time.gmtime(characterPlayedCheck)))


        # PRINT !stats command

        def print_stats():
            print("Name:", characterName)
            print("Date of Birth:", characterDateAndTimeOfBirth)
            print("Level:", characterLevel)
            print("Strength:", characterStrength)
            print("Agility:", characterAgility)
            print("Intelligence:", characterIntelligence)
            print("Coins:", characterCoins)
            print("Reputation:", characterReputation)


        # PRINT !location command
        def print_location():
            if characterLocation == "Bench in front of Acho":
                print("You are currently located at: ", characterLocation)
                print("You can go down to Mesta Street with !mesta")
                print("Or you can go up to Koprivshtitsa Street with !koprivshtitsa")
            elif characterLocation == "Mesta Street":
                print("You are currently located at: ", characterLocation)
                print("You can go down to Perlata with !perla")
                print("Or you can go up to Bench in front of Acho with !achobench")
            elif characterLocation == "Koprivshtitsa Street":
                print("You are currently located at: ", characterLocation)
                print("You can go down to Bench in front of Acho with !achobench")
                print("Or you can go up to Yavorov Primary School with !yavorov")
            elif characterLocation == "Yavorov Primary School":
                print("You are currently located at: ", characterLocation)
                print("You can go down to Koprivshtitsa Street with !koprivshtitsa")
            elif characterLocation == "Perlata":
                print("You are currently located at: ", characterLocation)
                print("You can go down to The Sea Garden with !seagarden")
                print("Or you can go up to Mesta with !mesta")       
            elif characterLocation == "The Sea Garden":
                print("You are currently located at: ", characterLocation)
                print("You can go up to Perlata with !perla")
                

        # PRINT Reputation command
        def print_reputation():
            print("Your reputation is:", characterReputation)


        # PRINT Coins command
        def print_coins():
            print("Your coins are: ", characterCoins)


        # PRINT Level command
        def print_level():
            print("Your level is:", characterLevel)


        # PRINT Strength command
        def print_strength():
            print("Your strength is:", characterStrength)


        # PRINT Agility command
        def print_agility():
            print("Your agility is:", characterAgility)


        # PRINT Intelligence command
        def print_intelligence():
            print("Your intelligence is:", characterIntelligence)


        # PRINT !help command

        def print_help():
            print("!stats to check your character stats.")
            print("!location to check where your character is located and where you can go..")
            print("!save to save your current progress.")
            print("!quit to quit the game.")
            print("!played to check your played time.")

        # QUIT game with !quit
        def quit_game():
            print("Would you like to save your progress before quitting the game?")
            time.sleep(1)
            saveorNot = input("To save and exit, type !yes. To exit without saving, type !no.")
            while True:
                if saveorNot == "!yes":
                    save_game()
                    print("Your game was successfully saved.")
                    time.sleep(0.5)
                    print("Quitting game in 3-..")
                    time.sleep(1)
                    print("Quitting game in 2-..")
                    time.sleep(1)
                    print("Quitting game in 1-..")
                    time.sleep(1)
                    print("See you around!")
                    sys.exit()
                elif saveorNot == "!no":
                    print("You decided not to save your progress.")
                    time.sleep(0.5)
                    print("Quitting game in 3-..")
                    time.sleep(1)
                    print("Quitting game in 2-..")
                    time.sleep(1)
                    print("Quitting game in 1-..")
                    time.sleep(1)
                    print("See you around!")
                    sys.exit()


        # LOGIN FUNCTION
        def login_function():
            while True:
                Name = input("Please input your character's name to login.(case sensitive)")
                Password = getpass.getpass(prompt="Please input your character's password to login.")
                if Name != characterName or Password != characterPassword:
                    print("The specified name or password is incorrect. Please try again.")
                else:
                    print("Login successful!")
                    break


        # WELCOME MESSAGE
        def welcome():
            print("Welcome to World of Lazurcraft, " + characterName + "!")
            time.sleep(2)
            print("Here are your current character details:")
            time.sleep(1)
            print("Name:", characterName)
            print("Date of Birth:", characterDateAndTimeOfBirth)
            print("Level:", characterLevel)
            print("Location:", characterLocation)
            print("Strength:", characterStrength)
            print("Agility:", characterAgility)
            print("Intelligence:", characterIntelligence)
            print("Coins:", characterCoins)
            print("Reputation:", characterReputation)
            time.sleep(2)
            print("For a list of all available commands, type !help")


        # Prints the current location, along with the available quests and options.

        def show_location_and_reputation(location, reputation):
            print("You're at " + location + "!")
            time.sleep(2)
            if location == 'Bench in front of Acho':
                if int(reputation) >= 200:
                    time.sleep(2)
                    print("You look around and you see Gorskiq sitting at 'The Stone'!")
                    time.sleep(2)
                    print("If you'd like to go see Gorskiq, type !visitgorskiq")
                else:
                    print("You look around and you see Ginko sitting at 'The Stone'!")
                    time.sleep(2)
                    print("If you'd like to go see Ginko, type !visitginko")
                time.sleep(2)
                print("If you'd like to go towards Koprivshtitsa Street, type !koprivshtitsa")
                time.sleep(1)
                print("If you'd like to go towards Mesta Street, type !mesta")
            elif location == "Koprivshtitsa Street":
                if int(reputation) >= 200:
                    time.sleep(2)
                    print("You look around and you see Itso - The Liar down the street!")
                    time.sleep(2)
                    print("If you'd like to talk to The Liar, type !visittheliar")
                else:
                    print("You look around and you see the Primo Store!")
                    time.sleep(2)
                    print("If you'd like to head towards the Primo Store, type !visitprimo")
                time.sleep(2)
                print("If you'd like to go up towards Yavorov Primary School, type !yavorov")
                time.sleep(1)
                print("If you'd like to go down towards the bench in front of acho, type !achobench")
            elif location == "Mesta Street":
                if int(reputation) >= 200:
                    time.sleep(2)
                    print("You look around and you see that a crazy blonde woman approaches down from the Sea Garden.")
                    time.sleep(2)
                    print("If you'd like to talk to her, type !visitcrazyblondewoman ")
                else:
                    print("You look around and you see the Shitthrower Store.")
                    time.sleep(2)
                    print("If you'd like to enter the Shitthrower Store, type !visitshitthrower")
                    time.sleep(1)
                time.sleep(2)
                print("If you'd like to go down towards Perla, type !perla")
                time.sleep(2)
                print("If you'd like to go up towards the bench in front of Acho, type !achobench")
            elif location == "Perlata":
                if int(reputation) >= 200:
                    time.sleep(2)
                    print("You look around and you see a communist-looking man, wearing a hat, approaching the Perla area.")
                    time.sleep(2)
                    print("If you'd like to interact with him, type !visithatman")
                else:
                    time.sleep(2)
                    print("You look around and you see George The Jupiter exiting the Perla Store.")
                    time.sleep(2)
                    print("If you'd like to approach George The Jupiter, type !visitthejupiter")
                print("If you'd like to go down towards the Sea Garden, type !seagarden")
                time.sleep(2)
                print("If you'd like to go up towards Mesta Street, type !mesta")
            elif location == "Yavorov Primary School":
                if int(reputation) >= 200:
                    time.sleep(2)
                    print("Soon after entering the school, you notice Yani The Tyson approaching the entrance of Yavkata.")
                    time.sleep(2)
                    if int(characterCoins) >= 10:
                        print("If you'd like to greet him, type !greetyani, or if you'd like to run like a pussy,trying to protect the enormous amount of coins that you  have, type !runfromyani")
                    else:
                        print("If you'd like to greet him, type !greetyani, or if you'd like to run like a pussy,trying to protect the very few coins that you have, type !runfromyani")
                else:
                    time.sleep(2)
                    print("You enter the school and you see people everywhere. To start the workout quest, type !workout")
                    time.sleep(2)
                    print("If you'd like to go down towards Koprivshtitsa Street, type !koprivshtitsa")
            elif location == "The Sea Garden":
                if int(reputation) >= 200:
                    print("CONTENT TO BE ADDED IN NEXT PATCH")
                    time.sleep(1)
                    print("Please go back to Perlata by typing !perla")
                else:
                    print("CONTENT TO BE ADDED IN NEXT PATCH")
                    time.sleep(1)
                    print("Please go back to Perlata by typing !perla")

        # Check if move is a change of location, action or utility and respond.

        def player_move_function(move):
            global characterLocation
            if move in locationsList.keys():
                characterLocation = locationsList[move]
                show_location_and_reputation(characterLocation, characterReputation)
            elif move in actionsList:
                if move == "!visitginko":
                    time.sleep(2)
                    print("You approach Ginko near the Stone.")
                    ginko_quest()
                elif move == "!visitgorskiq":
                    time.sleep(2)
                    print("You approach Gorskiq near the Stone.")
                    gorskiq_quest()
                elif move == "!visitprimo":
                    time.sleep(2)
                    print("You head towards the Primo store with a confident walk.")
                    primo_quest()
                elif move == "!visittheliar":
                    print("You approach Itso the Liar.")
                    time.sleep(2)
                    visittheliar_quest()
                elif move == "!visitshitthrower":
                    print("You head towards the Shitthrower store.")
                    time.sleep(2)
                    shitthrower_quest()
                elif move == "!greetyani":
                    time.sleep(2)
                    greetyani_quest()
                elif move == "!runfromyani":
                    time.sleep(2)
                    runfromyani_quest()
                elif move == "!workout":
                    print("Alright, now we have to decide what kind of workout we'll do.")
                    time.sleep(2)
                    workout_quest()
                elif move == "!visitthejupiter":
                    print("You approach George The Jupiter")
                    time.sleep(2)
                    thejupiter_quest()
            elif move in utilitiesList:
                if move == "!help":
                    print_help()
                elif move == "!stats":
                    print_stats()
                elif move == "!location":
                    print_location()
                elif move == "!save":
                    save_game()
                    print("Your game was successfully saved! Feel free to exit now!")
                elif move == "!quit":
                    quit_game()
                elif move == "!played":
                    played_time()
            else:
                print("This is an invalid command!")


        ####################################### QUESTS LOW REP #####################################################

        #### GINKO QUEST ####
        def ginko_quest():
            global characterReputation
            global characterLevel
            global characterStrength
            global characterAgility
            global characterIntelligence
            time.sleep(3)
            print(characterName + ": Hey, Ginko!")
            time.sleep(2.5)
            print("GINKO: Boy-..")
            time.sleep(2.5)
            print("GINKO: Cawn yew gewt mew my wine?")
            time.sleep(2.5)
            print("*** WOULD YOU LIKE TO ACCEPT THIS QUEST? ***")
            while True:
                acceptQuest = input("Type in !yes to accept or !no to refuse!")
                if acceptQuest == "!yes":
                    print(characterName + ": Sure thing, Ginko! Where have you left it?")
                    time.sleep(3)
                    print("GINKO: I think it's-..")
                    time.sleep(3)
                    print("GINKO: In the gawden be'aind thirty-sixth-..")
                    time.sleep(3)
                    print(characterName + ": Okay, I'll check it for you.")
                    time.sleep(3)
                    print("*** YOU WALK BEHIND 36TH ***")
                    time.sleep(3)
                    print("*** YOU SEE AN ALCOHOLIC SLEEPING ON A BENCH WITH A 5L BOTTLE OF SUSPICIOUS RED LIQUID! ***")
                    time.sleep(3)
                    print("WOULD YOU LIKE TO APPROACH HIM QUIETLY OR WOULD YOU RUSH TO HIM AND GRAB THE BOTTLE?")
                    time.sleep(3)
                    while True:
                        quietOrRush = input("Type in !quiet for a quiet approach and !rush to rush for the bottle.")
                        if quietOrRush == "!quiet":
                            time.sleep(3)
                            print("*** YOU APPROACH THE STRANGER QUIETLY AND YOU REACH FOR THE BOTTLE'S HANDLE ***")
                            time.sleep(3)
                            print("*** YOU GRAB THE BOTTLE'S HANDLE AND YOU HEAR-... ***")
                            time.sleep(3)
                            print("*** A LOUD FART ***")
                            time.sleep(3)
                            print("*** YOU REMAIN CALM AND YOU WALK AWAY BACK TO THE STONE ***")
                            time.sleep(3.5)
                            print("GINKO: Heeeeeyw-...")
                            time.sleep(3)
                            print("GINKO: Grewt jowb-.. boyw!")
                            time.sleep(2.5)
                            print("GINKO: What's yer name?")
                            time.sleep(2.5)
                            print(characterName + ": I'm " + characterName + "!")
                            time.sleep(3)
                            print("GINKO: A'right, " + characterName + " thank yew!")
                            time.sleep(3)
                            print("QUEST GINKO COMPLETED!")
                            time.sleep(3)
                            print(
                                "*** CONGRATULATIONS! YOU'VE EARNED +10 REPUTATION, GAINED A LEVEL AND INCREASED YOUR INTELLIGENCE BY 1.")
                            time.sleep(3)
                            characterReputation = int(characterReputation) + 10
                            characterLevel = int(characterLevel) + 1
                            characterIntelligence = int(characterIntelligence) + 1
                            print_reputation()
                            time.sleep(0.5)
                            print_level()
                            time.sleep(0.5)
                            print_intelligence()
                            time.sleep(0.5)
                            return
                        elif quietOrRush == "!rush":
                            time.sleep(2)
                            print("*** YOU RUSH FOR THE BENCH AND GRAB THE BOTTLE'S HANDLE ***")
                            time.sleep(2)
                            print("*** SUDDENLY, THE STRANGER WAKES UP AND SHOUTS! ***")
                            time.sleep(2.5)
                            print("STRANGER: Hey you! That's mine!")
                            time.sleep(2)
                            print("*** YOU IGNORE HIM AND START RUNNING TOWARDS GINKO AT THE STONE")
                            time.sleep(2)
                            print("*** AS YOU APPROACH THE STONE YOU REALIZE THAT THE STRANGER HAS BEEN CHASING YOU")
                            time.sleep(2)
                            print("*** YOU DROP THE BOTTLE IN FRONT OF GINKO AND YOU TURN AROUND ***")
                            time.sleep(2)
                            print("*** GINKO STANDS UP FROM THE STONE AND CHARGES AT THE STRANGER ***")
                            time.sleep(1)
                            print("WOULD YOU LIKE TO HELP GINKO IN THE FIGHT?")
                            while True:
                                fightForGinko = input(
                                    "Type in !fight if you'd like to join the fight or !run if you'd like to run towards the bench in front of Acho!")
                                if fightForGinko == "!fight":
                                    print(
                                        "*** YOU CHARGE TOWARDS THE STRANGER ALONG WITH GINKO AND SWING A RIGHT PUNCH IN HIS FACE!")
                                    time.sleep(2.5)
                                    print(
                                        "*** THE PUNCH CONNECTS WHILE GINKO FORCEFULLY PUSHES THE STRANGER WITH BOTH HIS ARMS ***")
                                    time.sleep(2.5)
                                    print(
                                        "*** THE STRANGER FALLS ON HIS BACK AND QUICKLY STANDS UP AND START RUNNING TOWARDS THE GARDEN ***")
                                    time.sleep(3)
                                    print("*** GINKO EXHALES *** GINKO: Ha, tha's wha' ye' get fo' stealin' mew wine!")
                                    time.sleep(3)
                                    print("*** GINKO TURNS TOWARDS YOU, BREATHING HEAVILY ***")
                                    time.sleep(2.5)
                                    print("GINKO: Grewt jowb-.. boyw!")
                                    time.sleep(1.5)
                                    print("GINKO: What's yer name?")
                                    time.sleep(1.5)
                                    print(characterName + ": I'm " + characterName + "!")
                                    time.sleep(2)
                                    print("GINKO: A'right, " + characterName + " thank yew!")
                                    time.sleep(2)
                                    print("QUEST GINKO COMPLETED!")
                                    time.sleep(2)
                                    print(
                                        "*** CONGRATULATIONS! YOU'VE EARNED +10 REPUTATION, GAINED 2 LEVELS AND INCREASED YOUR STRENGTH BY 1")
                                    time.sleep(3)
                                    characterReputation = int(characterReputation) + 10
                                    characterLevel = int(characterLevel) + 2
                                    characterStrength = int(characterStrength) + 1
                                    print_level()
                                    time.sleep(0.5)
                                    print_reputation()
                                    time.sleep(0.5)
                                    print_strength()
                                    time.sleep(0.5)
                                    return
                                elif fightForGinko == "!run":
                                    print("*** YOU MAKE A RUN TOWARDS THE BENCH IN FRONT OF ACHO INTO SAFETY ***")
                                    time.sleep(2.5)
                                    print("QUEST GINKO COMPLETED!")
                                    time.sleep(2)
                                    print(
                                        "*** CONGRATULATIONS! YOU'VE EARNED +10 REPUTATION, GAINED 1 LEVEL AND INCREASED YOUR AGILITY BY 2")
                                    time.sleep(2)
                                    characterReputation = int(characterReputation) + 10
                                    characterLevel = int(characterLevel) + 1
                                    characterAgility = int(characterAgility) + 2
                                    print_level()
                                    time.sleep(0.5)
                                    print_reputation()
                                    time.sleep(0.5)
                                    print_agility()
                                    time.sleep(0.5)
                                    return
                                else:
                                    print("This is an invalid command!")
                                    continue
                        else:
                            print("This is an invalid command!")
                            continue
                elif acceptQuest == "!no":
                    time.sleep(2)
                    print(characterName + ": Sorry Ginko, but not today. I got better things to do right now.")
                    time.sleep(2)
                    print("*** YOU TURN AROUND AND YOU WALK BACK TOWARDS THE BENCH IN FRONT OF ACHO ***")
                    return
                else:
                    print("This is an invalid command!")
                    continue


        #### PRIMO QUEST ####
        def primo_quest():
            global characterReputation
            global characterLevel
            global characterStrength
            global characterAgility
            global characterIntelligence
            global characterCoins
            global characterName
            time.sleep(3)
            print("*** As you approach the Primo store, you wonder what you'll be getting ***")
            time.sleep(3)
            print("*** Is it going to be Instant Noodles? A cup of Frozen Juice? Or maybe a Coffee Cola by Derby? ***")
            time.sleep(3)
            print(
                "*** You enter the Primo and you pass by a boy who appears to be a bit younger than you. Did you decide what you'll be getting already? ***")
            time.sleep(3)
            while True:
                primoDecision = input(
                    "Type !noodles to look for Instant Noodles, !frozenjuice to look for a cup of Frozen Juice or !coffeecola to look for a bottle of Coffee Cola by Derby ***")
                if primoDecision == "!noodles" or primoDecision == "!frozenjuice" or primoDecision == "!coffeecola":
                    print(
                        "*** As you approach the shelf, containing your sterile manufactured product, you hear the cashier shouting-.. ***")
                    time.sleep(3)
                    print("CASHIER: HEY YOU! COME BACK!")
                    time.sleep(3)
                    print(
                        "*** You turn towards the exit and you see the boy heading for the exit while skipping the pay desk ***")
                    time.sleep(3)
                    while True:
                        primoDecision2 = input("Type !chase to chase the boy or !ignore to ignore what's happening.")
                        if primoDecision2 == "!chase":
                            print("*** You drop your high-quality product as you rush after the kid ***")
                            time.sleep(2.5)
                            print(
                                "*** The boy turns right and starts running as he exits while slamming the door closed in front of you.")
                            time.sleep(3)
                            print(
                                "*** You open the door and start chasing him down as he runs on the sidewalk of Koprivshtitsa towards the side of 35th. ***")
                            time.sleep(3)
                            print(
                                "*** You soon approach the boy and have to decide whether to try to tackle his feet from behind or to try to get closer and grab him by his T-shirt.")
                            while True:
                                primoDecision3 = input(
                                    "Type !tackle to try to tackle the boy from behind or !grab to try to get even closer and grab him by his T-shirt.")
                                if primoDecision3 == "!tackle":
                                    print("*** You swing your leg at the kid's feet and successfully tackle him. ***")
                                    time.sleep(3)
                                    print(
                                        "*** The little vagabont drops on the floor as he spills the large pack of popcorn he had stolen just a few moments ago.")
                                    time.sleep(3)
                                    print(characterName,
                                          ": That's what you get from stealing from this neighborhood, fool.")
                                    time.sleep(3)
                                    print("*** The fool stands up while crying and heads down towards the Sea Garden.")
                                    time.sleep(3)
                                    print(
                                        "*** You receive +15 reputation and you level up for your deed. The little thief was punished and Lazur Mahala is once again a safe place to patrol. ***")
                                    time.sleep(3)
                                    print("*** Your strength has increased by 1 ***")
                                    characterStrength = int(characterStrength) + 1
                                    characterReputation = int(characterReputation) + 15
                                    characterLevel = int(characterLevel) + 1
                                    time.sleep(2)
                                    print_level()
                                    time.sleep(0.5)
                                    print_reputation()
                                    time.sleep(0.5)
                                    print_strength()
                                    time.sleep(0.5)
                                    return
                                elif primoDecision3 == "!grab":
                                    print(
                                        "*** You get even closer and reach out for the little vagabont's T-shirt. ***")
                                    time.sleep(3)
                                    print(
                                        "*** Just a few moments later, you grab the thief's T-shirt and he stops. ***")
                                    time.sleep(3)
                                    print("Little Thief shouting: Please, please, don't hurt me-...")
                                    time.sleep(2.5)
                                    print("*** The boy starts crying ***")
                                    time.sleep(3)
                                    print("Little Thief: Here, take this")
                                    time.sleep(3)
                                    print(
                                        "*** The kid offers you a pack of popcorn. Apparently, that's the stolen loot. ***")
                                    time.sleep(3)
                                    print(
                                        "*** You teach the poor boy a lesson as you recover ownership of the pack of popcorn ***")
                                    time.sleep(3)
                                    print(
                                        "*** But now you have a choice to make. Would you return the popcorn to the Primo store or would you keep it for yourself? ***")
                                    time.sleep(3)
                                    while True:
                                        primoDecision4 = input(
                                            "Type !return to return the popcorn to the Primo store or !keep to keep it and enjoy the free snack.")
                                        if primoDecision4 == ("!return"):
                                            print(
                                                "*** You go back to the Primo store and return the pack of popcorn as the cashier thanks you and is very proud of you.")
                                            time.sleep(3)
                                            print(
                                                "*** The cashier takes the pack of popcorn and puts it back on the shelf ***")
                                            time.sleep(3)
                                            print(
                                                "Your reputation has increased by 20, you level up and your agility has increased by 1")
                                            characterReputation = int(characterReputation) + 20
                                            characterLevel = int(characterLevel) + 1
                                            characterAgility = int(characterAgility) + 1
                                            print_reputation()
                                            time.sleep(0.5)
                                            print_level()
                                            time.sleep(0.5)
                                            print_agility()
                                            time.sleep(0.5)
                                            return
                                        elif primoDecision4 == ("!keep"):
                                            print(
                                                "*** You decide to keep the pack of popcorn that you just received. ***")
                                            time.sleep(3)
                                            print(
                                                "*** You sit on the Stone in front of Nikolai and start munching the popcorn ***")
                                            time.sleep(3)
                                            print(
                                                "Your reputation has increased by 15, you level up and your agility and intelligence has increased by 1")
                                            characterReputation = int(characterReputation) + 15
                                            characterLevel = int(characterLevel) + 1
                                            characterAgility = int(characterAgility) + 1
                                            characterIntelligence = int(characterIntelligence) + 1
                                            time.sleep(1.5)
                                            print_reputation()
                                            time.sleep(0.5)
                                            print_level()
                                            time.sleep(0.5)
                                            print_agility()
                                            time.sleep(0.5)
                                            print_intelligence()
                                            time.sleep(0.5)
                                            return
                                        else:
                                            print("That's an invalid command. Didn't you learn already?")
                                            continue
                                else:
                                    print("That's an invalid command. Didn't you learn already?")
                                    continue
                        elif primoDecision2 == "!ignore":
                            print("*** You ignore the situation and the kid escapes with his loot ***")
                            time.sleep(3)
                            print("CASHIER while looking at you: C'mon, won't you do anything?")
                            time.sleep(3)
                            print("CASHIER while looking at you: And you're not even ashamed of yourself-...")
                            time.sleep(3)
                            print(
                                "CASHIER while looking at you: The whole new generation is like that. Back in the days, that wouldn't happen.")
                            time.sleep(3)
                            print(
                                "*** You quietly pass through the pay desk as you pay for your high-quality product and you leave the Primo store ***")
                            time.sleep(3)
                            if characterLevel >= 2:
                                characterLevel = int(characterLevel) - 1
                                characterReputation = int(characterReputation) - 10
                                print(
                                    "*** You lose 10 Reputation and 1 Level for your deed. A store in Lazur Mahala was robbed today.")
                                time.sleep(2)
                                print_reputation()
                                time.sleep(0.5)
                                print_level()
                                time.sleep(0.5)
                                return
                            else:
                                characterReputation = int(characterReputation) - 10
                                print(
                                    "*** You lose 10 Reputation for your deed. A store in Lazur Mahala was robbed today.")
                                time.sleep(2)
                                print_reputation()
                                time.sleep(1)
                                return
                        else:
                            print("That's an invalid command. Didn't you learn already?")
                            continue
                else:
                    print("That's an invalid command. didn't you learn already?")
                    continue


        #### STREET FITNESS QUEST ####
        def workout_quest():
            global characterReputation
            global characterLevel
            global characterStrength
            global characterAgility
            global characterIntelligence
            global characterCoins
            global characterName
            while True:
                workoutDecision = input(
                    "Type !streetfitness for a street fitness workout. Type !jogging to jog around the football pitch or type !rest if you dont feel like working out and prefer to rest on a bench.")
                if workoutDecision == "!streetfitness":
                    print(
                        "*** You walk towards the Street Fitness equipment and deep inside you know you'll barely make 1 rep. ***")
                    time.sleep(3)
                    print("*** But you BELIEVE in YOURSELF and are DETERMINED to give your BEST! ***")
                    time.sleep(3)
                    print("*** You PUSH hard and successfully make 1 pull-up. ***")
                    time.sleep(3)
                    print("*** Soon you get compliments and motivational words from the djigits around you. ***")
                    time.sleep(3)
                    print("Random hap: Keep it up, little one, keep it up!")
                    time.sleep(2.5)
                    print("Another random anabol: What's your name, boy?")
                    time.sleep(3)
                    print(characterName, ": I-.. I-.. am -.. ", characterName)
                    time.sleep(3)
                    print("Street fitness maniac: From today you are ", characterName, " Losta, gu-gu-gu-gu-gu")
                    time.sleep(4)
                    print("*** The whole crowd starts laughing ***")
                    time.sleep(3)
                    print("*** You don't realize it yet, but tomorrow, the whole Lazur Mahala will know you as ",
                          characterName, " Losta")
                    characterName = characterName + " Losta"
                    time.sleep(4)
                    print("*** Your new name is now: ", characterName,
                          " (make sure you use your new name the next time you login) ***")
                    time.sleep(4)
                    print(
                        "*** You gained a level, your reputation has increased by 15 and your strength has increased by 1. ***")
                    time.sleep(4)
                    characterLevel = int(characterLevel) + 1
                    characterReputation = int(characterReputation) + 15
                    characterStrength = int(characterStrength) + 1
                    print_level()
                    time.sleep(0.5)
                    print_reputation()
                    time.sleep(0.5)
                    print_strength()
                    time.sleep(0.5)
                    return
                elif workoutDecision == "!jogging":
                    print("*** You slowly start jogging around. ***")
                    time.sleep(3)
                    print("*** You keep running for about 15 minutes when-.. ***")
                    time.sleep(3)
                    print(
                        "*** As you run you notice that the ball that they play football with is coming towards you. ***")
                    time.sleep(3)
                    print("Random guy from the football pitch: Hey, little one, pass the ball.")
                    time.sleep(3)
                    while True:
                        passTheBall = input("Type !pass to attempt to pass the ball and !ignore to ignore the request.")
                        if passTheBall == "!pass":
                            goodPass = random.random()
                            if goodPass >= 0.5:
                                print(
                                    "*** You hit the ball perfectly and pass the ball directly to the person asking for it.")
                                time.sleep(3)
                                print("Random guy from the football pitch: Nice pass, boy! Thanks!")
                                time.sleep(3)
                                print("*** You keep jogging for 10 more minutes and then finish your workout.")
                                time.sleep(3)
                                print(
                                    "*** You gained a level, increased your agility by 1 and increased your reputation by 10.")
                                characterLevel = int(characterLevel) + 1
                                characterAgility = int(characterAgility) + 1
                                characterReputation = int(characterReputation) + 10
                                time.sleep(3)
                                print_level()
                                time.sleep(0.5)
                                print_agility()
                                time.sleep(0.5)
                                print_reputation()
                                time.sleep(0.5)
                                return
                            else:
                                print("*** You miss the ball and trip, almost falling on the ground. ***")
                                time.sleep(3)
                                print("*** Everyone from the football pitch starts laughing at you. ***")
                                time.sleep(3)
                                print(
                                    "*** You ignore them and continue jogging for 10 more minutes, leaving them to get the ball themselves. ***")
                                time.sleep(3)
                                print(
                                    "*** You gained a level, increased your agility by 1 but decreased your reputation by 5. ***")
                                characterLevel = int(characterLevel) + 1
                                characterAgility = int(characterAgility) + 1
                                characterReputation = int(characterReputation) - 5
                                time.sleep(3)
                                print_level()
                                time.sleep(0.5)
                                print_agility()
                                time.sleep(0.5)
                                print_reputation()
                                time.sleep(0.5)
                                return
                        elif passTheBall == "!ignore":
                            print("*** You ignore their request and hear some mumbling and swearing. ***")
                            time.sleep(3)
                            print("*** But that's fine, they're probably not talking to you-... ***")
                            time.sleep(3)
                            print("*** They didn't ask specifically YOU to pass the ball, so we're fine here. ***")
                            time.sleep(3)
                            print(
                                "*** You continue jogging for 10 more minutes, leaving them to get the ball themselves. ***")
                            time.sleep(3)
                            print(
                                "*** You gained a level, increased your agility by 1 but decreased your reputation by 10. ***")
                            characterLevel = int(characterLevel) + 1
                            characterAgility = int(characterAgility) + 1
                            characterReputation = int(characterReputation) - 10
                            time.sleep(3)
                            print_level()
                            time.sleep(0.5)
                            print_agility()
                            time.sleep(0.5)
                            print_reputation()
                            time.sleep(0.5)
                            return
                        else:
                            print("This is an invalid command. Didn't you learn already?")
                            continue
                elif workoutDecision == "!rest":
                    time.sleep(1.5)
                    print("*** You start walking towards the nearest empty bench. ***")
                    time.sleep(3)
                    print(
                        "*** Soon you sit down to rest, even though you're not tired and get lost in deep thoughts. *** ")
                    time.sleep(5)
                    print(
                        "*** While you're looking around you notice something shining in the grass next to the bench. ***")
                    time.sleep(3)
                    print("*** You get closer and you realize that someone has lost 8 coins. ***")
                    time.sleep(3)
                    print(
                        "*** You look around to check that nobody is looking at you and quickly pocket the coins with a smile. ***")
                    time.sleep(2.5)
                    print("*** Nice workout! You gained 8 coins!")
                    characterCoins = int(characterCoins) + 8
                    time.sleep(2)
                    print_coins()
                    time.sleep(2)
                    return
                else:
                    print("This is an invalid command. Didn't you learn already?")
                    continue

        #### GEORGE THE JUPITER QUEST ####
        def thejupiter_quest():
            global characterReputation
            global characterLevel
            global characterStrength
            global characterAgility
            global characterIntelligence
            global characterCoins
            global characterName
            print("George The Jupiter: Hey, " + characterName + "!")
            time.sleep(2)
            print(characterName + ": Whass'up, Jupiter?")
            time.sleep(2)
            print("George The Jupiter: Nothing much. Wanna play a gambling game?")
            time.sleep(3)
            print("*** WOULD YOU LIKE TO PLAY A GAMBLING GAME WITH GEORGE THE JUPITER? ***")
            time.sleep(2)
            while True:
                acceptQuest = input("Type in !yes to accept or !no to refuse")
                if acceptQuest == "!yes":
                    time.sleep(2)
                    print(characterName + ": Yes, what is the game about?")
                    time.sleep(2)
                    print("George The Jupiter: We bet on Heads and Tails. We toss a coin and whoever's got the correct bet takes it all.")
                    time.sleep(2)
                    print("George The Jupiter: What do you think?")
                    time.sleep(2)
                    while True:
                        wantToPlay = input("Type in !yes if you still want to play and !no to refuse.")
                        if wantToPlay == "!yes":
                            time.sleep(1)
                            print(characterName + ": Sure, let's play.")
                            time.sleep(2)
                            print("George The Jupiter: Alright, deposit some coins and I'll match your bet.")
                            time.sleep(3)
                            print("*** You check your pants to see how many coins you have ***")
                            if int(characterCoins) >= 1:
                                time.sleep(3)
                                print_coins()
                                time.sleep(2)
                                while True:
                                    try:
                                        deposit = int(input("Type in the amount of coins you want to bet in this Head vs Tails game?"))
                                        if int(deposit) > 0 and int(deposit) < 20:
                                            if int(deposit) <= int(characterCoins):
                                                print(characterName + ": Okay, I'm betting " + str(deposit) +" coins")
                                                time.sleep(2)
                                                print("George The Jupiter: Okay, now choose heads or tails?")
                                                time.sleep(2)
                                                while True:
                                                        choose = input("Type in !heads or !tails.")
                                                        if choose == "!heads":
                                                            time.sleep(1.5)
                                                            print(characterName + ": I choose Heads!")
                                                            time.sleep(2)
                                                            print("George The Jupiter: Alright, Tails is for me then.")
                                                            time.sleep(2)
                                                            print("*** George The Jupiter takes out one coins and starts counting: ***")
                                                            time.sleep(3)
                                                            print("THREE")
                                                            time.sleep(1.5)
                                                            print("TWO")
                                                            time.sleep(1.5)
                                                            print("ONE")
                                                            time.sleep(1)
                                                            print("*** George The Jupiter tosses the coin and it lands on: ***")
                                                            time.sleep(1)
                                                            coinDrop = random.random()
                                                            if coinDrop >= 0.60:
                                                                print("*** HEADS!!! ***")
                                                                time.sleep(2)
                                                                print("George The Jupiter: Ah, crap..")
                                                                time.sleep(2)
                                                                print("Alright, take your coins.")
                                                                time.sleep(2)
                                                                winAmount = int(deposit) + int(deposit)
                                                                print("You grab " + str(winAmount) +" coins and pocket them.")
                                                                time.sleep(3)
                                                                characterCoins = int(characterCoins) + int(deposit)
                                                                print_coins()
                                                                time.sleep(2)
                                                                print("You walk back to the Perla Stone a richer person.")
                                                                time.sleep(1)
                                                                return
                                                            else:
                                                                print("*** TAILS!!! ***")
                                                                time.sleep(2)
                                                                print("George The Jupiter: Hehey, I win!")
                                                                time.sleep(2)
                                                                characterCoins = int(characterCoins) - int(deposit)
                                                                print_coins()
                                                                time.sleep(2)
                                                                print("You walk back to the Perla Stone a poorer person.")
                                                                time.sleep(1)
                                                                return
                                                        elif choose == "!tails":
                                                            time.sleep(1.5)
                                                            print(characterName + ": I choose Tails!")
                                                            time.sleep(2)
                                                            print("George The Jupiter: Alright, Heads is for me then.")
                                                            time.sleep(2)
                                                            print("*** George The Jupiter takes out one coins and starts counting: ***")
                                                            time.sleep(3)
                                                            print("THREE")
                                                            time.sleep(1.5)
                                                            print("TWO")
                                                            time.sleep(1.5)
                                                            print("ONE")
                                                            time.sleep(1)
                                                            print("*** George The Jupiter tosses the coin and it lands on: ***")
                                                            time.sleep(1)
                                                            coinDrop = random.random()
                                                            if coinDrop >= 0.60:
                                                                print("*** HEADS!!! ***")
                                                                time.sleep(2)
                                                                print("George The Jupiter: Hehey, I win!")
                                                                time.sleep(2)
                                                                characterCoins = int(characterCoins) - int(deposit)
                                                                print_coins()
                                                                time.sleep(2)
                                                                print("You walk back to the Perla Stone a poorer person.")
                                                                time.sleep(1)
                                                                return          
                                                            else:
                                                                print("*** TAILS!!! ***")
                                                                time.sleep(2)
                                                                print("George The Jupiter: Ah, crap..")
                                                                time.sleep(2)
                                                                print("Alright, take your coins.")
                                                                time.sleep(2)
                                                                winAmount = int(deposit) + int(deposit)
                                                                print("You grab " + str(winAmount) +" coins and pocket them.")
                                                                time.sleep(3)
                                                                characterCoins = int(characterCoins) + int(deposit)
                                                                print_coins()
                                                                time.sleep(2)
                                                                print("You walk back to the Perla Stone a richer person.")
                                                                time.sleep(1)
                                                                return
                                                        else:
                                                            print("This is an invalid command! Didn't you learn already after all this playing?")
                                                            time.sleep(2)
                                                            continue
                                                        break;
                                            else:
                                                print("You can't deposit more coins than you currently have.")
                                                time.sleep(2)
                                                continue
                                        else:
                                            print("You can't deposit less than 1 coin or more than 20 coins as The Jupiter doesn't have that many.")
                                            continue
                                    except ValueError:
                                        print("Your answer can only be a number.")
                            else:
                                time.sleep(3)
                                print_coins()
                                time.sleep(2)
                                print(characterName + ": Sorry, Jupiter, but I ain't got no spare coins right now. See ya' later.")
                                time.sleep(2)
                                return
                        elif wantToPlay == "!no":
                            time.sleep(2)
                            print(characterName + ": Sorry Jupiter, but I don't want to steal your coins today.")
                            time.sleep(1)
                            print("*** YOU TURN AROUND AND YOU WALK BACK TOWARDS THE PERLA STONE. ***")
                            return
                        else:
                            print("This is an invalid command! !yes - to accept and !no to refuse. Didn't you learn already after all this playing?")
                            continue    
                elif acceptQuest == "!no":
                    time.sleep(2)
                    print(characterName + ": Sorry Jupiter, but not today. I got better things to do right now.")
                    time.sleep(1)
                    print("*** YOU TURN AROUND AND YOU WALK BACK TOWARDS THE PERLA STONE. ***")
                    return
                else:
                    print("This is an invalid command! !yes - to accept and !no to refuse. Didn't you learn already after all this playing?")
                    continue    

        def shitthrower_quest():
            global characterReputation
            global characterLevel
            global characterStrength
            global characterAgility
            global characterIntelligence
            global characterCoins
            global characterName
            possibleActions = ["!rock", "!paper", "!scissors"]
            print("*** As you're headed towards the Shitthrower you meet Kalin going out and he joins your company for a small talk while you're walking.")
            time.sleep(4)
            print("*** The usual what's up, what's good chit chat.")
            time.sleep(4)
            print("*** A FEW MOMENTS LATER YOU NOTICE SOMETHING ON THE GROUND ***")
            time.sleep(3)
            print(characterName + ": Hey, that's 2 coins on the ground! ** You point at the dropped 2 coins on the sidewalk **")
            time.sleep(4)
            print("** Not even a second after you point at the 2 coins and Kalin quickly ducks down and grabs the coins **")
            time.sleep(4)
            print(characterName + ": Ey', I saw it first, give it to me.")
            time.sleep(4)
            print("Kalin: Yeah, but I took it first.")
            time.sleep(3)
            print(characterName + ": That's unfair!")
            time.sleep(3)
            print("Kalin: Fine-.. fine-..")
            time.sleep(3)
            print("Kalin: Here's what we're gonna do. We'll play rock, paper, scissors and whoever wins will take it. That's fair, right?")
            time.sleep(3)
            print(characterName + ": Sure. Best of 1 or Best of 3?")
            time.sleep(3)
            print("Kalin: You decide, makes no difference for me.")
            time.sleep(3)
            while True:
                gameType = input("Type in !bestof1 or !bestof3")
                if gameType == "!bestof1":
                    time.sleep(2)
                    print(characterName + ": Let's make it best of 1.")
                    time.sleep(2)
                    print("Kalin: Alrighty then.")
                    time.sleep(2)
                    print("Kalin: Ready?")
                    time.sleep(2)
                    print("Kalin: Rock, paper, scissors. ")
                    time.sleep(1)
                    print("One.")
                    time.sleep(1)
                    print("Two.")
                    time.sleep(1)
                    while True:
                        kalinAction = random.choice(possibleActions)
                        userAction = input("Type in either !rock, !paper or !scissors")
                        if userAction == "!rock" or userAction == "!paper" or userAction == "!scissors":
                            if userAction == kalinAction:
                                print("Three.")
                                print("*** You both show the same and it's a draw. ***")
                                time.sleep(2)
                                print("Kalin: Rock, paper, scissors. ")
                                time.sleep(1)
                                print("One.")
                                time.sleep(1)
                                print("Two.")
                                time.sleep(1)
                                continue
                            elif userAction == "!rock":
                                if kalinAction == "!scissors":
                                    print("Three.")
                                    time.sleep(1)
                                    print("*** You show Rock and Kalin shows Scissors. You win.")
                                    time.sleep(2)
                                    print("*** Kalin passes you the 2 coins. ***")
                                    time.sleep(2)
                                    characterCoins = int(characterCoins) + 2
                                    time.sleep(2)
                                    print_coins()
                                    time.sleep(2)
                                    print("*** After winning the game you return back to Mesta.")
                                    return
                                else:
                                    print("Three.")
                                    time.sleep(1)
                                    print("You show Rock and Kalin shows Paper. You lose.")
                                    time.sleep(1)
                                    print("Kalin: Haaa! Take that!")
                                    time.sleep(2)
                                    print("Kalin: I win.")
                                    time.sleep(2)
                                    print("*** Kalin says bye and grins widely as he leaves up towards Bolero.")
                                    time.sleep(2)
                                    print("*** After losing the game you return back to Mesta.")
                                    return
                            elif userAction == "!paper":
                                if kalinAction == "!rock":
                                    print("Three.")
                                    time.sleep(1)
                                    print("You show Paper and Kalin shows Rock. You win.")
                                    time.sleep(2)
                                    print("*** Kalin passes you the 2 coins. ***")
                                    time.sleep(2)
                                    characterCoins = int(characterCoins) + 2
                                    time.sleep(2)
                                    print_coins()
                                    time.sleep(2)
                                    print("*** After winning the game you return back to Mesta.")
                                    return
                                else:
                                    print("Three.")
                                    time.sleep(1)
                                    print("You show Paper and Kalin shows Scissors. You lose.")
                                    time.sleep(1)
                                    print("Kalin: Haaa! Take that!")
                                    time.sleep(2)
                                    print("Kalin: I win.")
                                    time.sleep(2)
                                    print("*** Kalin says bye and grins widely as he leaves up towards Bolero.")
                                    time.sleep(2)
                                    print("*** After losing the game you return back to Mesta.")
                                    return
                            elif userAction == "!scissors":
                                if kalinAction == "!paper":
                                    print("Three.")
                                    time.sleep(1)
                                    print("You show Scissors and Kalin shows Paper. You win.")
                                    time.sleep(2)
                                    print("*** Kalin passes you the 2 coins. ***")
                                    time.sleep(2)
                                    characterCoins = int(characterCoins) + 2
                                    time.sleep(2)
                                    print_coins()
                                    time.sleep(2)
                                    print("*** After winning the game you return back to Mesta.")
                                    return
                                else:
                                    print("Three.")
                                    time.sleep(1)
                                    print("You show Scissors and Kalin shows Rock. You lose.")
                                    time.sleep(1)
                                    print("Kalin: Haaa! Take that!")
                                    time.sleep(2)
                                    print("Kalin: I win.")
                                    time.sleep(2)
                                    print("*** Kalin says bye and grins widely as he leaves up towards Bolero.")
                                    time.sleep(2)
                                    print("*** After losing the game you return back to Mesta. ***")
                                    return
                        else:    
                            print("This is an invalid command.")
                            time.sleep(1)
                            continue
                elif gameType == "!bestof3":
                    time.sleep(2)
                    print(characterName + ": Let's make it best of 3.")
                    time.sleep(2)
                    print("Kalin: Alrighty then.")
                    time.sleep(2)
                    print("Kalin: Ready?")
                    time.sleep(2)
                    print("Kalin: Rock, paper, scissors. ")
                    time.sleep(1)
                    print("One.")
                    time.sleep(1)
                    print("Two.")
                    time.sleep(1)
                    userWins = 0
                    kalinWins = 0
                    neccesaryWins = 2
                    while True:
                        kalinAction = random.choice(possibleActions)
                        userAction = input("Type in either !rock, !paper or !scissors")
                        if userAction == "!rock" or userAction == "!paper" or userAction == "!scissors":
                            if userAction == kalinAction:
                                print("Three.")
                                print("*** You both show the same and it's a draw. ***")
                                time.sleep(2)
                                print("Kalin: Rock, paper, scissors. ")
                                time.sleep(1)
                                print("One.")
                                time.sleep(1)
                                print("Two.")
                                time.sleep(1)
                                continue
                            elif userAction == "!rock" and kalinAction == "!scissors":
                                userWins += 1
                                print("Three.")
                                time.sleep(1)
                                print("*** You show Rock and Kalin shows Scissors. You win.")
                                time.sleep(2)
                                print("The result is:")
                                time.sleep(1)
                                print(characterName + ": " + str(userWins) + " wins.")
                                print("Kalin: " + str(kalinWins) + " wins.")
                                time.sleep(2)
                                if userWins == neccesaryWins:
                                    print("*** You win.")
                                    time.sleep(2)
                                    print("*** Kalin passes you the 2 coins. ***")
                                    time.sleep(2)
                                    characterCoins = int(characterCoins) + 2
                                    time.sleep(2)
                                    print_coins()
                                    time.sleep(2)
                                    print("*** After winning the game you return back to Mesta.")
                                    return
                                else:
                                    continue           
                            elif userAction == "!rock" and kalinAction =="!paper":
                                kalinWins += 1
                                print("Three.")
                                time.sleep(1)
                                print("You show Rock and Kalin shows Paper. You lose.")
                                time.sleep(1)
                                print("The result is:")
                                time.sleep(1)
                                print(characterName + ": " + str(userWins) + " wins.")
                                print("Kalin: " + str(kalinWins) + " wins.")
                                time.sleep(2)
                                if kalinWins == neccesaryWins:
                                    print(" You lose.")
                                    time.sleep(1)
                                    print("Kalin: Haaa! Take that!")
                                    time.sleep(2)
                                    print("Kalin: I win.")
                                    time.sleep(2)
                                    print("*** Kalin says bye and grins widely as he leaves up towards Bolero.")
                                    time.sleep(2)
                                    print("*** After losing the game you return back to Mesta.")
                                    return
                                else:
                                    continue
                            elif userAction == "!paper" and kalinAction == "!rock":
                                userWins += 1
                                print("Three.")
                                time.sleep(1)
                                print("You show Paper and Kalin shows Rock. You win.")
                                time.sleep(2)
                                print("The result is:")
                                time.sleep(1)
                                print(characterName + ": " + str(userWins) + " wins.")
                                print("Kalin: " + str(kalinWins) + " wins.")
                                time.sleep(2)
                                if userWins == neccesaryWins:
                                    print("*** You win.")
                                    time.sleep(2)
                                    print("*** Kalin passes you the 2 coins. ***")
                                    time.sleep(2)
                                    characterCoins = int(characterCoins) + 2
                                    time.sleep(2)
                                    print_coins()
                                    time.sleep(2)
                                    print("*** After winning the game you return back to Mesta.")
                                    return
                                else:
                                    continue
                            elif userAction =="!paper" and kalinAction == "!scissors":
                                kalinWins +=1
                                print("Three.")
                                time.sleep(1)
                                print("You show Paper and Kalin shows Scissors. You lose.")
                                time.sleep(1)
                                print("The result is:")
                                time.sleep(1)
                                print(characterName + ": " + str(userWins) + " wins.")
                                print("Kalin: " + str(kalinWins) + " wins.")
                                time.sleep(2)
                                if kalinWins == neccesaryWins:
                                    print(" You lose.")
                                    time.sleep(1)
                                    print("Kalin: Haaa! Take that!")
                                    time.sleep(2)
                                    print("Kalin: I win.")
                                    time.sleep(2)
                                    print("*** Kalin says bye and grins widely as he leaves up towards Bolero.")
                                    time.sleep(2)
                                    print("*** After losing the game you return back to Mesta.")
                                    return
                                else:
                                    continue
                            elif userAction == "!scissors" and kalinAction == "!paper":
                                userWins += 1
                                print("Three.")
                                time.sleep(1)
                                print("You show Scissors and Kalin shows Paper. You win.")
                                time.sleep(2)
                                print("The result is:")
                                time.sleep(1)
                                print(characterName + ": " + str(userWins) + " wins.")
                                print("Kalin: " + str(kalinWins) + " wins.")
                                time.sleep(2)
                                if userWins == neccesaryWins:
                                    print("*** You win.")
                                    time.sleep(2)
                                    print("*** Kalin passes you the 2 coins. ***")
                                    time.sleep(2)
                                    characterCoins = int(characterCoins) + 2
                                    time.sleep(2)
                                    print_coins()
                                    time.sleep(2)
                                    print("*** After winning the game you return back to Mesta.")
                                    return
                                else:
                                    continue
                            elif userAction == "!scissors" and kalinAction == "!paper":
                                kalinWins += 1
                                print("Three.")
                                time.sleep(1)
                                print("You show Scissors and Kalin shows Paper. You lose.")
                                time.sleep(1)
                                print("The result is:")
                                time.sleep(1)
                                print(characterName + ": " + str(userWins) + " wins.")
                                print("Kalin: " + str(kalinWins) + " wins.")
                                time.sleep(2)
                                if kalinWins == neccesaryWins:
                                    print(" You lose.")
                                    time.sleep(1)
                                    print("Kalin: Haaa! Take that!")
                                    time.sleep(2)
                                    print("Kalin: I win.")
                                    time.sleep(2)
                                    print("*** Kalin says bye and grins widely as he leaves up towards Bolero.")
                                    time.sleep(2)
                                    print("*** After losing the game you return back to Mesta.")
                                    return
                                else:
                                    continue
                        else:    
                            print("This is an invalid command.")
                            time.sleep(1)
                            continue

        ####################################### QUESTS HIGH REP #####################################################

        #### GORSKIQ QUEST ####
        def gorskiq_quest():
            global characterReputation
            global characterLevel
            global characterStrength
            global characterAgility
            global characterIntelligence
            global characterCoins
            global characterName
            time.sleep(2)
            print(characterName + ": Hey Gorski, what's up?")
            time.sleep(3)
            print("GORSKIQ: All good and you, razboinik?")
            time.sleep(3)
            print(characterName + ": Just hangin' around.")
            time.sleep(3)
            print("GORSKIQ: I see you're bored. Why don't you go and buy me a bottle of Zytnia vodka?")
            time.sleep(3)
            print("*** WOULD YOU LIKE TO ACCEPT THIS QUEST? ***")
            while True:
                acceptQuest = input("Type in !yes to accept or !no to refuse!")
                if acceptQuest == "!yes":
                    time.sleep(3)
                    print(characterName + ":No probs, Gorski! Which store do you want me to buy the Zytnia from?")
                    time.sleep(3)
                    print("GORSKIQ: I don't care where you buy it from. Here's 15 coins, should be enough.")
                    time.sleep(3)
                    print("*** GORSKIQ passes over 15 coins to you.")
                    time.sleep(2)
                    characterCoins = int(characterCoins) + 15
                    print("You've received 15 coins. You now have ", characterCoins, "coins.")
                    time.sleep(3)
                    print(characterName + ": Okay, I'll be right back, Gorski, you wait for me here.")
                    time.sleep(3)
                    print("GORSKIQ: Good! And don't keep me waiting for too long.")
                    time.sleep(3)
                    print("*** WHICH STORE WOULD YOU GO TO? THE SHIT-THROWER OR THE PRIMO")
                    while True:
                        whichStore = input("Select by typing either !thrower or !theprimo")
                        if whichStore == "!thrower":
                            time.sleep(2)
                            print("*** YOU START WALKING TOWARDS THE SHIT THROWER")
                            time.sleep(3)
                            print("*** HOW SILLY OF YOU-... THE SHIT THROWER IS FARTHER THAN THE PRIMO ***")
                            time.sleep(3)
                            print("*** YOU GAIN 1 AGILITY AND YOU LOSE 1 INTELLIGENCE ***")
                            characterAgility = int(characterAgility) + 1
                            characterIntelligence = int(characterIntelligence) - 1
                            time.sleep(0.5)
                            print_agility()
                            time.sleep(0.5)
                            print_intelligence()
                            time.sleep(2)
                            print(
                                "*** YOU KEEP WALKING BUT SOON START TO WONDER-.. WHAT IF I BURN GORSKIQ AND KEEP THE COINS FOR MYSELF? ***")
                            while True:
                                burnGorskiq = input(
                                    "Type !burn to burn Gorskiq and keep the coins for yourself or !dontburn to be loyal and buy the old alchoholic a vodka.")
                                if burnGorskiq == "!burn":
                                    print("*** YOU BURN GORSKIQ AND LOSE 25 REPUTATION-... ***")
                                    characterReputation = int(characterReputation) - 25
                                    time.sleep(2)
                                    print_reputation()
                                    time.sleep(2)
                                    print("*** BUT YOU KEEP 15 COINS ***")
                                    return
                                elif burnGorskiq == "!dontburn":
                                    print("*** YOU APPROACH THE SHIT THROWER BUT YOU WONDER AGAIN ***")
                                    time.sleep(3)
                                    print("***", characterName,
                                          ", ARE YOU SURE THAT YOU DON'T WANT TO KEEP 15 COINS FOR YOURSELF ***")
                                    time.sleep(3)
                                    while True:
                                        burnGorskiq = input(
                                            "Type !burn to burn Gorskiq and keep the coins for yourself or !dontburn to be loyal and buy the old alchoholic a vodka.")
                                        if burnGorskiq == "!burn":
                                            print("*** YOU BURN GORSKIQ AND LOSE 25 REPUTATION-... ***")
                                            characterReputation = int(characterReputation) - 25
                                            time.sleep(2)
                                            print("Your reputation now is:", characterReputation)
                                            time.sleep(2)
                                            print("*** BUT YOU KEEP 15 COINS ***")
                                            return
                                        elif burnGorskiq == "!dontburn":
                                            print(
                                                "*** YOU ENTER THE SHIT THROWER, LOOK AT THE BOTTLE OF ZYTNIA AND CHECK THE PRICE TAG! IT SAYS - 15 COINS! ***")
                                            time.sleep(3)
                                            print(
                                                characterName + ": Damn, the old creep didn't even give me 1 extra coin-.. what's in it for me if not the change?")
                                            time.sleep(3)
                                            print(
                                                "*** YOU LOOK AROUND AND YOU NOTICE THAT THERE'S NOBODY AT THE COUNTER AT THAT MOMENT ***")
                                            time.sleep(3)
                                            print(
                                                "*** WOULD YOU LEAVE THE BOTTLE ON THE SHELF, EXIT AND BURN GORSKIQ? ***")
                                            time.sleep(3)
                                            print(
                                                "*** OR MAYBE YOU'LL STEAL THE BOTTLE, KEEP GORSKIQ HAPPY AND KEEP THE COINS IN YOUR POCKET? ***")
                                            time.sleep(3)
                                            print(
                                                "*** OR WOULD YOU POLITELY WAIT FOR THE CASHIER TO PAY FOR THE VODKA? ***")
                                            time.sleep(3)
                                            while True:
                                                whatToDo = input(
                                                    "Type !burn to burn Gorskiq, !steal to steal the bottle or !pay to politely wait for the cashier")
                                                if whatToDo == "!burn":
                                                    print("*** YOU BURN GORSKIQ AND LOSE 25 REPUTATION-... ***")
                                                    characterReputation = int(characterReputation) - 25
                                                    time.sleep(2)
                                                    print_reputation()
                                                    time.sleep(2)
                                                    print("*** BUT YOU KEEP 15 COINS AND GAIN 1 LEVEL ***")
                                                    characterLevel = int(characterLevel) + 1
                                                    print_level()
                                                    return
                                                elif whatToDo == "!steal":
                                                    print("*** YOU STEAL THE BOTTLE AND HEAD BACK TO GORSKIQ ***")
                                                    time.sleep(3)
                                                    print(
                                                        "*** WHILE WALKING YOU WILL HAVE THE OPTION TO KEEP THE BOTTLE AS AN ITEM AND DO SOMETHING WITH IT, BUT THAT'LL HAPPEN IN THE NEXT EXPANSION")
                                                    time.sleep(3)
                                                    print("*** GORSKIQ THANKS YOU FOR THE FAVOR ***")
                                                    time.sleep(2)
                                                    print("*** YOU GAIN 25 REPUTATION, 1 AGILITY POINT AND 1 LEVEL ***")
                                                    characterReputation = int(characterReputation) + 25
                                                    characterAgility = int(characterAgility) + 1
                                                    characterLevel = int(characterLevel) + 1
                                                    time.sleep(1)
                                                    print_reputation()
                                                    time.sleep(0.5)
                                                    print_agility()
                                                    time.sleep(0.5)
                                                    print_level()
                                                    time.sleep(0.5)
                                                    return
                                                elif whatToDo == "!pay":
                                                    print(
                                                        "*** YOU WAIT FOR THE CASHIER AND PAY 15 COINS FOR A BOTTLE OF ZYTNIA ***")
                                                    characterCoins = int(characterCoins) - 15
                                                    print("Your coins now are:", characterCoins)
                                                    time.sleep(2.5)
                                                    print(
                                                        "*** YOU HEAD BACK TO GORSKIQ AND GIVE HIM THE BOTTLE OF ZYTNIA***")
                                                    time.sleep(3)
                                                    print(
                                                        "*** WHILE WALKING YOU WILL HAVE THE OPTION TO KEEP THE BOTTLE AS AN ITEM AND DO SOMETHING WITH IT, BUT THAT'LL HAPPEN IN THE NEXT EXPANSION")
                                                    time.sleep(3)
                                                    print("*** GORSKIQ THANKS YOU FOR THE FAVOR ***")
                                                    time.sleep(2)
                                                    print("***  YOU GAIN 25 REPUTATION AND 1 LEVEL ***")
                                                    characterLevel = int(characterLevel) + 1
                                                    characterReputation = int(characterReputation) + 25
                                                    print_reputation()
                                                    time.sleep(0.5)
                                                    print_level()
                                                    time.sleep(0.5)
                                                    return
                                                else:
                                                    print(
                                                        "This is an invalid command! Didn't you learn already after all this playing?")
                                                    continue
                                    else:
                                        print(
                                            "This is an invalid command! Didn't you learn already after all this playing?")
                                        continue
                        elif whichStore == "!theprimo":
                            time.sleep(2)
                            print("*** YOU START WALKING TOWARDS THE PRIMO")
                            time.sleep(3)
                            print(
                                "*** SMART MOVE-... THE PRIMO IS THE CLOSER THAN THE SHIT THROWER FROM YOUR LOCATION ***")
                            time.sleep(3)
                            print("*** YOU GAIN 1 INTELLIGENCE")
                            characterIntelligence = int(characterIntelligence) + 1
                            time.sleep(0.5)
                            print_intelligence()
                            time.sleep(2)
                            print(
                                "*** YOU KEEP WALKING BUT SOON START TO WONDER-.. WHAT IF I BURN GORSKIQ AND KEEP THE COINS FOR MYSELF? ***")
                            while True:
                                burnGorskiq = input(
                                    "Type !burn to burn Gorskiq and keep the coins for yourself or !dontburn to be loyal and buy the old alchoholic a vodka.")
                                if burnGorskiq == "!burn":
                                    print("*** YOU BURN GORSKIQ AND LOSE 25 REPUTATION-... ***")
                                    characterReputation = int(characterReputation) - 25
                                    time.sleep(1)
                                    print_reputation()
                                    time.sleep(1)
                                    print("*** BUT YOU KEEP 15 COINS ***")
                                    return
                                elif burnGorskiq == "!dontburn":
                                    print("*** YOU APPROACH THE PRIMO BUT YOU WONDER AGAIN ***")
                                    time.sleep(3)
                                    print("***", characterName,
                                          ", ARE YOU SURE THAT YOU DON'T WANT TO KEEP 15 COINS FOR YOURSELF ***")
                                    time.sleep(3)
                                    while True:
                                        burnGorskiq = input(
                                            "Type !burn to burn Gorskiq and keep the coins for yourself or !dontburn to be loyal and buy the old alchoholic a vodka.")
                                        if burnGorskiq == "!burn":
                                            print("*** YOU BURN GORSKIQ AND LOSE 25 REPUTATION-... ***")
                                            characterReputation = int(characterReputation) - 25
                                            time.sleep(1)
                                            print_reputation()
                                            time.sleep(1)
                                            print("*** BUT YOU KEEP 15 COINS ***")
                                            return
                                        elif burnGorskiq == "!dontburn":
                                            print(
                                                "*** YOU ENTER THE PRIMO, LOOK AT THE BOTTLE OF ZYTNIA AND CHECK THE PRICE TAG! IT SAYS - 15 COINS! ***")
                                            time.sleep(3)
                                            print(
                                                characterName + ": Damn, the old creep didn't even give me 1 extra coin-.. what's in it for me if not the change?")
                                            time.sleep(3)
                                            print(
                                                "*** YOU LOOK AROUND AND YOU NOTICE THAT THERE'S NOBODY AT THE COUNTER AT THAT MOMENT ***")
                                            time.sleep(3)
                                            print(
                                                "*** WOULD YOU LEAVE THE BOTTLE ON THE SHELF, EXIT AND BURN GORSKIQ? ***")
                                            time.sleep(3)
                                            print(
                                                "*** OR MAYBE YOU'LL STEAL THE BOTTLE, KEEP GORSKIQ HAPPY AND KEEP THE COINS IN YOUR POCKET? ***")
                                            time.sleep(3)
                                            print(
                                                "*** OR WOULD YOU POLITELY WAIT FOR THE CASHIER TO PAY FOR THE VODKA? ***")
                                            time.sleep(3)
                                            while True:
                                                whatToDo = input(
                                                    "Type !burn to burn Gorskiq, !steal to steal the bottle or !pay to politely wait for the cashier")
                                                if whatToDo == "!burn":
                                                    print("*** YOU BURN GORSKIQ AND LOSE 25 REPUTATION-... ***")
                                                    characterReputation = int(characterReputation) - 25
                                                    time.sleep(1.5)
                                                    print_reputation()
                                                    time.sleep(1.5)
                                                    print("*** BUT YOU KEEP 15 COINS AND GAIN 1 LEVEL ***")
                                                    characterLevel = int(characterLevel) + 1
                                                    print_level()
                                                    time.sleep(0.5)
                                                    return
                                                elif whatToDo == "!steal":
                                                    print("*** YOU STEAL THE BOTTLE AND HEAD BACK TO GORSKIQ ***")
                                                    time.sleep(3)
                                                    print(
                                                        "*** WHILE WALKING YOU WILL HAVE THE OPTION TO KEEP THE BOTTLE AS AN ITEM AND DO SOMETHING WITH IT, BUT THAT'LL HAPPEN IN THE NEXT EXPANSION")
                                                    time.sleep(3)
                                                    print("*** GORSKIQ THANKS YOU FOR THE FAVOR ***")
                                                    time.sleep(2)
                                                    print("*** YOU GAIN 25 REPUTATION, 1 AGILITY POINT AND 1 LEVEL ***")
                                                    characterReputation = int(characterReputation) + 25
                                                    characterAgility = int(characterAgility) + 1
                                                    characterLevel = int(characterLevel) + 1
                                                    time.sleep(1)
                                                    print_reputation()
                                                    time.sleep(0.5)
                                                    print_agility()
                                                    time.sleep(0.5)
                                                    print_level()
                                                    time.sleep(0.5)
                                                    return
                                                elif whatToDo == "!pay":
                                                    print(
                                                        "*** YOU WAIT FOR THE CASHIER AND PAY 15 COINS FOR A BOTTLE OF ZYTNIA ***")
                                                    characterCoins = int(characterCoins) - 15
                                                    print("Your coins now are:", characterCoins)
                                                    time.sleep(3)
                                                    print(
                                                        "*** YOU HEAD BACK TO GORSKIQ AND GIVE HIM THE BOTTLE OF ZYTNIA***")
                                                    time.sleep(3)
                                                    print(
                                                        "*** WHILE WALKING YOU WILL HAVE THE OPTION TO KEEP THE BOTTLE AS AN ITEM AND DO SOMETHING WITH IT, BUT THAT'LL HAPPEN IN THE NEXT EXPANSION")
                                                    time.sleep(3)
                                                    print("*** GORSKIQ THANKS YOU FOR THE FAVOR ***")
                                                    time.sleep(3)
                                                    print("*** YOU GAIN 25 REPUTATION AND 1 LEVEL ***")
                                                    characterLevel = int(characterLevel) + 1
                                                    characterReputation = int(characterReputation) + 25
                                                    print_reputation()
                                                    time.sleep(0.5)
                                                    print_level()
                                                    time.sleep(0.5)
                                                    return
                                                else:
                                                    print(
                                                        "This is an invalid command! Didn't you learn already after all this playing?")
                                                    continue
                                    else:
                                        print(
                                            "This is an invalid command! Didn't you learn already after all this playing?")
                                        continue
                        else:
                            print("This is an invalid command! Didn't you learn already after all this playing?")
                            continue
                elif acceptQuest == "!no":
                    time.sleep(2)
                    print(characterName + ": Sorry Gorski, but not today. I got better things to do right now.")
                    time.sleep(1)
                    print("*** YOU TURN AROUND AND YOU WALK BACK TOWARDS THE BENCH IN FRONT OF ACHO ***")
                    return
                else:
                    print(
                        "This is an invalid command! !yes - to accept and !no to refuse. Didn't you learn already after all this playing?")
                    continue


        login_function()  # Using the Login function to verify user's name and password.
        time.sleep(1)
        welcome()  # Welcoming the player to the game.
        time.sleep(2)
        show_location_and_reputation(characterLocation, characterReputation)  # Showing the player the location and reputation.

        while (True):
            playerMove = input("Please make a move!")
            player_move_function(playerMove)


        ### THE LIAR QUEST ####

    elif loginRegisterOrRecover == "!register":
        register_account()
        continue
    elif loginRegisterOrRecover == "!recover":
        recover_account()
        continue
    else:
        print("That's an invalid command!")
        continue

if __name__ == '__main__':
    main()



















