#This is a random number game
import random as r

name = (input("Enter the number :"))

if(name.isdigit()):
    name = int(name)

    if(name < 0):
         print("Enter the value greater then 0 next time")
         quit()

else:
    print("Type a number next time")
    quit()


cal = r.randint(0,name)

guess = 0

while True:

    guess += 1

    choice_macth = input("Make a guess")

    if(choice_macth.isdigit()):
        choice_macth = int(choice_macth)

    else:
        print("Type a number next time")
        continue

    if(choice_macth == cal):
        print("You got it")
        break
    elif(choice_macth > cal):
        print("You guess a large number")
    else:
        print("You guess the very small number")

print(f"You guess is in {guess} guess")
