print("Welcome to the Quiz Game!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:

    playing_status = input("Want to play?: ").lower()
    if playing_status != "yes":
        break

    score = 0
    print("Here is the first question")

    print("What does CPU stand for?")
    answer1 = input("Enter your answer: ").lower()
    if answer1 == "central processing unit":
        score += 1

    print("What job has the highest DPS in ROO?")
    answer2 = input("Enter your answer: ").lower()

    if answer2 == "stalker":
        score += 1

    print(f"Your total score is {score}")






