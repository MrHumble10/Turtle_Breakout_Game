import time
import os
from turtle import Screen, Turtle
from bricks import Bricks
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard, ScoreBoardLives, ScoreBoardRecord
import pyglet
from tkinter import TclError


points = 0
x = 410
y = 250
idx = 0
color = ["red", "green", "orange"]
bricks = []
level = 0
t = 0.04
paddle_size = 10
paddle_distance = 110
if not os.path.isfile('points.txt'):
    with open('points.txt', mode='w') as p:
        points = p.write(str(0))


def new_game():
    global bricks, level, t, idx, x, y, bricks,paddle_size, paddle_distance, points
    idx = 0
    x = 410
    y = 250
    bricks = []

    def game_sound(sound):
        music = pyglet.resource.media(f'{sound}')
        music.play()

    def wall():
        global x, y, color, idx, bricks
        for i in range(1, 61):
            x -= 75
            bricks.append(Bricks(color=color[idx], position=(x, y)))
            if i % 10 == 0:

                y -= 35
                x = 410
            if i % 20 == 0:
                idx += 1
        game_sound('music/start.wav')
        # game_sound('music/glass_break.wav')

    def collision_with_paddle():
        print(paddle.xcor(), ball.xcor())
        if paddle.distance(ball) < paddle_distance and ball.ycor() < -250:
            print('HIT')

            if paddle.xcor() < ball.xcor():
                if ball.x_move == -10:
                    ball.bounce_y()
                else:
                    print(f'distance right is {ball.distance(paddle)}')
                    ball.bounce_y()
                    ball.bounce_x()
                return

            elif paddle.xcor() > ball.xcor():
                if ball.x_move == -10:
                    print(f'distance left is   {ball.distance(paddle)}')

                    ball.bounce_y()
                    ball.bounce_x()
                else:
                    ball.bounce_y()
                return

            elif paddle.xcor() == ball.xcor():
                ball.bounce_y()
                return

    screen = Screen()
    screen.title("Blackout Game")
    screen.bgcolor("Black")
    screen.setup(width=800, height=600)

    screen.tracer(0)
    wall()

    paddle = Paddle()
    paddle.shapesize(stretch_wid=1, stretch_len=paddle_size)
    ball = Ball()
    screen.listen()

    screen.onkey(paddle.go_right, "Right")
    screen.onkey(paddle.go_left, "Left")
    screen.update()
    ScoreBoardRecord()
    scoreboard = ScoreBoard(points)
    scoreboard_lives = ScoreBoardLives()
    screen.update()

    # def game(game_speed):
    #     global level
    time.sleep(3)
    game_is_on = True
    screen.tracer(1)
    while game_is_on:
        time.sleep(t)
        screen.update()
        ball.move()

        if ball.ycor() < -275:
            game_sound('music/life.wav')
            ball.reset_ball()
            screen.tracer(1)
            scoreboard_lives.game_lives()

        if scoreboard_lives.lives == 0:
            game_sound('music/game_over.wav')
            scoreboard.game_over()
            game_is_on = False
            ball.reset_ball()

        if ball.ycor() > 275:
            game_sound('music/up.mp3')
            ball.bounce_y()

            game_sound('music/ding.wav')

        elif ball.xcor() > 380 or ball.xcor() < -380:
            game_sound('music/sides.wav')
            ball.bounce_x()

        for brick in bricks:
            if ball.distance(brick) < 30:
                points += 1
                screen.tracer(0)
                screen.update()
                with open('points.txt', mode='r') as dt:
                    record = dt.read()
                    # print(record)
                if points > int(record):
                    with open('points.txt', mode='w') as dt:
                        dt.write(f'{points}')
                game_sound('music/glass_break.wav')
                scoreboard.point()
                brick.color('black')
                bricks.remove(brick)
                ball.bounce_y()

        collision_with_paddle()

        if len(bricks) == 0:
            game_sound('music/win.wav')
            screen.reset()
            scoreboard.winner(level)
            level += 1
            if not t < 0.02:
                t -= 0.009
            else:
                t = 0.005
                if not paddle_size == 2:
                    paddle_size -= 1
                if not paddle_distance == 35:
                    paddle_distance -= 10

            game_is_on = False
            print(t)
            scoreboard.winner(level)
            screen.update()
            time.sleep(3)
            screen.reset()
            try:
                new_game()
            except OSError:
                pass





    screen.exitonclick()


try:
    new_game()
except TclError:
    pass

