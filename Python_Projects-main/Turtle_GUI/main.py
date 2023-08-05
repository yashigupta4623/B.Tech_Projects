import another_module #another_Variable = 20 --- written this in the file.

# object.attribute
# object.methods
'''ATTRIBUTES -- features like car has speed, fuel etc
METHODS -- function like def move(): speed = 60'''

# import turtle #mandatory to write
# timmy = turtle.Turtle() 
# ''' is mandatory to write and "timmy" is just a
# variable and Turtle is the class of the turtle method'''

#OR

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle") #to change the shape of the turtle
timmy.color("green")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight) # will display for milliseconds with height
my_screen.exitonclick() #to pause the screen until we click














