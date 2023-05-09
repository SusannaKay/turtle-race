from turtle import Turtle, Screen
from random import random, randint

is_race_on = False
# Screen setup
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

# Turtles setup
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

ypos = -140
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    ypos -= -40
    new_turtle.setposition(x=-220, y=ypos)
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You won. The winning turtle is {winning_color}")
            else:
                print(f"You've lost. The winning turtle is {winning_color}")
        random_distance = randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()