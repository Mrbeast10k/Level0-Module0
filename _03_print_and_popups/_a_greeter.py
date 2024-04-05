from tkinter import messagebox, simpledialog, Tk
from tkinter.messagebox import showinfo
import turtle
# Create an if-main code block 
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    my_turtle = turtle.Turtle()
    # Ask the user for their name and save it to a variable
    # name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    name = simpledialog.askstring(title='Greeter', prompt="turtle")
    # Show a message box with your message using the .showinfo() method
    messagebox.showinfo('title', name )
    # Print your message to the console using the print() function
    print(name)
    # Show an error message using messagebox.showerror()

    # Run the window's .mainloop() method

    pass
