#This is a prject one of game

print("welcome to the my computer")

#this is a name taken code

name = input("Enter your name :").upper()

print(f"Asslam o alikum! {name}")
#This is a game Enter Code
play = input("Do you Want to play a game :) ").lower()

#this is a score 
score = 0


if(play != "yes"):
    quit()

#this is a condition to make game until the end of code
while True:

    name = input("Enter the English form of 1 :").lower()
    if(name == "one"):
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    name = input("Enter the English form of 2 :").lower()
    if(name == "two"):
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    name = input("Enter the English form of 3 :").lower()
    if(name == "three"):
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    name = input("Enter the English form of 4 :").lower()
    if(name == "four"):
        print("Correct")
        score += 1
    else:
        print("Incorrect")

#this is a score call code
    print(f"Your total score is {score}")
    
#This is a choice situation to restart or quit game 
    name = input("Choice Quite = Q & Restart = R :").lower()
    if(name == "q"):
        break
    elif(name == "r"):
        continue
    else:
        print("Invalid")
        break
    
