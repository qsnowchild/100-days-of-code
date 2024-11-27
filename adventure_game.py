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
    print("Dark Frame")


gold_bank = 0
inventory = []

def movement():
    global gold_bank
    global inventory
    # pick_path = input("Left or Right?: L/R: ").lower()
    while True:
        pick_path = input("Left or Right?: L/R: ").lower()
        if pick_path == "l":
            print("You have obtained 500 gold!")
            gold_bank += 500
            print(gold_bank)
            break
        elif pick_path == "r":
            print("You have obtained a Shiny Sword!")
            inventory.append("Shiny Sword")
            print(inventory)
            break
        else:
            print("Please input a valid choice L/R")


def action():
    fight_nego = input("Do you wanna fight the monster? Y/N: ").lower()
    if fight_nego == "y":
        enemy1()
        print("Swings a sword")

playgame = input("Do you wanna play? Y/N: ").lower()
if playgame != "y":
    quit()

print("Welcome Go Forth and Find the Treasure!!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(f"Your current finds are {gold_bank} and {inventory}")

chooseapath = int(input("Each cave leads to different places, pick one! 1 / 2 / 3: "))

if chooseapath == 1:
    sea()
elif chooseapath == 2:
    cave()
else:
    ice()


