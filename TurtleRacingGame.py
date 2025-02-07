import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Racing Game!!!")
num_turtles = int(screen.textinput("Turtle Racing", "Enter the number of Turtles Racing: "))
colors = ["Yellow", "Blue", "Orange", "Red", "Green", "Maroon", "Pink"]
turtles = []

for i in range(num_turtles):
    racer = turtle.Turtle()
    racer.shape("Turtle")
    racer.color(colors[i % len(colors)])
    racer.penup()
    racer.goto(-200, 150-(i * 30))
    turtles.append(racer)

def race():
    winner = None
    while winner is None:
        for racer in turtles:
            racer.forward(random.randint(1, 10))
            if racer.xcor() > 200:
                winner = racer
                break
    print("The Winner is The {winner.color()[0]} Turtle!!!")
    winner.goto(0, 0)

race()
screen.exitonclick()
