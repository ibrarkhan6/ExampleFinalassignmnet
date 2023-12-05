# First import tkinter as tk.
import tkinter as tk
# After that from tkinter import simpledialog
from tkinter import simpledialog
#Seclecting class as ShapeDrawerApp
class ShapeDrawerApp:
    def __init__(myself, master):
        myself.master = master
        myself.master.title("Shape Drawer")
       
        myself.canvas = tk.Canvas(myself.master, width=400, height=400, bg="white")
        myself.canvas.pack()
       # Shapes that needs to be drawn.
        myself.shapes = ["Oval", "Rectangle", "Square", "Triangle"]

        myself.shape_var = tk.StringVar()
        myself.shape_var.set(myself.shapes[0])

        myself.create_shape_selection()
        myself.create_input_button()
    # Using below the dif function to create shape selection.
    def create_shape_selection(myself):
        myshape_label = tk.Label(myself.master, text="Select a shape:")
        myshape_label.pack(pady=10)

        shape_menu = tk.OptionMenu(myself.master, myself.shape_var, *myself.shapes)
        shape_menu.pack(pady=10)
     # Using the def function in order to create the input button.
    def create_input_button(myself):
        input_button = tk.Button(myself.master, text="Input Coordinates", command=myself.get_coordinates)
        input_button.pack(pady=10)
     # Using the def function in order to get the coordinates.
    def get_coordinates(myself):
        shape = myself.shape_var.get()
    # Using the if function for the shapes creation.
        if shape == "Oval":
            myself.draw_oval()
        elif shape == "Rectangle":
            myself.draw_rectangle()
        elif shape == "Square":
            myself.draw_square()
        elif shape == "Triangle":
            myself.draw_triangle()
    # Using the def function to draw the shapes below.
    # Using the def function to draw oval.
    def draw_oval(myself):
        coordinates = myself.get_user_coordinates()
        myself.canvas.create_oval(coordinates, outline="black")
     # Using the def function to draw rectangle.
    def draw_rectangle(myself):
        coordinates = myself.get_user_coordinates()
        myself.canvas.create_rectangle(coordinates, outline="black")
      # Using the def function to draw square.
    def draw_square(myself):
        coordinates = myself.get_user_coordinates()
        myself.canvas.create_rectangle(coordinates, outline="black")
     #Using the def function to draw triangle.
    def draw_triangle(myself):
        coordinates = myself.get_user_coordinates()
        myself.canvas.create_polygon(coordinates, outline="black")
     #Using the def function to help the user in order  to  get the coordinates.
    def get_user_coordinates(myself):
        user_input = simpledialog.askinteger("Input", "Enter coordinates (comma-seperated):")
        if user_input: # Using the if function for the user_input
            coordinates = [int(coord) for coord in user_input.split(",")]
            return coordinates # Using return function.
        # Using the else function.
        else:
            return []
# Using the if fucntion to define the name and main.
if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawerApp(root) # The name of the app is ShapeDrawerapp
    # Using below the mainloop function.
    root.mainloop()