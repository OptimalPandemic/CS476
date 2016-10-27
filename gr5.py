import sys
from turtle import Turtle, mainloop


class KeysMouseEvents:

    def __init__(self):
        super().__init__()
        self.T = Turtle()
        self.T.screen.setup(width=600, height=400, startx=300, starty=200)
        self.T.pensize(4)
        self.T.color("blue")
        self.screen = self.T.getscreen()
        self.distance = 10
        self.turn = 15
        self.screen.onkey(self.fwd10, "Right")
        self.screen.onkey(self.bkwd10, "Left")
        self.screen.onkey(self.left15, "Up")
        self.screen.onkey(self.right15, "Down")
        self.screen.onkey(self.clear, "c")
        self.screen.onkey(self.quit, "q")
        self.screen.onclick(self.drawdot)
        self.screen.listen()

    def fwd10(self):
        self.T.forward(self.distance)

    def bkwd10(self):
        self.T.backward(self.distance)

    def left15(self):
        self.T.left(self.turn)

    def right15(self):
        self.T.right(self.turn)

    def clear(self):
        self.T.screen.clear()
        self.__init__()

    def quit(self):
        self.T.screen.bye()
        sys.exit(0)

    def drawdot(self, x, y):
        print(x, y)
        self.T.goto(x, y)
        self.T.dot()

    def main(self):
        mainloop()


def gr5():
    draw = KeysMouseEvents()
    draw.main()

gr5()