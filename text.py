import turtle

def write_text(t, text, x, y, font=("Arial", 24, "bold"), color="black"):
    """
    Writes text at the specified position with the specified font and color.

    Args:
        t (turtle.Turtle): The turtle object.
        text (str): The text to write.
        x, y (float): The coordinates to position the text.
        font (tuple): Font type, size, and style.
        color (str): Color of the text.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.write(text, align="center", font=font)

def draw_text_art(t):
    """
    Creates a creative text art design using the turtle module.
    """
    # Draw a rectangle background for the text
    t.penup()
    t.goto(-200, 50)
    t.pendown()
    t.fillcolor("lightblue")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

    # Write text in the center of the rectangle
    write_text(t, "Hello, Turtle!", 0, 20, font=("Verdana", 20, "bold"), color="darkblue")

    # Add additional decorative text
    write_text(t, "Fun with Python", 0, -50, font=("Comic Sans MS", 16, "italic"), color="green")

def main():
    """
    Main function to draw text and artistic decorations.
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Text Writing with Turtle")
    screen.bgcolor("white")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.hideturtle()

    # Draw the text art
    draw_text_art(t)

    # Keep the screen open
    screen.mainloop()

# Run the program
main()
