x = 1
y = 1

s = "(S)outh"
n = "(N)orth"
w = "(W)est"
e = "(E)ast"
o = " or "

while (x != 3) | (y != 1):
    if y == 1:
        print("You can travel " + n)
        k = input("Direction ")
        if k == "N" or k == "n":
            y += 1
        else:
            print("Not a valid direction")
    elif (x == 2 and y == 2) or (x==3 and y ==3):
        print("You can travel " + w + o + s)
        k = input("Direction ")
        if k == "w" or k == "W":
            x -= 1
        elif k == "s" or k == "S":
           y -=1
        else:
            print("Not a valid direction")
    elif (x == 1 and y == 2):
        print("You can travel " + n + o + s + o + e)
        k = input("Direction ")
        if k == "e" or k == "E":
            x += 1
        elif k == "s" or k == "S":
            y -= 1 
        elif k == "n" or k == "N":
            y += 1
        else:
            print("Not a valid direction")
    elif (x == 3 and y == 2):
        print("You can travel " + n + o + s)
        k = input("Direction ")
        if k == "s" or k == "S":
            y -= 1 
        elif k == "n" or k == "N":
            y += 1
        else:
            print("Not a valid direction")
    elif (x == 1 and y == 3):
        print("You can travel " + e + o + s)
        k = input("Direction ")
        if k == "s" or k == "S":
            y -= 1
        elif k == "e" or k == "E":
            x += 1
        else:
            print("Not a valid direction")
    elif (x == 2 and y == 3):
        print("You can travel " + e + o + w)
        k = input("Direction ")
        if k == "w" or k == "W":
            x -= 1 
        elif k == "e" or k == "E":
            x += 1
        else:
            print("Not a valid direction")



print("Victory")

    






