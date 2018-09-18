x = 1
y = 1

s = "(S)outh"
n = "(N)orth"
w = "(W)est"
e = "(E)ast"
o = " or "

while (x != 3) | (y != 1):
    if y == 1:
        print("You can travel: " + n + ".")
        k = input("Direction: ")
        while (k != 'N') and (k != 'n'):
            print("Not a valid direction!")
            k = input("Direction: ")
        if k == "N" or k == "n":
            y += 1
    elif (x == 2 and y == 2) or (x==3 and y ==3):
        print("You can travel: " + s + o + w + ".")
        k = input("Direction: ")
        while (k != 'w') and (k != 'W') and (k != 's') and (k != 'S'):
            print("Not a valid direction!")
            k = input("Direction: ")
        if k == "w" or k == "W":
            x -= 1
        elif k == "s" or k == "S":
           y -=1
    elif (x == 1 and y == 2):
        print("You can travel: " + n + o + e + o + s + ".")
        k = input("Direction: ")
        while (k != 'e') and (k != "E") and (k != "s") and (k != "S") and (k != "N") and (k != "n"):
            print("Not a valid direction!")
            k = input("Direction: ")
        if k == "e" or k == "E":
            x += 1
        elif k == "s" or k == "S":
            y -= 1 
        elif k == "n" or k == "N":
            y += 1
        
    elif (x == 3 and y == 2):
        print("You can travel: " + n + o + s + ".")
        k = input("Direction: ")
        while (k != "n") and (k != "N") and (k != "S") and (k != "s"):
            print("Not a valid direction!")
            k = input("Direction: ")
        if k == "s" or k == "S":
            y -= 1 
        elif k == "n" or k == "N":
            y += 1
    elif (x == 1 and y == 3):
        print("You can travel: " + e + o + s + ".")
        k = input("Direction: ")
        while (k != "e") and (k != "E") and (k != "S") and (k != "s"):
            print("Not a valid direction!")
            k = input("Direction: ")
        if k == "s" or k == "S":
            y -= 1
        elif k == "e" or k == "E":
            x += 1
    elif (x == 2 and y == 3):
        print("You can travel: " + e + o + w + ".")
        k = input("Direction: ")
        while (k != "e") and (k != "E") and (k != "W") and (k != "w"):
            print("Not a valid direction!")
            k = input("Direction: ")
        if k == "w" or k == "W":
            x -= 1 
        elif k == "e" or k == "E":
            x += 1



print("Victory!")

    






