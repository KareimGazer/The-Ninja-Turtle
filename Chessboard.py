import turtle

def draw_square(t, x, y, size, color):
    """
    Draws a single square on the chessboard.

    Args:
        t (turtle.Turtle): The turtle object.
        x (float): X-coordinate of the square's top-left corner.
        y (float): Y-coordinate of the square's top-left corner.
        size (float): Length of the square's side.
        color (str): Fill color of the square.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_chessboard(t, start_x, start_y, size):
    """
    Draws an 8x8 chessboard.

    Args:
        t (turtle.Turtle): The turtle object.
        start_x (float): X-coordinate of the chessboard's top-left corner.
        start_y (float): Y-coordinate of the chessboard's top-left corner.
        size (float): Length of each square's side.
    """
    colors = ["white", "black"]
    for row in range(8):
        for col in range(8):
            x = start_x + col * size
            y = start_y - row * size
            color = colors[(row + col) % 2]  # Alternate between black and white
            draw_square(t, x, y, size, color)

def draw_piece(t, x, y, size, color):
    """
    Draws a circular piece at the given square.

    Args:
        t (turtle.Turtle): The turtle object.
        x (float): X-coordinate of the square's center.
        y (float): Y-coordinate of the square's center.
        size (float): Diameter of the piece.
        color (str): Fill color of the piece.
    """
    t.penup()
    t.goto(x, y - size / 2)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size / 2)
    t.end_fill()

def draw_chess_pieces(t, start_x, start_y, size):
    """
    Draws chess pieces on the chessboard.

    Args:
        t (turtle.Turtle): The turtle object.
        start_x (float): X-coordinate of the chessboard's top-left corner.
        start_y (float): Y-coordinate of the chessboard's top-left corner.
        size (float): Length of each square's side.
    """
    # Draw pawns (example representation)
    for col in range(8):
        # White pawns
        draw_piece(t, start_x + col * size + size / 2, start_y - size * 1.5, size / 2, "white")
        # Black pawns
        draw_piece(t, start_x + col * size + size / 2, start_y - size * 6.5, size / 2, "black")

def main():
    """
    Main function to draw the chessboard with pieces.
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Chessboard with Pieces")
    screen.bgcolor("white")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed

    # Chessboard parameters
    start_x = -200  # Top-left corner x
    start_y = 200   # Top-left corner y
    square_size = 50  # Size of each square

    # Draw the chessboard
    draw_chessboard(t, start_x, start_y, square_size)

    # Draw the chess pieces
    draw_chess_pieces(t, start_x, start_y, square_size)

    # Hide the turtle
    t.hideturtle()

    # Keep the screen open
    screen.mainloop()

# Call the main function to start the program
main()
