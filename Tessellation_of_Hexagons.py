import turtle

def draw_hexagon(t, side_length):
    """
    Draws a single hexagon using the turtle module.

    Args:
        t (turtle.Turtle): The turtle object.
        side_length (float): The length of each side of the hexagon.
    """
    for _ in range(6):
        t.forward(side_length)
        t.left(60)

def draw_tessellation(rows, cols, side_length):
    """
    Draws a tessellation of hexagons.

    Args:
        rows (int): Number of rows in the tessellation.
        cols (int): Number of columns in the tessellation.
        side_length (float): The length of each side of the hexagon.
    """
    screen = turtle.Screen()
    screen.title("Hexagon Tessellation")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.penup()

    # Calculate the horizontal and vertical offsets for hexagons
    x_offset = 1.5 * side_length
    y_offset = (3 ** 0.5) * side_length  # Height of a hexagon

    for row in range(rows):
        for col in range(cols):
            # Compute the starting position for the current hexagon
            x = col * x_offset
            y = -row * y_offset

            # Offset every other row for a tessellated pattern
            if row % 2 != 0:
                x += x_offset / 2

            # Move the turtle to the position and draw the hexagon
            t.goto(x, y)
            t.pendown()
            draw_hexagon(t, side_length)
            t.penup()

    t.hideturtle()
    screen.mainloop()

# Example usage
draw_tessellation(rows=5, cols=6, side_length=30)
