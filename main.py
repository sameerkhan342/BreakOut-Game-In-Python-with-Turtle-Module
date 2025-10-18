from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.dx = 5
ball.dy = 5

colors = ["red", "orange", "yellow", "green", "blue"]
bricks = []
y_positions = [250, 230, 210, 190, 170]

for i in range(5):
    y = y_positions[i]
    for x in range(-350, 350, 70):
        brick = Turtle("square")
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.color(colors[i])
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)

score = 0
scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(0, 260)
scoreboard.write(f"Score: {score}", align="center", font=("Courier", 18, "bold"))

win_message = Turtle()
win_message.hideturtle()
win_message.color("white")
win_message.penup()

def move_left():
    new_x = paddle.xcor() - 40
    if new_x > -350:
        paddle.goto(new_x, paddle.ycor())

def move_right():
    new_x = paddle.xcor() + 40
    if new_x < 350:
        paddle.goto(new_x, paddle.ycor())

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

game_on = True

while game_on:
    time.sleep(0.01)
    screen.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.dx *= -1
    if ball.ycor() > 280:
        ball.dy *= -1
    if ball.ycor() < -280:
        ball.goto(0, -230)
        ball.dy *= -1
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.dy *= -1
    for brick in bricks:
        if brick.distance(ball) < 30:
            brick.goto(1000, 1000)
            bricks.remove(brick)
            ball.dy *= -1
            score += 1
            scoreboard.clear()
            scoreboard.write(f"Score: {score}", align="center", font=("Courier", 18, "bold"))
    if not bricks:
        scoreboard.clear()
        win_message.goto(0, 0)
        win_message.write("YOU WIN!", align="center", font=("Courier", 30, "bold"))
        game_on = False

screen.mainloop()
