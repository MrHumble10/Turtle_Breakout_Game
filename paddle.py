from turtle import Turtle

MOVE_DISTANCE = 80
class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=3.3)
        self.penup()
        self.goto(0, -280)

    def go_right(self):
        # if not self.pos() > (300, -260):
        self.forward(MOVE_DISTANCE)

    def go_left(self):
        # if not self.pos() < (-300, -260):
        self.backward(MOVE_DISTANCE)
