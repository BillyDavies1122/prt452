import random
#The lower limit of the randomiser
LOWER_LIMIT = 1
#the upper limit of the randomiser
UPPER_LIMIT = 100
def generateRandNum():
    randNum = random.randint(LOWER_LIMIT,UPPER_LIMIT)
    return randNum

def numericCheck(userInput):
    if userInput.isnumeric() == False:
        return True

def correctRange(userInput):
    if int(userInput) < LOWER_LIMIT or int(userInput) > UPPER_LIMIT:
        return True

def userQuit(userInput):
    if userInput == 'q':
        return True

def checkUserAnswer(userInput,randNum,total):
    if randNum == int(userInput):
        total = total + 1
        return True

def numbersGame():
    randNum = generateRandNum()
    total = 0
    while True:
        userInput = input("Enter a number: ")
        if  userQuit(userInput):
            print("You tried ",total," times")
            print("Thanks for playing!")
            break
        elif numericCheck(userInput):
             print("Please enter a number")
        elif correctRange(userInput):
             print("Number outside the correct range")
        elif checkUserAnswer(userInput,randNum,total):
            print("You did it and it only took you ",total," Tries")
            break
        else:
            print("You failed please Guess again",randNum)
            total = total + 1

while __name__ == "__main__":
    numbersGame()
    break
