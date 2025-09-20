#this is rock paper scissor game
import random

#This is a score value to recode score
user_score = 0
comp_score = 0

#This is a list of string that we want to play
option = ["rock","paper","scissor"]

#This is continues Condition that is continues until it break
while True:
 

 user_input = input("Enter the Rock/Paper/Scissor or Q for quite:").lower()

#This is a code to quite the game 
 if(user_input == "q"):
    break
 

#This is a code in which user enter wronge value or write numerical value
 if user_input not in option:
      continue
 
 #This is a random value genrate file
 rand = random.randint(0,2)

 #This is a where computer pick from option

 Computer_pick = option[rand]

 print("Computer Pick",Computer_pick + ".")

 #This is a situtation where you can win or lose

 if(user_input == "rock" and Computer_pick == "scissor"):
    print("You Won!")
    user_score += 1

 elif(user_input == "paper" and Computer_pick == "rock"):
    print("You Won!")
    user_score += 1

 elif(user_input == "scissor" and Computer_pick == "paper"):
    print("You Won!")
    user_score += 1

 else:
    print("You lose!")
    comp_score += 1

#THis is print of final score after a match
print(f"You won {user_score} Times")
print(f"The computer won {comp_score} Times")
print("Goodbye")
 

 


