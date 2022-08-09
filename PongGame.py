import turtle
from pygame import mixer

wn = turtle.Screen()
wn.title("Ping Pong Game")
wn.bgcolor("black")
wn.setup(800, 600)
wn.tracer(0)

# score
score_a = 0
score_b = 0
# paddle_a things
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(5, 1)
# paddle_b things
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(5, 1)
# ball things
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# for score board

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.hideturtle()
pen.write("Player A:0 Player B:0", False, "center", ("courier", 24, "bold"))


# functions for paddle a and b up down


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard things to call the function


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
while True:
    wn.update()
    # ball movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        mixer.init()
        mixer.music.load("bounce.mp3")
        mixer.music.play()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        mixer.init()
        mixer.music.load("bounce.mp3")
        mixer.music.play()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a, score_b), False, "center", ("courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a, score_b), False, "center", ("courier", 24, "bold"))

    # paddle and ball coalitions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        mixer.init()
        mixer.music.load("bounce.mp3")
        mixer.music.play()

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        mixer.init()
        mixer.music.load("bounce.mp3")
        mixer.music.play()
