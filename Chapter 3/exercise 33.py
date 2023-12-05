# First we have to import tkinter as tk.
import tkinter as tk
# Second from tkinter we have to import ttk.
from tkinter import ttk
# We alo need to import math.
import math
# Mentioning class below.
class GeometryCalculator(tk.Tk):
    def __int__(myself):
        super().__init__()
      # Keeping title as My Geometry Calculator.
        myself.title("Geometry Calculator")

        # Now we have to create a notebook (tabbed interface)
        myself.notebook == ttk.Notebook(myself)

        # Now we also need to add tabs for the shapes such as Circle,Square and Rectangle.
        myself.circle_tab = CircleTab(myself.notebook)
        myself.square_tab = SquareTab(myself.notebook)
        myself.rectangle_tab = RectangleTab(myself.notebook)

        myself.notebook.add(myself.circle_tab, text="Circle")
        myself.notebook.add(myself.circle_tab, text="Square")
        myself.notebook.add(myself.circle_tab, text="Rectangle")

        myself.notebook.pack(expand=1, fill="both")
# Now mentioning class as CircleTab.
class CircleTab(tk.Frame):
    def __init__(myself, master):
        super().__init__(master)
    # Now mentioning and updating information about circle area.
        myself.radius_label = tk.Label(myself, text="Enter Your Radius:")
        myself.radius_entry = tk.Entry(myself)
        myself.calculate_button = tk.Button(myself, text="Calculate", command=myself.calculate_area)
        myself.result_label = tk.Label(myself, text="Result:")
    # Now updating the rows and column for the circle part.
        myself.radius_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        myself.radius_entry.grid(row=0, column=1, padx=10, pady=10)
        myself.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)
        myself.result_label.grid(row=2, column=0, columnspan=2, pady=10)
    # Now using the def function to calculate the area of circle.
    def calculate_area(myself):
        try:
            side = float(myself.side_entry.get())
            area = side **2
            myself.result_label.config(text=f"Result: Area = {area:.2f}")
        except ValueError:
            myself.result_label.config(text="Result: Kindly please enter a valid radius.")
 # Now mentioning class as SquareTab.          
class SquareTab(tk.Frame):
    def __init__(myself, master):
        super().__init__(master)
     # Now mentioning and updating information about the area of square.
        myself.side_label = tk.Label(myself, text="Enter side length:")
        myself.side_entry = tk.Entry(myself)
        myself.calculate_button = tk.Button(myself, text="Calculate", command=myself.calculate_area)
        myself.result_label = tk.Label(myself, text="Result:")
        # Now updating the rows and column for the square part.
        myself.side_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        myself.side_entry.grid(row=0, column=1, padx=10, pady=10)
        myself.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)
        myself.result_label.grid(row=2, column=0, columnspan=2, pady=10)
     # Now using the def function to calculate the area of square.
    def calculate_area(myself):
        try:
            side = float(myself.side_entry.get())
            area = side **2
            myself.result_label.config(text=f"Result: Area = {area:.2f}")
        except ValueError:
            myself.result_label.config(text="Result: Kindly please enter a valid side length.")

class RectangleTab(tk.Frame):
    def __init__(myself, master):
        super().__init__(master)
    # Now mentioning and updating information about the area of Rectangle.
        myself.length_label = tk.Label(myself, text="Enter  length:")
        myself.length_entry = tk.Entry(myself)
        myself.width_label = tk.Label(myself, text="Enter width:")
        myself.width_entry = tk.Entry(myself)
        myself.calculate_button = tk.Button(myself, text="Calculate", command=myself.calculate_area)
        myself.result_label = tk.Label(myself, text="Result:")
       # Now updating the rows and column for the rectangle part.
        myself.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        myself.length_entry.grid(row=0, column=1, padx=10, pady=10)
        myself.width_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        myself.width_entry.grid(row=1, column=1, padx=10, pady=10)
        myself.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)
        myself.result_label.grid(row=3, column=0, columnspan=2, pady=10)
      # Now using the def function to calculate the area of rectangle.
    def calculate_area(myself):
        try:
            length = float(myself.length_entry.get())
            width = float(myself.width_entry.get())
            area = length * width
            myself.result_label.config(text=f"Result: Area = {area:.2f}")
        except ValueError:
            myself.result_label.config(text="Result: Kindly please enter a length and width.")
# Below using the if function and mainloop.
if __name__ == "__main__":
    app = GeometryCalculator()
    app.mainloop() 
