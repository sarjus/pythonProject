import math
import turtle
board = turtle.Turtle()
board.forward(100)  # draw base
board.left(90)
board.forward(100)
board.left(135)
x= math.sqrt(100**2+100**2) #C2 = a2 + b2
board.forward(x)
turtle.done()
