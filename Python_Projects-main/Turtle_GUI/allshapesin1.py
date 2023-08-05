from turtle import Turtle, Screen 
import random

t = Turtle()

colours = ["IndianRed","Yellow","Black","Blue","Green","Orange","pink"]

def draw_angle(num_sides):
    angle =  360/num_sides
    for i in range(num_sides):
        t.forward(100)
        t.right(angle)

for shape_side in range(3,10):
    t.color(random.choice(colours))
    draw_angle(shape_side)


screen = Screen()
screen.exitonclick()
