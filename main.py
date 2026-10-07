import turtle

# 1. Set up the screen
screen = turtle.Screen()
screen.title("My Turtle Program")
screen.setup(width=600, height=600)
screen.bgcolor("white")

# 2. Create and configure the turtle
Tur = turtle.Turtle()
Tur.shape("turtle")
Tur.color("blue")
Tur.speed(1)  # Speed from 1 (slow) to 10 (fast); 0 is fastest
Tur.setheading(270)

# 3. Your drawing code goes here
def square(size):
    Tur.begin_fill()
    for i in range(4):
        Tur.forward(size)
        Tur.left(90)
    Tur.end_fill()

Tur.hideturtle()
square(10)


Tur.goto(-150, 150)
Tur.write("END")


# 4. Keep the window open until you click it
screen.exitonclick()
