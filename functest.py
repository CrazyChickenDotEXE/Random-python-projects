import time as t
import turtle as tr

def TurtleDrawSquare(size):
    tr.forward(size)
    tr.right(90)
    tr.forward(size)
    tr.right(90)
    tr.forward(size)
    tr.right(90)
    tr.forward(size)
    return

s = tr.getscreen()

print("Drawing square...")
TurtleDrawSquare(200)
