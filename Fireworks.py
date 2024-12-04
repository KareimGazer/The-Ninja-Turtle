import turtle
import random

def draw_firework(t, x, y, size, colors):
    """
    Draws a single firework at the specified position.

    Args:
        t (turtle.Turtle): The turtle object.
        x (float): X-coordinate of the firework's origin.
        y (float): Y-coordinate of the firework's origin.
        size (float): Size (radius) of the firework explosion.
        colors (list): List of colors to use for the firework.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(36):  # Firework bursts with 36 lines
        t.pencolor(random.choice(colors))
        t.forward(size)
        t.backward(size)
        t.right(10)  # 360 degrees divided by 36 lines

def fireworks_simulation():
    """
    Simulates a fireworks display with random bursts on the screen.
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Fireworks Simulation")
    screen.bgcolor("black")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.hideturtle()

    # Define colors for fireworks
    colors = ["red", "yellow", "blue", "green", "purple", "orange", "white"]

    # Simulate multiple fireworks
    for _ in range(10):  # Number of fireworks
        x = random.randint(-300, 300)  # Random x-coordinate
        y = random.randint(-300, 300)  # Random y-coordinate
        size = random.randint(50, 150)  # Random size for each firework
        draw_firework(t, x, y, size, colors)

    # Keep the screen open
    screen.mainloop()

# Call the fireworks simulation function
fireworks_simulation()
