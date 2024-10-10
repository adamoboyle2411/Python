import os, random, time

class Colours:
    Normal = "\033[37m"
    Correct = "\033[32m"
    Incorrect = "\033[31m"

def Reset():
    os.system("CLS")
    print(Colours.Normal + "-- Hangman --\n")

Words = ["bikini", "puzzle", "jazz", "galaxy", "strength", "junior", "will", "torn", "bully", "employment", "undecided", "depression", "loyalty", "hamburger", "establishment", "retro", "aligned", "cup", "premade", "jumper", "explanation", "rhino", "wherever", "quieter", "wooly", "editor", "roman", "thought", "youth", "underscore", "ill", "operator", "philosophical", "amazed", "slicer", "demented", "frosty", "gigantic", "honorable", "jammed", "kit", "layer", "zebra", "xylophone", "chocolate", "vile", "boredom", "naughty", "monstrosity"]

def GetRandomWord():
    RandomIndex = random.randint(0, len(Words) - 1)
    return Words[RandomIndex]

def CleanWord(Word):
    NewWord = ""
    for Character in Word:
        if Character.isalpha():
            NewWord += Character.lower()
        elif Character == " " and NewWord[-1] != "/":
            NewWord += "/"
    return NewWord

Player1 = ["", 0]
Player2 = ["", 0]

Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def PrintHangman(WrongLetters):
    Reset()
    if WrongLetters == 0:
        print("\n"*6)
    elif WrongLetters == 1:
        print("______\n| / |\n|/\n|\n|\n|\n")
    elif WrongLetters == 2:
        print("______\n| / |\n|/  O\n|\n|\n|\n")
    elif WrongLetters == 3:
        print("______\n| / |\n|/  O\n|   |\n|\n|\n")
    elif WrongLetters == 4:
        print("______\n| / |\n|/  O\n|  /|\n|\n|\n")
    elif WrongLetters == 5:
        print("______\n| / |\n|/  O\n|  /|\ \n|\n|\n")
    elif WrongLetters == 6:
        print("______\n| / |\n|/  O\n|  /|\ \n|  /\n|\n")
    elif WrongLetters == 7:
        print("______\n| / |\n|/  O\n|  /|\ \n|  / \ \n|\n")

def PrintGuess(Word, RemainingLetters):
    Guess = ""
    for Character in Word:
        Guessed = True
        for Letter in RemainingLetters:
            if Character == Letter:
                Guessed = False
                break
        if Guessed == True:
            print(Colours.Normal + Character, end = " ")
            Guess += Character
        else:
            print(Colours.Normal + "_", end = " ")
            Guess += "_"
    print("\n")
    return Guess

def PrintLetters(RemainingLetters):
    for Index in range(26):
        Guessed = True
        for RemainingLetter in RemainingLetters:
            if Letters[Index] == RemainingLetter:
                Guessed = False
                break
        if Guessed == True:
            Present = False
            for Character in Word:
                if Character == Letters[Index]:
                    Present = True
                    break
            if Present == True:
                print(Colours.Correct + Letters[Index], end = " ")
            else:
                print(Colours.Incorrect + Letters[Index], end = " ")
        else:
            print(Colours.Normal + Letters[Index], end = " ")
        if Index == 12:
            print(Colours.Normal + "         " + Player1[0] + ": " + str(Player1[1]) + "\n")
    print(Colours.Normal + "         " + Player2[0] + ": " + str(Player2[1]) + "\n")

def GuessWord(Word, GuessingPlayer, OtherPlayer):
    Word = CleanWord(Word)
    RemainingLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Guess = ""
    WrongLetters = 0
    while Guess != Word:
        PrintHangman(WrongLetters)
        if WrongLetters == 7:
            for Character in Word:
                print(Colours.Normal + Character, end = " ")
            print("\n")
            OtherPlayer[1] += 1
            PrintLetters(RemainingLetters)
            print(Colours.Normal + GuessingPlayer[0] + " loses!")
            break
        Guess = PrintGuess(Word, RemainingLetters)
        if Guess == Word:
            GuessingPlayer[1] += 1
            PrintLetters(RemainingLetters)
            print(Colours.Normal + GuessingPlayer[0] + " wins!")
        else:
            PrintLetters(RemainingLetters)
            GuessedLetter = input("Guess a letter: ")
            if GuessedLetter.isalpha():
                GuessedLetter = GuessedLetter.lower()
            for Letter in RemainingLetters:
                if GuessedLetter == Letter:
                    RemainingLetters.remove(Letter)
                    Present = False
                    for Character in Word:
                        if Character == Letter:
                            Present = True
                            break
                    if Present == False:
                        WrongLetters += 1
                    break

Reset()

print(Colours.Normal + "One player (1)\nTwo players (2)")
ModeNumber = input("Game mode: ")

Reset()

if ModeNumber == "1":
    Player1[0] = input("Player: ").title()
    Player2[0] = input("Opponent: ").title()
else:
    Player1[0] = input("Player 1: ").title()
    Player2[0] = input("Player 2: ").title()

Reset()

print("Enter the length of the match:")
FirstTo = int(input("First to "))

def EndGame():
    if Player1[1] >= FirstTo:
        Reset()
        print(Player1[0] + ": " + str(Player1[1]))
        print(Player2[0] + ": " + str(Player2[1]) + "\n")
        print(Player1[0] + " wins the match!")
        time.sleep(1000)
    elif Player2[1] >= FirstTo:
        Reset()
        print(Player1[0] + ": " + str(Player1[1]))
        print(Player2[0] + ": " + str(Player2[1]) + "\n")
        print(Player2[0] + " wins the match!")
        time.sleep(1000)

if ModeNumber == "1":
    while True:
        Word = GetRandomWord()
        GuessWord(Word, Player1, Player2)
        time.sleep(2)
        EndGame()
elif ModeNumber == "2":
    while True:
        Reset()
        print("Enter a word for " + Player2[0] + " to guess:\n")
        Word = input()
        GuessWord(Word, Player2, Player1)
        time.sleep(2)
        Reset()
        print("Enter a word for " + Player1[0] + " to guess:\n")
        Word = input()
        GuessWord(Word, Player1, Player2)
        time.sleep(2)
        EndGame()
