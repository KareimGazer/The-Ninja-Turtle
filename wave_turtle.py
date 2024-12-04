import turtle
import math

def draw_wave():
    """
    Draws a sine wave using the turtle module.
    """
    screen = turtle.Screen()
    screen.title("Wave")
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.width(2)  # Thickness of the line
    t.pencolor("blue")

    # Draw the sine wave
    t.penup()
    t.goto(-360, 0)  # Start point of the wave
    t.pendown()

    for x in range(-360, 361):  # Draw the wave from -360 to 360
        y = 50 * math.sin(math.radians(x))  # Sine wave formula
        t.goto(x, y)

    t.hideturtle()
    screen.mainloop()

draw_wave()