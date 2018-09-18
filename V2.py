
def possiblem(x , y):
    attir = "(S)outh (N)orth (W)est (E)ast"
    s, n, w, e = attir.split()
    if y == 1:
        return n + "."
    elif x == 1:
        if y == 2:
            return n + " or " + e + " or " + s + "."
        if y == 3:
            return e + " or " + s + "."
    elif x == 2:
        if y == 2:
            return s + " or " + w + "."
        if y == 3:
            return e + " or " + w + "."
    elif x == 3:
        if y == 2:
            return n + " or " + s + "."
        if y == 3:
            return s + " or " + w + "."
    else:
        return ""

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
n = "(N)orth"
s = "(S)outh"
e = "(E)ast"
w = "(W)est"

while (x != 3) | (y != 1):
    a =""
    b=""
    c = ""
    d =""
    print("You can travel: " + possiblem(x, y))
    move = input("Direction: ")
    if n in possiblem(x,y):
        a = n
    if s in possiblem(x,y):
        b = s
    if e in possiblem(x,y):
        c = e
    if w in possiblem(x,y):
        d = w
    while (move.upper() != a[1:2]) and (move.upper() != b[1:2]) and (move.upper() != c[1:2]) and (move.upper() != d[1:2]):
        print("Not a valid direction!")
        move = input("Direction: ")
    x += movementx(move)
    y += movementy(move)
print("Victory!")

    






