import tkinter as tk
from tkinter import ttk
import math

class GeometryCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Geometry Calculator")

        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self)

        # Add tabs for Circle, Square, and Rectangle
        self.circle_tab = CircleTab(self.notebook)
        self.square_tab = SquareTab(self.notebook)
        self.rectangle_tab = RectangleTab(self.notebook)

        self.notebook.add(self.circle_tab, text="Circle")
        self.notebook.add(self.square_tab, text="Square")
        self.notebook.add(self.rectangle_tab, text="Rectangle")

        self.notebook.pack(expand=1, fill="both")

class CircleTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.radius_label = tk.Label(self, text="Enter radius:")
        self.radius_entry = tk.Entry(self)
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_area)
        self.result_label = tk.Label(self, text="Result:")

        self.radius_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.radius_entry.grid(row=0, column=1, padx=10, pady=10)
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_area(self):
        try:
            radius = float(self.radius_entry.get())
            area = math.pi * radius ** 2
            self.result_label.config(text=f"Result: Area = {area:.2f}")
        except ValueError:
            self.result_label.config(text="Result: Please enter a valid radius.")

class SquareTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.side_label = tk.Label(self, text="Enter side length:")
        self.side_entry = tk.Entry(self)
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_area)
        self.result_label = tk.Label(self, text="Result:")

        self.side_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.side_entry.grid(row=0, column=1, padx=10, pady=10)
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_area(self):
        try:
            side = float(self.side_entry.get())
            area = side ** 2
            self.result_label.config(text=f"Result: Area = {area:.2f}")
        except ValueError:
            self.result_label.config(text="Result: Please enter a valid side length.")

class RectangleTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.length_label = tk.Label(self, text="Enter length:")
        self.length_entry = tk.Entry(self)
        self.width_label = tk.Label(self, text="Enter width:")
        self.width_entry = tk.Entry(self)
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_area)
        self.result_label = tk.Label(self, text="Result:")

        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)
        self.width_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.width_entry.grid(row=1, column=1, padx=10, pady=10)
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_area(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            area = length * width
            self.result_label.config(text=f"Result: Area = {area:.2f}")
        except ValueError:
            self.result_label.config(text="Result: Please enter valid length and width.")

if __name__ == "__main__":
    app = GeometryCalculator()
    app.mainloop()
