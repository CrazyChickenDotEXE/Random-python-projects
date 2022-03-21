import time as t
import turtle as tr
# import packages


tr.speed(int(input('Enter turtle speed (WARNING: Use fast speed if you want to draw a circle!)')))
# user defined speed


def TurtleDrawSquare(size):
    tr.forward(size)
    tr.right(90)
    tr.forward(size)
    tr.right(90)
    tr.forward(size)
    tr.right(90)
    tr.forward(size)
    return
# Draw a square
def TurtleDrawCircle(size):
    i = 1
    while i <= 360:
        tr.forward(size)
        tr.right(1)
        i += 1
    return
# Draw a circle
def TurtleDrawTriangle(size):
    tr.forward(size)
    tr.left(120)
    tr.forward(size)
    tr.left(120)
    tr.forward(size)
    tr.left(120)
    return
# Draw a triangle
s = tr.getscreen()
i = 1
while i == 1:

    print('Type "tri" for triangle, "cir" for circle, or "sq" for square.  EXT to exit.')
    usrshape = input()
    if usrshape == 'tri':
        TurtleDrawTriangle(int(input('Size of triangle:')))
    elif usrshape == 'cir':
        TurtleDrawCircle(int(input('Size of circle:')))
    elif usrshape == 'sq':
        TurtleDrawSquare(int(input('Size of square:')))
    elif usershape == "EXT":
        break

print('Exiting...')
exit()
