import os, random, time

class Colours:
    Normal = "\033[37m"
    Correct = "\033[32m"
    Incorrect = "\033[31m"

DifficultyNumber = "0"

def Reset(Index):
    os.system("CLS")
    if DifficultyNumber == "0":
        print(Colours.Normal + "-- Math Game -- " + Index + "\n")
    elif DifficultyNumber == "1":
        print(Colours.Normal + "-- Math Game (Easy) -- " + Index + "\n")
    elif DifficultyNumber == "2":
        print(Colours.Normal + "-- Math Game (Medium) -- " + Index + "\n")
    elif DifficultyNumber == "3":
        print(Colours.Normal + "-- Math Game (Hard) -- " + Index + "\n")

Reset("")

print(Colours.Normal + "Easy (1)\nMedium (2)\nHard (3)")
DifficultyNumber = input(Colours.Normal + "Difficulty: ")

Symbols = []
NumberRange = []
AnswerRange = 0
Negatives = False

if DifficultyNumber == "1":
    Symbols = ["+", "-"]
    NumberRange = [10, 20]
    AnswerRange = [20, 20]                   
    Negatives = False
elif DifficultyNumber == "2":
    Symbols = ["+", "-", "x", "/"]
    NumberRange = [20, 50, 10, 100]
    AnswerRange = [100, 100, 100, 100]
    Negatives = False
elif DifficultyNumber == "3":
    Symbols = ["+", "-", "x", "/"]
    NumberRange = [100, 100, 12, 144]
    AnswerRange = [100, 100, 144, 144]
    Negatives = True

def GetRandomNumber(NumRange, Symbol):
    if Negatives == True:
        RandomNumber = random.randint(-NumRange, NumRange)
        while RandomNumber == 0 or ((Symbol == "x" or Symbol == "/") and (RandomNumber == 1 or RandomNumber == -1)):
            RandomNumber = random.randint(-NumRange, NumRange)
        return RandomNumber
    else:
        RandomNumber = random.randint(1, NumRange)
        while (Symbol == "x" or Symbol == "/") and RandomNumber == 1:
            RandomNumber = random.randint(1, NumRange)
        return RandomNumber

def GetRandomSymbol():
    RandomIndex = random.randint(0, len(Symbols) - 1)
    return Symbols[RandomIndex], NumberRange[RandomIndex], AnswerRange[RandomIndex]

StartTime = time.time()

Score = 0

for Index in range(20):
    Reset(str(Index + 1) + "/20")
    Question = ""
    Symbol, NumRange, AnsRange = GetRandomSymbol()
    Answer = AnsRange * 2
    Number1 = 0
    Number2 = 0
    while Answer == 0 or Answer > AnsRange or Answer < -AnsRange or (Negatives == False and Answer < 0) or Answer != round(Answer) or (Symbol == "/" and (Answer == 1 or Answer == -1)):
        Number1 = GetRandomNumber(NumRange, Symbol)
        Number2 = GetRandomNumber(NumRange, Symbol)
        if Symbol == "+":
            Answer = Number1 + Number2
        elif Symbol == "-":
            Answer = Number1 - Number2
        elif Symbol == "x":
            Answer = Number1 * Number2
        else:
            if Number1 > Number2:
                Answer = Number1 / Number2
            else:
                Answer = Number2 / Number1
                Number3 = Number2
                Number2 = Number1
                Number1 = Number3
    Guess = input(Colours.Normal + str(Number1) + " " + Symbol + " " + str(Number2) + " = ")
    if Guess == str(int(Answer)):
        print(Colours.Correct + "Correct!")
        Score += 1
        time.sleep(1)
    else:
        print(Colours.Incorrect + "Incorrect!\nThe correct answer is " + str(int(Answer)))
        time.sleep(2)

Reset("")

TotalTime = round(time.time() - StartTime)
BestTime = 0

if DifficultyNumber == "1":
    BestTime = 55
elif DifficultyNumber == "2":
    BestTime = 65
elif DifficultyNumber == "3":
    BestTime = 85

Points = 100 - (TotalTime - BestTime)/(BestTime * 2) * 100
if Points > 100:
    Points = 100
elif Points < 50:
    Points = 50
Points = Points * Score/20

print(Colours.Normal + "You got " + str(Score) + "/20 in " + str(TotalTime) + "s")
print("Mathematician Score: " + str(round(Points)) + "/100")
time.sleep(10000)
