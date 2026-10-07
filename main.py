import turtle

# 1. Set up the screen
screen = turtle.Screen()
screen.title("My Turtle Program")
screen.setup(width=600, height=600)
screen.bgcolor("white")

# 2. Create and configure the turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")
my_turtle.speed(3)  # Speed from 1 (slow) to 10 (fast); 0 is fastest

# 3. Your drawing code goes here
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)

# 4. Keep the window open until you click it
screen.exitonclick()
