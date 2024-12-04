import turtle

def draw_sun(t, x, y, radius):
    """
    Draws the sun at a specified position.

    Args:
        t (turtle.Turtle): The turtle object.
        x (float): X-coordinate of the sun's center.
        y (float): Y-coordinate of the sun's center.
        radius (float): Radius of the sun.
    """
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_mountain(t, x, y, width, height, color):
    """
    Draws a triangular mountain.

    Args:
        t (turtle.Turtle): The turtle object.
        x (float): X-coordinate of the mountain's base.
        y (float): Y-coordinate of the mountain's base.
        width (float): Width of the mountain.
        height (float): Height of the mountain.
        color (str): Fill color of the mountain.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x + width / 2, y + height)  # Peak of the mountain
    t.goto(x + width, y)  # Bottom-right corner
    t.goto(x, y)  # Back to the starting point
    t.end_fill()

def draw_tree(t, x, y, trunk_width, trunk_height, foliage_radius):
    """
    Draws a tree with a rectangular trunk and a circular foliage.

    Args:
        t (turtle.Turtle): The turtle object.
        x (float): X-coordinate of the trunk's bottom-left corner.
        y (float): Y-coordinate of the trunk's bottom-left corner.
        trunk_width (float): Width of the trunk.
        trunk_height (float): Height of the trunk.
        foliage_radius (float): Radius of the foliage.
    """
    # Draw the trunk
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(trunk_width)
        t.left(90)
        t.forward(trunk_height)
        t.left(90)
    t.end_fill()

    # Draw the foliage
    t.penup()
    t.goto(x + trunk_width / 2, y + trunk_height)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.circle(foliage_radius)
    t.end_fill()

def draw_river(t, x, y, width, height, color):
    """
    Draws a river as a rectangle.

    Args:
        t (turtle.Turtle): The turtle object.
        x (float): X-coordinate of the river's bottom-left corner.
        y (float): Y-coordinate of the river's bottom-left corner.
        width (float): Width of the river.
        height (float): Height of the river.
        color (str): Fill color of the river.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def main():
    """
    Draws a landscape scene with a sun, mountains, trees, and a river.
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Landscape Scene")
    screen.bgcolor("skyblue")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed

    # Draw the sun
    draw_sun(t, x=-200, y=150, radius=50)

    # Draw mountains
    draw_mountain(t, x=-300, y=-50, width=300, height=200, color="grey")
    draw_mountain(t, x=0, y=-50, width=300, height=200, color="darkgrey")

    # Draw a river
    draw_river(t, x=-400, y=-200, width=800, height=100, color="blue")

    # Draw trees
    draw_tree(t, x=-250, y=-100, trunk_width=20, trunk_height=50, foliage_radius=30)
    draw_tree(t, x=-150, y=-100, trunk_width=20, trunk_height=50, foliage_radius=30)
    draw_tree(t, x=100, y=-100, trunk_width=20, trunk_height=50, foliage_radius=30)
    draw_tree(t, x=200, y=-100, trunk_width=20, trunk_height=50, foliage_radius=30)

    # Hide the turtle
    t.hideturtle()

    # Keep the screen open
    screen.mainloop()

# Call the main function to start the program
main()
