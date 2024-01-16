import time
import os
from turtle import Screen, Turtle
from bricks import Bricks
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from lives import ScoreBoardLives
from record import ScoreBoardRecord
import pyglet


points = 0
x = 410
y = 250
idx = 0
color = ["red", "green", "orange"]
bricks = []
t = 0.02
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

    screen = Screen()

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

        if ball.ycor() < -280:
            game_sound('music/life.wav')
            ball.reset_ball()
            screen.tracer(1)
            scoreboard_lives.game_lives()

        if scoreboard_lives.lives == 0:
            game_sound('music/game_over.wav')
            scoreboard.game_over()
            game_is_on = False

        if ball.ycor() > 275:
            game_sound('music/up.mp3')
            ball.bounce_y()

        if ball.distance(paddle) < paddle_distance and ball.ycor() < -230:
            screen.tracer(0)
            screen.update()
            game_sound('music/ding.wav')
            ball.bounce_y()

        if ball.xcor() > 360 or ball.xcor() < -360:
            game_sound('music/sides.wav')
            ball.bounce_x()

        for brick in bricks:
            if ball.distance(brick) < 30:
                points += 1
                with open('points.txt', mode='r') as dt:
                    record = dt.read()
                    print(record)
                if points > int(record):
                    with open('points.txt', mode='w') as dt:
                        dt.write(f'{points}')
                game_sound('music/glass_break.wav')
                scoreboard.point()
                brick.color('black')
                bricks.remove(brick)
                ball.bounce_y()

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

            new_game()



            # screen.update()
            # level += 1
            # print(game_speed)
            # if game_speed > 0.02:
            #     game_speed -= 0.02
            # else:
            #     game_speed = 0.03
            # time.sleep(5)
            # screen.reset()
            # if scoreboard_lives.lives != 0:
            #     game(game_speed)

    screen.exitonclick()


new_game()

