import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def get_next_color(i):
    return colors[i % len(colors)]


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    window.setup(width=0.75, height=0.9, startx=0, starty=0)
    
    colors = ('black', 'white', 'black', 'white', 'green')
    
    # Make a new turtle
    my_turtle=turtle.Turtle()
    # Make the turtle shape 'turtle', .shape('turtle')
    my_turtle.shape('turtle')
    # Set the turtle speed to max (0)
    my_turtle.speed(1000000000000)
    # Set the turtle width to 1
    my_turtle.width(1)
    # Create a variable to hold the number of sides in a pentagon
    pentagon=5
    # Create a variable to be the angle of 360 divided by the sides variable
    angle=360/pentagon
    # Use a for loop to repeat ALL the following lines of code 360 times. 
    for x in range(360):

        # If the loop variable (i) is equal to 100, set the turtle width to 2
        if x == 100:
            my_turtle.width(2)
        # If the loop variable (i) is equal to 200, set the turtle width to 3
        if x == 200:
            my_turtle.width(3)
        # Use the get_next_color function to set the turtle pencolor,
        # *hint .pencolor(get_next_color(i))
        my_turtle.pencolor(get_next_color(x))
        # Move the turtle forward by the loop variable, *hint .forward(i)
        my_turtle.forward(x)
        my_turtle.right(60)
        my_turtle.right(10)

        my_turtle.left(9)
        # Turn the turtle to the right by the angle variable + 1

    # Hide your turtle so you can see the pattern.
        
    # Check the pattern against the picture in the recipe. If it matches, you are done!
    
    # Variations:
    # *Make the pattern really huge
    # *Change the colors
    # *Experiment with different shapes
    
    # Call the turtle.done() method
    turtle.done()