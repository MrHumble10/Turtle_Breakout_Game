# def check_collision_with_walls():
#     if ball.xcor() < -375 and ball.xcor() > 375:
#         ball.bounce_y()

    # def collision_with_paddle():
    #     print(paddle.xcor(), ball.xcor())
    #     if paddle.distance(ball) < paddle_distance and ball.ycor() < -250:
    #         print('HIT')
    #
    #         if paddle.xcor() < ball.xcor():
    #             if ball.x_move == -10:
    #                 ball.bounce_y()
    #             else:
    #                 ball.bounce_y()
    #                 ball.bounce_x()
    #             return
    #
    #         elif paddle.xcor() > ball.xcor():
    #             if ball.x_move == -10:
    #                 ball.bounce_y()
    #                 ball.bounce_x()
    #             else:
    #                 ball.bounce_y()
    #             return
    #
    #         elif paddle.xcor() == ball.xcor():
    #             ball.bounce_y()
    #             return

#
# def collision_with_paddle():
#     print(paddle.xcor(), ball.xcor())
#     if paddle.distance(ball) < paddle_distance and ball.ycor() < -250:
#         print('HIT')
#         # if paddle.xcor() > 0:
#         if paddle.xcor() < ball.xcor() and ball.x_move == -10:
#             ball.bounce_y()
#             return
#         else:
#             if paddle.xcor() < ball.xcor() and ball.x_move == 10:
#                 ball.bounce_y()
#                 ball.bounce_x()
#                 return
#
#         if paddle.xcor() > ball.xcor() and ball.x_move == -10:
#             ball.bounce_y()
#             ball.bounce_x()
#             return
#         else:
#             if paddle.xcor() > ball.xcor() and ball.x_move == 10:
#                 ball.bounce_y()
#                 return
#         # elif paddle.xcor() < 0:
#         if paddle.xcor() == ball.xcor():
#             ball.bounce_y()
#             return












# def collision_with_paddle():
#     print(paddle.xcor(), ball.xcor())
#     if paddle.distance(ball) < paddle_distance and ball.ycor() < -250:
#         print('HIT')
#         if paddle.xcor() > 0:
#             if ball.xcor() > paddle.xcor():
#                 ball.bounce_y()
#                 ball.bounce_x()
#                 return
#             else:
#                 ball.bounce_y()
#                 return
#
#         elif paddle.xcor() < 0:
#             if ball.xcor() < paddle.xcor():
#                 ball.bounce_y()
#                 ball.bounce_x()
#                 return
#             else:
#                 ball.bounce_y()
#                 return
#         else:
#             if ball.xcor() > paddle.xcor():
#                 ball.bounce_y()
#                 ball.bounce_x()
#                 return
#             elif ball.xcor() < paddle.xcor():
#                 ball.bounce_y()
#                 ball.bounce_x()
#                 return
#             else:
#                 ball.bounce_y()
