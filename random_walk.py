import turtle
import random

def random_walk(steps, step_length):
    """
    Simulates a random walk using the turtle module.

    Args:
        steps (int): Number of steps in the random walk.
        step_length (float): Length of each step.
    """
    # Create the turtle screen
    screen = turtle.Screen()
    screen.title("Random Walk Simulation")
    screen.bgcolor("white")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Maximum speed
    t.width(2)  # Thickness of the trail

    # Random walk loop
    for _ in range(steps):
        # Pick a random direction (angle) and color
        angle = random.choice([0, 90, 180, 270])  # North, East, South, West
        color = random.choice(["red", "blue", "green", "purple", "orange", "yellow"])

        # Set the turtle's color and move
        t.pencolor(color)
        t.setheading(angle)
        t.forward(step_length)

    # Hide the turtle and keep the window open
    t.hideturtle()
    screen.mainloop()

# Example usage
random_walk(steps=500, step_length=20)
