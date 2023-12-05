
import tkinter as tk

def write_to_file():
    with open("bio.txt", "w") as file:
        file.write(f"Name: {name_entry.get()}\n")
        file.write(f"Age: {age_entry.get()}\n")
        file.write(f"Hometown: {hometown_entry.get()}\n")

def read_from_file():
    try:
        with open("bio.txt", "r") as file:
            content = file.read()
            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, content)
            output_text.config(state=tk.DISABLED)
    except FileNotFoundError:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "File not found.")
        output_text.config(state=tk.DISABLED)

# Create the main window
app = tk.Tk()
app.title("Bio Information")

# Create entry widgets
name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.E)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

age_label = tk.Label(app, text="Age:")
age_label.grid(row=1, column=0, sticky=tk.E)
age_entry = tk.Entry(app)
age_entry.grid(row=1, column=1)

hometown_label = tk.Label(app, text="Hometown:")
hometown_label.grid(row=2, column=0, sticky=tk.E)
hometown_entry = tk.Entry(app)
hometown_entry.grid(row=2, column=1)

# Create buttons
write_button = tk.Button(app, text="Write to File", command=write_to_file)
write_button.grid(row=3, column=0, columnspan=2, pady=10)

read_button = tk.Button(app, text="Read from File", command=read_from_file)
read_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create text widget for output
output_text = tk.Text(app, height=6, width=30, state=tk.DISABLED)
output_text.grid(row=5, column=0, columnspan=2)

# Start the main loop
app.mainloop()