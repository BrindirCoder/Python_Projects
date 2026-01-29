import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.color("crimson")
t.width(3)
t.speed(5)  # medium speed (smooth & calm)

# Draw heart
t.penup()
t.goto(0, -80)
t.pendown()

t.begin_fill()
t.left(140)
t.forward(180)

t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)

t.forward(180)
t.end_fill()

# Finish
t.hideturtle()
turtle.done()
