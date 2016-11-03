import sys
from turtle import Turtle, mainloop


class KeysMouseEvents:
    def __init__(self):
        super().__init__()
        self.T = Turtle()
        self.screen = self.T.getscreen()
        self.screen.onkey(self.clear, "c")
        self.screen.onkey(self.quit, "q")
        self.screen.onclick(self.draw_fig)
        self.screen.listen()

    def clear(self):
        self.T.screen.clear()
        self.__init__()

    @staticmethod
    def quit():
        sys.exit(0)

    def draw_fig(self, x, y):
        print(x, y)
        self.T.goto(x, y)
        self.T.circle(20)

    def main(self):
        mainloop()


def gr0():
    draw = KeysMouseEvents()
    draw.main()

gr0()
