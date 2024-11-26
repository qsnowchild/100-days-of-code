def sea():
    print("Welcome to the Red Sea!")
    return

def cave():
    print("Welcome to the Glast Heim")
    return

def ice():
    print("Welcome to the Icy Garm")
    return



playgame = input("Do you wanna play? Y/N: ").lower()
if playgame != "y":
    quit()

print("Welcome Go Forth and Find the Treasure!!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

chooseapath = int(input("Each cave leads to different places, pick one! 1 / 2 / 3: "))

if chooseapath == 1:
    sea()
elif chooseapath == 2:
    cave()
else:
    ice()


