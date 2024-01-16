from turtle import Turtle


class ScoreBoardRecord(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        with open('points.txt', mode='r') as dt:
            self.record = dt.read()
        self.update_record()

    def update_record(self):
        self.clear()
        self.color('white')
        self.goto(290, -170)
        self.write(f"Best Record: {self.record}", align='center',  font=('Elefant', 10, 'bold'))



