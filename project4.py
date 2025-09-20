#This is choice your own game

name = input("Enter your name :")

print(f"Wellcome to Advanture Game :{name}")

start = input("You enter the jungle and you walk there is to road where you want to go left or right (left/Right)").lower()

if(start == "left"):
        answer = input("you come to near a river what you want to do swim or pass the river (swim/pass)").lower()
        if(answer == "swim"):
               print("Their are aligater in water! so you lose")

        elif(answer == "pass"):
               print("The lion is drinking water near the river the lion attack you you lose")
        else:
               print("You enter the invalid option you lose") 
               
elif(start == "right"):
        answer = input("you came near to lion cave what you want to d now go to cave or pass by the cave (cave/pass)").lower()
        if(answer == "cave"):
               answer = input("you enter the cave their is two way left or right (left/Right)")
               if(answer.lower() == "left"):
                    print("your go near to lion and lion attack you and you lose")
               elif(answer.lower() == "right"):
                    print("You get out other side of cave there you see a village you won")
               else:
                    print("You enter the invalid option you lose")
        elif(answer == "pass"):
               print("you pass the cave there is a trap and you fell into trap you lose")
        else:
               print("You enter the invalid option you lose") 
else:
    print("You enter the invalid option you lose") 
