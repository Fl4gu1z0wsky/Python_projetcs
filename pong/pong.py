# Pong followed on youtube via : https://www.youtube.com/watch?v=XGf2GcyHPhc&list=PLVHYtdkOCcuqP3GAy2YN3p9xjH8RyrKA7&index=2&t=0s
# Created by Flaguizwosky

import turtle
import time
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(10)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
	y = paddle_a.ycor()
	if y <= 250:
		y += 20
		paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	if y >= -250:
		y -= 20
		paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	if y <= 250:
		y += 20
		paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	if y >= -250:
		y -= 20
		paddle_b.sety(y)



# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
	wn.update()

	# Ball move
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		winsound.PlaySound("C:/Users/flavio/Desktop/python/pong/bounce.wav", winsound.SND_ASYNC)

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		winsound.PlaySound("C:/Users/flavio/Desktop/python/pong/bounce.wav", winsound.SND_ASYNC)

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_a += 1
		winsound.PlaySound("C:/Users/flavio/Desktop/python/pong/bounce.wav", winsound.SND_ASYNC)
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_b += 1
		winsound.PlaySound("C:/Users/flavio/Desktop/python/pong/bounce.wav", winsound.SND_ASYNC)
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

	# Collisions paddle/ball
	if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
		ball.setx(330)
		ball.dx *= -1
		winsound.PlaySound("C:/Users/flavio/Desktop/python/pong/bounce.wav", winsound.SND_ASYNC)

	if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
		ball.setx(-330)
		ball.dx *= -1
		winsound.PlaySound("C:/Users/flavio/Desktop/python/pong/bounce.wav", winsound.SND_ASYNC)

	#time.sleep(0.01)