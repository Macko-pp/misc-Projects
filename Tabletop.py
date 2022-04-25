import random
import os

choice = input("Tool: ")

#Vars--------------------------------------------------------------------------

dice = random.randint(1, 6)
dice2 = random.randint(1, 6), random.randint(1, 6)
coin = random.randint(1, 2)
rps = random.randint(1, 3)

#Dice--------------------------------------------------------------------------

if choice == "dice" or choice == "Dice":
    print("(" + str(dice) + ")")

elif choice == "dice2" or choice == "dice 2" or choice == "Dice 2" or choice == "2 dice" or choice == "2 Dice":
    print(dice2)

#Coin--------------------------------------------------------------------------

elif choice == "coin":
    if coin == 1:
        print("Heads")
    
    elif coin == 2:
        print("Tails")

#Rock-Paper-Siccors------------------------------------------------------------

elif choice == "rps" or choice == "Rps" or choice == "Rock-paper-scissors" or choice == "Rock-Paper-Siccors":
    shoot = input("Choice: ")
    print("1")
    os.system("sleep 0.5")
    print("2")
    os.system("sleep 0.5")
    print("3")
    os.system("sleep 0.5")
    print("Rock")
    os.system("sleep 0.5")
    print("Paper")
    os.system("sleep 0.5")
    print("Scissors")
    os.system("sleep 0.5")
    print("Shoot!")
    os.system("sleep 0.5")
    if rps == 1:
        print("Rock 🪨")
        os.system("sleep 0.5")
    elif rps == 2:
        print("Paper 📄")
        os.system("sleep 0.5")
    elif rps == 3:
        print("Scissors ✂️")
        os.system("sleep 0.5")

    if shoot == "rock" or shoot == "Rock":
        if rps == 1:
            print("Tie :|")
            os.system("sleep 0.5")
        elif rps == 2:
            print("You Lose :(")
            os.system("sleep 0.5")
        elif rps == 3:
            print("You Win :)")
            os.system("sleep 0.5")
    elif shoot == "paper" or shoot == "Paper":
        if rps == 1:
            print("You Win :)")
            os.system("sleep 0.5")
        elif rps == 2:
            print("Tie :|")
            os.system("sleep 0.5")
        elif rps == 3:
            print("You Lose :(")
            os.system("sleep 0.5")
    elif shoot == "scissors" or shoot == "Scissors":
        if rps == 1:
            print("You Lose :(")
            os.system("sleep 0.5")
        elif rps == 2:
            print("You Win :)")
            os.system("sleep 0.5")
        elif rps == 3:
            print("Tie :|")
            os.system("sleep 0.5")

else:
    print("Action not available")
