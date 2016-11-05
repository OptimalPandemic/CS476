import sys
import math
import random
from turtle import Turtle, mainloop


class Drawer(object):

    def __init__(self):
        super(Drawer, self).__init__()
        self.t = Turtle()
        self.t.hideturtle()
        self.screen = self.t.getscreen()
        self.screen.setup(width=600, height=400, startx=300, starty=200)
        self.t.pensize(1)
        self.t.color("black")
        self.screen.onkey(self.clear, "c")
        self.screen.onkey(self.quit, "q")
        self.a_x = 0
        self.a_y = 0
        self.b_x = 0
        self.b_y = 0
        self.radius = 0
        self.t.speed(0)
        self.screen.listen()
        self.screen.onclick(self.set_a)

    def clear(self):
        self.screen.clear()
        self.__init__()

    def quit(self):
        self.screen.bye()
        sys.exit(0)

    def set_a(self, x, y):
        self.t.penup()
        self.a_x = x
        self.a_y = y
        print(x, y)
        self.t.goto(x, y)
        self.t.dot()
        self.screen.onclick(self.set_b)

    # This function continues execution after set_a
    def set_b(self, x, y):
        self.t.fillcolor(choose_color())
        self.b_x = x
        self.b_y = y
        print(x, y)
        self.t.goto(x, y)
        self.t.dot()
        self.radius = math.hypot(self.a_x - self.b_x, self.a_y - self.b_y)
        self.t.goto(self.a_x, self.a_y - self.radius)
        self.t.setheading(0)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(self.radius)
        self.t.end_fill()
        self.t.penup()
        self.t.goto(self.a_x, self.a_y + 1.23 * self.radius)
        self.t.pendown()
        self.t.fillcolor(choose_color())
        self.t.begin_fill()
        self.t.right(36)  # half a full angle
        self.t.forward(1.452 * self.radius)
        for i in range(4):
            self.t.right(72)
            self.t.forward(1.452 * self.radius)  # formula for side of pentagon

        self.t.end_fill()
        self.t.penup()
        self.t.goto(self.a_x, self.a_y + self.radius)
        self.t.fillcolor(choose_color())
        self.t.begin_fill()
        for i in range(5):
            self.t.right(72)
            self.t.forward(1.18 * self.radius)

        self.t.end_fill()
        self.t.pendown()
        self.__init__()

    def main(self):
        mainloop()


def choose_color():
    colors = {"red", "green", "blue", "yellow", "white", "pink", "brown", "purple", "gray", "orange"}
    return random.choice(tuple(colors))


def draw():
    drawer = Drawer()
    drawer.main()

draw()
