import random

print("Welcome to Rock Paper Scissor Game! ")
print("~~~~~~~~~~~~~~~~~~~~~~~")

user = 0
computer = 0

rounds = int(input("How many rounds do you want?: ")) +1

options = ["rock", "paper", "scissor"]

while rounds > 0:
    print("~~~~~~~~~~~~~")
    print(f"Round {rounds -1} ")
    userinput = input("Rock, Paper, Scissor / Q = to quit: ").lower()
    if userinput == "q" or userinput not in options:
        print("Game Aborted")
        break
    if userinput in options:
        print(f"You picked: {userinput}")

    randomnum = random.randint(0,2)

    computerpick = options[randomnum]
    print(f"Computer picked: {computerpick}")

    rounds -= 1

    if userinput == "rock" and computerpick == "scissor":
        user += 1
    elif userinput == "paper" and computerpick == "rock":
        user += 1
    elif userinput == "scissor" and computerpick == "paper":
        user += 1
    elif userinput == computerpick:
        print("Draw")
    else:
        computer +=1

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if user > computer:
    print(f"You won, your score is {user} vs computer {computer}")
elif user == computer:
    print("Draw")
elif user < computer:
    print(f"You lose, your score is {user} vs computer {computer}")
else:
    print("Game Aborted")



