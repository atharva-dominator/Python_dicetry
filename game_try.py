print("          Welcome to a game of Bet!      ")
print("Instructions are as follows:---")
print("You have to choose a number from 1 to 6 if the number you choose is greater tha the one that I choose you will lose alternatively if the number matches the one i choose yu still lose!! GOOD LUCK........ ")
import random
b=[1,2,3,4,5,6]

comscr=0     #initially
userscr=0    #initially
chances = 10
no_of_chances= 0
while no_of_chances < chances:
    a = int(input("Choose a number on dice--> "))
    c=random.choice(b)
    print("I choose: ",c)

    if a==c:
        print("You lose!")
        comscr=+1
    elif a<c:
        print("You lose!")
        comscr+=1
    else:
        print("You win")
        userscr=+1
    
    no_of_chances=no_of_chances+1
    print(f"{chances-no_of_chances} chances left")

print("Game over")
if comscr > userscr:
    print("You lost the bet!")
elif comscr < userscr:
    print("You won UwU")
else:
    print("It's a draw..sed")

print(f"You score: {human_points} || Computer score: {computer_points}")
   