import turtle

def koch_curve(t, length, depth):
    """
    Draws a Koch curve using recursion.

    Args:
        t (turtle.Turtle): The turtle object.
        length (float): The length of the current segment.
        depth (int): The recursion depth.
    """
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)

def koch_snowflake(length, depth):
    """
    Draws a Koch snowflake by combining three Koch curves.

    Args:
        length (float): The length of the snowflake's side.
        depth (int): The recursion depth.
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Koch Snowflake")
    screen.bgcolor("white")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.width(2)  # Thickness of the line
    t.penup()
    t.goto(-length / 2, length / (2 * (3 ** 0.5)))  # Center the snowflake
    t.pendown()

    # Draw the snowflake
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)

    # Hide the turtle
    t.hideturtle()

    # Keep the screen open
    screen.mainloop()

# Example usage
koch_snowflake(length=300, depth=4)
