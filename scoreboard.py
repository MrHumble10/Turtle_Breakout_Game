from turtle import Turtle
import os


class ScoreBoard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.record = score
        self.score = score
        self.lives = 3
        self.update_points()

    def update_points(self):
        self.clear()
        self.color('green')
        self.goto(300, -230)
        self.write(f"Current Score: {self.score}", align='center', font=('Elefant', 10, 'bold'))

    def point(self):
        self.score += 1
        self.update_points()

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write(f"Game Over", align='center', font=('Elefant', 70, 'bold'))

    def winner(self, num):
        self.clear()
        self.goto(0, -100)
        self.color('light blue')
        self.write(f"You Won\nLevel {num}", align='center', font=('Elefant', 70, 'bold'))
        self.hideturtle()


    def best_record(self):
        self.clear()
        self.color('green')
        self.goto(290, -200)
        self.write(f"Best record: {self.record}", align='center', font=('Elefant', 10, 'bold'))


class ScoreBoardLives(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.lives = 3
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.color('green')
        self.goto(290, -200)
        self.write(f"Your Lives: {self.lives}",align='center',  font=('Elefant', 10, 'bold'))

    def game_lives(self):
        self.lives -= 1

        self.update_lives()


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
        self.color('green')
        self.goto(300, -170)
        self.write(f"Best Record: {self.record}", align='center',  font=('Elefant', 10, 'bold'))



