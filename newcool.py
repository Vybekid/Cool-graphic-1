import turtle 
import random 

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Cool Graphic")
screen.colormode(255)

pen = turtle.Turtle()
pen.speed(0.004)
pen.hideturtle()
pen.pensize(2)

num_points = 5 
star_size = 200 
num_stars = 100 
angle_offset = 360 / num_stars 

def get_random_color(): 
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

for i in range(num_stars): 
    pen.pencolor(get_random_color())
    pen.setheading(i * angle_offset)

    pen.penup()
    pen.goto(0, 0)
    pen.forward(star_size / 2)
    pen.pendown()

    for _ in range(num_points): 
        pen.forward(star_size)
        pen.right(180 - (180 / num_points))

screen.exitonclick()

