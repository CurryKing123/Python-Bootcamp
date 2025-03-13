print("Welcome to Treasure Island")

path1 = input("You're at a crossroad. On the left there is a clear path, on the right the path is covered in blood. Where do you want to go: left or right?").lower()
if (path1 == "right"):
    print("Game Over")
elif (path1 == "left"):
    path2 = input("There is a raging river. You could swim to get across or wait to see if there is another way to cross. What do you do: swim or wait?").lower()
    if (path2 == "swim"):
        print("Game Over")
    elif (path2 == "wait"):
        path3 = input("There are 3 doors. Which door do you go through: red, blue, or yellow?").lower()
        if (path3 == "red" | "blue"):
            print("Game Over")
        elif (path3 == "yellow"):
            print("You Win!")
        else:
            print("That is not a valid response")
    else: 
        print("That is not a valid response")
else:
    print("That is not a valid response")
