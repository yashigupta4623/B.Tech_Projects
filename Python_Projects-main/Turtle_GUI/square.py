from turtle import Turtle, Screen
t = Turtle()

t.shape("turtle")
t.color("red")
for i in range(3):
    t.forward(100)
    t.left(90)

t.forward(100)


screen = Screen() 
screen.exitonclick()
