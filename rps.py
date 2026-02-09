import os
import random

computer = random.randint(1,3)

os.system("clear")

user = int(input("1. Rock\n2. Paper\n3. Scissors\nChoose (1-3):"))
print("Computer: ", computer, "User: ", user)

if user == computer:
    print("Draw!")
if user == 1 and computer == 2:
    print("Computer Wins!")
if user == 1 and computer == 3:
    print("User Wins!")
if user == 2 and computer == 1:
    print("User Wins!")
if user == 2 and computer == 3:
    print("Computer Wins!")
if user == 3 and computer == 2:
    print("User Wins!")
if user == 3 and computer == 1:
    print("Computer Wins!")