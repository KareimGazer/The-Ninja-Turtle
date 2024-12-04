import turtle

def draw_circle(t, x, y, radius, color):
    """
    Draws a circle at the specified position with the given radius and color.

    Args:
        t (turtle.Turtle): The turtle object.
        x (float): The x-coordinate of the circle's center.
        y (float): The y-coordinate of the circle's center.
        radius (float): The radius of the circle.
        color (str): The color of the circle.
    """
    t.penup()
    t.goto(x, y - radius)  # Move to the starting position
    t.pendown()
    t.pencolor(color)
    t.circle(radius)

def draw_olympic_rings():
    """
    Draws the Olympic Rings with their respective colors and positions.
    """
    # Create the turtle screen
    screen = turtle.Screen()
    screen.title("Olympic Rings")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(3)  # Set the drawing speed

    # Define the colors and positions for the rings
    colors = ["blue", "black", "red", "yellow", "green"]
    positions = [(-150, 0), (0, 0), (150, 0), (-75, -50), (75, -50)]
    radius = 50

    # Draw each ring
    for color, (x, y) in zip(colors, positions):
        draw_circle(t, x, y, radius, color)

    # Hide the turtle
    t.hideturtle()

    # Keep the window open
    screen.mainloop()

# Call the function to draw the Olympic Rings
draw_olympic_rings()
