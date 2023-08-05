import turtle 
import random

tim = turtle.Turtle()
turtle.colormode(255) 

def random_color():
  r = random.randint(0,255)
  r = random.randint(0,255)
  r = random.randint(0,255)
  random_color = (r,g,b) 
  return random_color

directions = [0,90,180,270] 
tim.pensize(10)
tim.speed("fastest") 

for _ in range(200):
  tim.color(random_color())
  tim.forward(30) 

s = Screen() 
s.exitonclick()
  
  tim.setheading(random.choice(directions))
