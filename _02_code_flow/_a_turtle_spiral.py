import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    my_turtle = turtle.Turtle()
    # This code sets our shape to a turtle
    my_turtle.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    my_turtle.speed(10000000000000000000000000)
    # Set your turtle's color using .color('green')
    my_turtle.color (get_random_color())
    # Use a loop to repeat a the code below 50 times
    for x in range(150):
        # Set the turtle color to a random color

        # Move the turtle (5*i) pixels. 'i' is the loop variable
        my_turtle.forward(5*x)
        my_turtle.color(get_random_color())
        # Turn the turtle (360/7) degrees to the right
        my_turtle.right(360/7)
        my_turtle.color(get_random_color())
        # Change the turtle width to 'i' (the loop variable)
        my_turtle.width(5)
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()