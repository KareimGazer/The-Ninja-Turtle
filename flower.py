import turtle
import random

def draw_flower(t, petals, radius, colors):
    """
    Draws a flower-like pattern with multiple petals.

    Args:
        t (turtle.Turtle): The turtle object.
        petals (int): Number of petals.
        radius (float): Radius of each petal.
        colors (list): List of colors for the petals.
    """
    angle = 360 / petals
    for _ in range(petals):
        t.fillcolor(random.choice(colors))
        t.begin_fill()
        for _ in range(2):
            t.circle(radius, 60)  # Draw a half-petal arc
            t.left(120)  # Turn to complete the petal
        t.end_fill()
        t.right(angle)  # Move to the next petal position

def draw_inner_circle(t, radius, colors):
    """
    Draws a filled circle in the center of the mandala.

    Args:
        t (turtle.Turtle): The turtle object.
        radius (float): Radius of the inner circle.
        colors (list): List of colors for the circle.
    """
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_layered_mandala(t, layers, initial_radius, step, colors):
    """
    Draws a layered mandala design with multiple flower-like layers.

    Args:
        t (turtle.Turtle): The turtle object.
        layers (int): Number of layers in the mandala.
        initial_radius (float): Radius of the innermost layer.
        step (float): Increment in radius for each layer.
        colors (list): List of colors for the layers.
    """
    for layer in range(layers):
        draw_flower(
            t, petals=8 + layer * 4,  # Increase petals with each layer
            radius=initial_radius + layer * step,
            colors=colors,
        )

def draw_complex_mandala():
    """
    Draws a complex mandala resembling a flower with multiple layers.
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Complex Flower Mandala")
    screen.bgcolor("black")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.hideturtle()

    # Define colors for the mandala
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white"]

    # Draw the mandala
    draw_inner_circle(t, radius=50, colors=colors)  # Inner circle
    draw_layered_mandala(t, layers=8, initial_radius=60, step=20, colors=colors)

    # Keep the screen open
    screen.mainloop()

# Run the mandala drawing
draw_complex_mandala()
