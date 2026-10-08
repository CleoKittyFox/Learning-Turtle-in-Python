import turtle

# 1. Set up the screen
screen = turtle.Screen()

screen.tracer(0) # Turn off auto update screen

screen.title("My Turtle Program")
screen.setup(width=600, height=600)
screen.bgcolor("white")

# 2. Create and configure the turtle
Tur = turtle.Turtle()
Tur.shape("turtle")
Tur.color("blue")
Tur.speed(0)  # Speed from 1 (slow) to 10 (fast); 0 is fastest
Tur.setheading(270)

# 3. Your drawing code goes here
def square(size):
    Tur.begin_fill()
    for i in range(4):
        Tur.forward(size)
        Tur.left(90)
    Tur.end_fill()

def shift(length, direction):
    Tur.penup()
    original_direction = Tur.heading()
    Tur.setheading(direction)
    Tur.forward(length)
    Tur.setheading(original_direction)
    Tur.pendown()

Tur.hideturtle()

for y in range(7):
    for x in range(6):
        square(10)
        shift(15, 0)
    shift(90, 180)
    shift(15, 270)

xpos = Tur.xcor()
ypos = Tur.ycor()
Tur.goto(-150, 150)
Tur.write(f"END: ({xpos}, {ypos})")


# 4. Keep the window open until you click it
screen.update() #updates the screen

screen.exitonclick()
