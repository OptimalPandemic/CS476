import turtle
import signal


def drawSquare (myTurtle, sideLength):
        for i in range(4):
                myTurtle.forward(sideLength)
                myTurtle.right(90)  # side i


def nestedSquares(T, side):
        if side >= 10:
                drawSquare(T, side)
                nestedSquares(T, side-10)


def gr2():
        t = turtle.Turtle()
        nestedSquares(t, 200)
        signal.pause()

gr2()
