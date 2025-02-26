import random
import turtle

screen = turtle.Screen()
screen.setup(width=2560, height=1440)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
turtle.bgcolor('black')

directions = [0, 90, 180, 270]
t.pensize(3)
boundary_x = 1250
boundary_y = 700


def draw():
    t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.forward(30)
    t.setheading(random.choice(directions))


while True:
    draw()
    if abs(t.xcor()) > boundary_x or abs(t.ycor()) > boundary_y:
        t.penup()
        t.goto(random.randint(-boundary_x, boundary_x), random.randint(-boundary_y, boundary_y))
        t.pendown()
        draw()
        '''t.undo()
        t.setheading(random.choice(directions))'''
    screen.update()

screen.mainloop()
