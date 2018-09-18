
def movementx(char):
    if char == "e" or char == "E":
        x = 1
    elif char == "w" or char == "W":
        x = -1
    else:
        x = 0
    return x

def movementy(char):
    if char == "n" or char == "N":
        y = 1
    elif char == "s" or char =="S":
        y = -1
    else:
        y = 0
    return y

x = 1
y = 1

s = "(S)outh"
n = "(N)orth"
w = "(W)est"
e = "(E)ast"
o = " or "

while (x != 3) and (y != 1):
    if y == 1:
        print("You can travel " + n)
        k = input("Direction ")
        if k == "N" or k == "n":
            move = movementy(k)
            y += move
        else:
            print("Not a valid direction")
    elif (x == 2 and y == 2) or (x==3 and y ==3):
        print("You can travel " + w + o + s)
        k = input("Direction ")
        if k == "w" or k == "W":
            move = movementx(k)
            x += move
        elif k == "s" or k == "S":
            move = movementy(k)
            y += move
        else:
            print("Not a valid direction")
    elif (x == 1 and y == 2):
        print("You can travel " + n + o + s + o + e)
        k = input("Direction ")
        if k == "e" or k == "E":
            move = movementx(k)
            x += move
        elif k == "s" or k == "S":
            move = movementy(k)
            y += move
        elif k == "n" or k == "N":
            move = movementy(k)
            y += move
        else:
            print("Not a valid direction")
    elif (x == 3 and y == 2):
        print("You can travel " + n + o + s)
        k = input("Direction ")
        if k == "s" or k == "S":
            move = movementy(k)
            y += move
        elif k == "n" or k == "N":
            move = movementy(k)
            y += move
        else:
            print("Not a valid direction")
    elif (x == 1 and y == 3):
        print("You can travel " + e + o + s)
        k = input("Direction ")
        if k == "s" or k == "S":
            move = movementy(k)
            y += move
        elif k == "e" or k == "E":
            move = movementx(k)
            x += move
        else:
            print("Not a valid direction")
    elif (x == 2 and y == 3):
        print("You can travel " + e + o + w)
        k = input("Direction ")
        if k == "w" or k == "W":
            move = movementx(k)
            x += move
        elif k == "e" or k == "E":
            move = movementx(k)
            x += move
        else:
            print("Not a valid direction")



print("Victory")

    






