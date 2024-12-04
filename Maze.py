import turtle
import random

def draw_line(t, x1, y1, x2, y2):
    """
    Draws a line from (x1, y1) to (x2, y2).

    Args:
        t (turtle.Turtle): The turtle object.
        x1, y1 (float): Starting coordinates of the line.
        x2, y2 (float): Ending coordinates of the line.
    """
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

def draw_maze(t, x, y, width, height):
    """
    Recursively divides the area into smaller regions to generate a maze.

    Args:
        t (turtle.Turtle): The turtle object.
        x, y (float): Bottom-left corner of the region.
        width, height (float): Dimensions of the region.
    """
    if width < 20 or height < 20:  # Base case: Stop when regions are too small
        return

    # Decide the orientation of the division
    horizontal = random.choice([True, False])

    if horizontal:
        # Draw a horizontal wall
        wall_y = y + random.randint(10, height - 10)
        gap_x = x + random.randint(0, width)
        draw_line(t, x, wall_y, x + width, wall_y)  # Draw the wall
        draw_line(t, gap_x, wall_y, gap_x, wall_y - 10)  # Leave a gap
        # Recur for the two divided regions
        draw_maze(t, x, y, width, wall_y - y)  # Bottom region
        draw_maze(t, x, wall_y, width, y + height - wall_y)  # Top region
    else:
        # Draw a vertical wall
        wall_x = x + random.randint(10, width - 10)
        gap_y = y + random.randint(0, height)
        draw_line(t, wall_x, y, wall_x, y + height)  # Draw the wall
        draw_line(t, wall_x, gap_y, wall_x + 10, gap_y)  # Leave a gap
        # Recur for the two divided regions
        draw_maze(t, x, y, wall_x - x, height)  # Left region
        draw_maze(t, wall_x, y, x + width - wall_x, height)  # Right region

def maze_generator():
    """
    Generates a random maze.
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Maze Generator")
    screen.bgcolor("white")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.hideturtle()

    # Dimensions of the maze
    start_x = -200
    start_y = -200
    maze_width = 400
    maze_height = 400

    # Draw the outer boundary of the maze
    draw_line(t, start_x, start_y, start_x + maze_width, start_y)
    draw_line(t, start_x, start_y, start_x, start_y + maze_height)
    draw_line(t, start_x, start_y + maze_height, start_x + maze_width, start_y + maze_height)
    draw_line(t, start_x + maze_width, start_y, start_x + maze_width, start_y + maze_height)

    # Generate the maze
    draw_maze(t, start_x, start_y, maze_width, maze_height)

    # Keep the screen open
    screen.mainloop()

# Run the maze generator
maze_generator()
