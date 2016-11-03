import turtle
import signal
import time


def draw1Triangle(aT, p1, p2, p3):
        aT.up()
        aT.goto(p1)
        aT.down()
        aT.goto(p2)
        aT.goto(p3)
        aT.goto(p1)


def midPoint(p1, p2):
        return (p1[0]+p2[0])/2.0, (p1[1]+p2[1])/2.0


def draw3Triangles (myT, p1, p2, p3, depth):
        if depth > 0:
                draw3Triangles(myT, p1, midPoint(p1,p2), midPoint(p1,p3), depth-1)
                draw3Triangles(myT, p2, midPoint(p2,p3), midPoint(p2,p1), depth-1)
                draw3Triangles(myT, p3, midPoint(p3,p1), midPoint(p3,p2), depth-1)
        else:
                draw1Triangle(myT, p1, p2, p3)


def drawNestedTriangles(len, depth):
        p1 = (0, len)
        p2 = (len, -len)
        p3 = (-len, -len)
        t = turtle.Turtle()
        draw3Triangles(t, p1, p2, p3, depth)
        t.up()
        t.goto((0,len))
        t.right(90)

def gr3():
        s = turtle.Screen()
        drawNestedTriangles(200,0)
        time.sleep(5)
        s.clear()
        drawNestedTriangles(200,1)
        time.sleep(5)
        s.clear()
        drawNestedTriangles(200,2)
        signal.pause()

gr3()
