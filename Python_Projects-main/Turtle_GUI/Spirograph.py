
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)  # from 0 to 255


def random_color():
    """returns a random color using the RGB tuple"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)  # creates a tuple that consists of the 3 integers above
    return color


tim.speed("fastest")

def draw_spirograph(size):
  for _ in range(int(360/size)):
    tim.color(random_color())
    tim.circle(100) 
    tim.setheading(tim.heading() + 10)

draw_spirograph(5)

s = t.Screen()
s.exitonclick()
