from turtle import Turtle


class ScoreBoardLives(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.lives = 3
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.color('white')
        self.goto(290, -200)
        self.write(f"Your Lives: {self.lives}",align='center',  font=('Elefant', 10, 'bold'))

    def game_lives(self):
        self.lives -= 1

        self.update_lives()



