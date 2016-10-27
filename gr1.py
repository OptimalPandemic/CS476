import turtle
import signal


def drawSquare (myTurtle, sideLength):
        for i in range(4):
                myTurtle.forward(sideLength)
                myTurtle.right(90)  # side i

def drawSquareFill (myTurtle, sideLength):
        myTurtle.begin_fill()
        for i in range(4):
                myTurtle.forward(sideLength)
                myTurtle.right(90)  # side i
        myTurtle.end_fill()

def drawPolygon (myTurtle, sideLength, numSides):
        turnAngle=360/numSides
        for i in range (numSides):
                myTurtle.forward(sideLength)
                myTurtle.right(turnAngle)


def drawCircle(myTurtle, radius):
        circum = 2*3.14*radius
        sideLength = circum/360
        drawPolygon(myTurtle, sideLength, 360)


def gr1():
        t = turtle.Turtle()
        s = turtle.Screen()
        s.bgcolor('light green')

        t.shape("square")
        t.shape("square")
        t.color("blue")
        t.width(2)
        t.speed(2)
        drawSquare(t, 150)

        t.shape("arrow")
        t.color("red")
        t.width(4)
        t.speed(4)
        drawPolygon(t, 100, 8)

        t.shape("turtle")
        t.color("purple")
        t.width(6)
        t.speed(0)
        drawCircle(t, 100)
        t.hideturtle()
        t.shape("circle")
        drawSquareFill(t, 50)
        t.showturtle()

        t.color("red")
        t.begin_fill()
        t.circle(50)
        t.end_fill()

        t.up()
        t.back(200)
        t.dot()
        t.forward(50)
        t.write("DONE")
        t.forward(50)
        t.hideturtle()
        t.dot()
        signal.pause()

gr1()
