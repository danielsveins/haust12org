import random
from pics import *
from functions import *

'''
Moguleikar..
       0        1     2     3     4     5     6         7
[E|EO|EO2|EO3,O|X|W,O|X|B,O|X|W,O|X|B,O|X|W,O|X|B,E|EX|EX2|EX3]


'''
iterations = int(raw_input("How many random nannon boards?"))

a = [E,EO,EO2,EO3]
b = [O,X,W]
c = [O,X,B]
d = [O,X,W]
e = [O,X,B]
f = [O,X,W]
g = [O,X,B]
h = [E,EX,EX2,EX3]

j = [a,b,c,d,e,f,g,h]

for x in range(iterations):
    board = []
    for y in range(7):
        if((y == 0) or (y == 7)):
            board.append(j[y][random.randint(0,3)])
        else:
            board.append(j[y][random.randint(0,2)])
    drawboard(board)
