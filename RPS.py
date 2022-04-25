import os
import random

rps = random.randint(1, 3)

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

if shoot == "rock" or shoot == "Rock" or shoot == "r" or shoot == "R":
    if rps == 1:
        print("Tie :|")
        os.system("sleep 0.5")
    elif rps == 2:
        print("You Lose :(")
        os.system("sleep 0.5")
    elif rps == 3:
        print("You Win :)")
        os.system("sleep 0.5")
elif shoot == "paper" or shoot == "Paper" or shoot == "p" or shoot == "P":
    if rps == 1:
        print("You Win :)")
        os.system("sleep 0.5")
    elif rps == 2:
        print("Tie :|")
        os.system("sleep 0.5")
    elif rps == 3:
        print("You Lose :(")
        os.system("sleep 0.5")
elif shoot == "scissors" or shoot == "Scissors" or shoot == "s" or shoot == "S":
    if rps == 1:
        print("You Lose :(")
        os.system("sleep 0.5")
    elif rps == 2:
        print("You Win :)")
        os.system("sleep 0.5")
    elif rps == 3:
        print("Tie :|")
        os.system("sleep 0.5")
