from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.goto(0, -280)

    def go_right(self):
        if not self.pos() > (300, -260):
            new_x = self.xcor() + 80
            self.goto(new_x, self.ycor())

    def go_left(self):
        if not self.pos() < (-300, -260):
            new_x = self.xcor() - 80
            # print(self.pos())
            self.goto(new_x, self.ycor())
