import random


while __name__ == "__main__":
    randNum = random.randint(1,100)
    total = 0
    while True:
        userInput = input("Enter a number: ")
        if userInput == 'q':
            print("You tried ",total," times")
            print("Thanks for playing!")
            break
        elif userInput.isnumeric() == False:
            print("Please enter a number")
        elif int(userInput) < 1 or int(userInput) > 100:
            print("Number outside the correct range")
        elif randNum == int(userInput):
            total = total + 1
            print("You did it and it only took you ",total," Tries")
            break
        else:
            print("You failed please Guess again",randNum)
            total = total + 1
    break
