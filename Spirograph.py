import turtle

def draw_spirograph(radius, step_angle):
    """
    Draws a spirograph pattern using the turtle module.

    Args:
        radius (float): Radius of each individual circle.
        step_angle (float): Angle to turn for each step of the spirograph.
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Spirograph")
    screen.bgcolor("black")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.width(2)  # Thickness of the line

    # Define colors for the spirograph
    colors = ["red", "blue", "green", "purple", "orange", "yellow"]

    # Draw the spirograph
    for angle in range(0, 360, int(step_angle)):
        t.pencolor(colors[angle % len(colors)])  # Cycle through colors
        t.penup()
        t.goto(0, -radius)  # Move to the starting position of the circle
        t.pendown()
        t.setheading(angle)  # Rotate the turtle
        t.circle(radius)  # Draw the circle

    # Hide the turtle
    t.hideturtle()

    # Keep the screen open
    screen.mainloop()

# Example usage
draw_spirograph(radius=100, step_angle=15)
