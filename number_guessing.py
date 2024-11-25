import random

print("Welcome to Number Guessing!")
print("~~~~~~~~~~~~~~~~~~")

print("IMPORTANT REMINDER: You only have 5 attempts, consume it all and you lose")

playing_status = input("Do you want to play?: ").lower()

if playing_status == "yes":

    while True:
            number = random.randrange(11)
            score = 5
            guesses = []
            while score != 0:

                guess = int(input("Guess a number: "))
                guesses.append(guess)

                if guess == number:
                    print("You are correct")
                    break
                else:
                    print("Your guess is incorrect")
                    print("~~~~~~~~~~~~~")
                    score -= 1
                    if score == 0:
                        print("You do not have any attempts left")
                        print(f"The random number is {number}")
                        break
                    else:
                        print(f"You only have {score} attempts left")

            print(f"These are your guesses: {guesses}")

            play_again = input("Wanna keep playing? ").lower()

            if play_again != "yes":
                print("Thank you for playing!")
                break
else:
    print("Thank you!")
    quit()



