def sea():
    print("Welcome to the Red Sea!")
    movement()
    action()
    return

def cave():
    print("Welcome to the Glast Heim")
    movement()
    action()
    return

def ice():
    print("Welcome to the Icy Garm")
    movement()
    action()
    return

#create an enemy
def enemy1():
    return 1200

#character
def character():
    return char_points


char_points = 0

def movement():
    global char_points
    while True:
        pick_path = input("Left or Right?: L/R: ").lower()
        if pick_path == "l":
            print("You have obtained 500 points!")
            char_points += 600
            break
        elif pick_path == "r":
            print("You have obtained 300 points!")
            char_points += 300
            break
        else:
            print("Please input a valid choice L/R")

def action():
    global char_points
    fight_nego = input(f"Do you wanna fight the monster? Y/N: Remember, the enemy has {enemy1()} points: ").lower()
    if fight_nego == "y":
        print("Omega slash!!!!!!!!!!")
        calc()
    if fight_nego == "n":
        print("Runs away, ill get back to you soon")
        explore = input("Do you wanna explore other caves first?: ").lower()
        if explore == "y":
            firstmove()
        else:
            quit()



playgame = input("Do you wanna play? Y/N: ").lower()
if playgame != "y":
    quit()

def calc():
    char_points = character()
    enemy_points = enemy1()

    if char_points > enemy_points:
        print("You won")
    else:
        print("You lost")

print("Welcome Go Forth and Find the Treasure!!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def firstmove():
    chooseapath = int(input("Each cave leads to different places, pick one! 1 / 2 / 3: "))

    if chooseapath == 1:
        sea()
    elif chooseapath == 2:
        cave()
    else:
        ice()

firstmove()


