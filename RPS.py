import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

player_choice = input("Enter... \n1 for ROCK\n2 for PAPER\n3 for SCISSORS\n\n You Entered: ")
player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("You must Enter 1,2 or 3")

computer_choice = random.choice("123")
computer = int(computer_choice)

print("")
print("You Chose " + str(RPS(player)).replace("RPS.",""))
print("Python Chose " + str(RPS(computer)).replace("RPS.",""))
print("")

if player == 1 and computer == 3:
    print("😊 YOU WIN")
elif player == 2 and computer == 1:
    print("😊 YOU WIN")
elif player == 3 and computer == 2:
    print("😊 YOU WIN")
elif player == computer:
    print("😯 TIE GAME")
else:
    print("🐍 PYTHON WINS")