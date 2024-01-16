from turtle import Turtle

class Bricks(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(1, 3)
        self.penup()
        self.goto(position)



    # def go_up(self):
    #     new_y = self.ycor() + 20
    #     self.goto(self.xcor(), new_y)
    #
    # def go_down(self):
    #     new_y = self.ycor() - 20
    #     self.goto(self.xcor(), new_y)
