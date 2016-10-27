import random
import math
import turtle
import signal


def PiApprox(numDarts):
        wn = turtle.Screen()
        drawingT = turtle.Turtle()

        wn.setworldcoordinates(-2, -2, 2, 2)

        drawingT.up()
        drawingT.goto(-1, 0)
        drawingT.down()
        drawingT.goto(1, 0)

        drawingT.up()
        drawingT.goto(0, 1)
        drawingT.down()
        drawingT.goto(0, -1)

        circle = 0
        drawingT.up()
        drawingT.hideturtle()

        for i in range(numDarts):
                x=random.random()
                y=random.random()

                d=math.sqrt(x**2+y**2)

                drawingT.goto(x,y)

                if d<=1:
                        circle=circle+1
                        drawingT.color("blue")
                else:
                        drawingT.color("red")

                drawingT.dot()

        pi= (circle/numDarts) * 4
        drawingT.goto(-.5, .5)
        drawingT.write("DONE", font=("Arial", 16, "normal"))
        drawingT.goto(-.5, .3)
        drawingT.write(pi, font=("Arial", 16, "normal"))
        print('done: approximate value of pi:')
        print(pi)


def gr4():
        PiApprox(100)
        signal.pause()


gr4()
