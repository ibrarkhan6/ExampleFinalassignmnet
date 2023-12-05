#First we have to import tkinter as tk.
import tkinter as tk
#And than from tkinter we have to import messagebox
from tkinter import messagebox
#Now we have to use def in order to update 
# the user greeting,name,color and label.
def update_greeting():
    name = name_myentry.get()
    color = color_myvar.get()
    greeting_mylabel.config(text=f"Hello Champ, {name}!", fg=color)
#Using root as tk.Tk
root = tk.Tk()
#Root title is "Greeting App"
root.title("Greeting App")
#Now I am updating my input frame below in which background color is blue.
#And padx abd pady is 21.
input_myframe = tk.Frame(root, bg="blue", padx=21, pady=21)
input_myframe.pack()
#Now I am updating my display frame in which the background color is selected as light green.
#And padx and pady is 21.
display_myframe = tk.Frame(root, bg="orange", padx=21, pady=21)
display_myframe.pack()
#Editing my label with codes below in which the text inside the 
# label are mentioned as "Welcome User!".
#Background color updated and font type and size as well as the pady.
title_mylabel = tk.Label(input_myframe, text="Welcome User!",
 fg="blue", font=("Arial", 16), pady=10)
title_mylabel.grid(row=0, columnspan=2)
#Using the below codes I have mentioned the text 
# "Enter your name:" inside the label.
name_mylabel = tk.Label(input_myframe, text="Enter your name:")
name_mylabel.grid(row=1, column=0)
#This label have one row and no columns
name_myentry = tk.Entry(input_myframe)
#Entry have one row and no columns as well.
name_myentry.grid(row=1, column=1)#Entry have one row and no columns as well.
#Using the below codes I have mentioned the text "Select a good color:" inside the frame.
color_mylabel = tk.Label(input_myframe, text="Select a good color:")
#This frame have one row and no columns.
color_mylabel.grid(row=2, column=0)
#The four colors which I have used are mentioned in this frames are mentioned below.
colors = ['Purple', 'Red', 'Golden', 'Pink']
color_myvar = tk.StringVar(root)
#Updating my dropdown label.
color_mydropdown = tk.OptionMenu(input_myframe, color_myvar, *colors)
color_mydropdown.grid(row=2, column=1)
#Updating my button label part in which text mentioned are "Update Greeting".
update_mybutton = tk.Button(input_myframe, text="Update Greeting", command=update_greeting)
#The button label have three rows and two columspan.
update_mybutton.grid(row=3, columnspan=2)
#Updating my greeting section keeping font family as arial and size as 14.
greeting_mylabel = tk.Label(display_myframe, text="", font=("Arial", 14))
greeting_mylabel.pack()
#Using mainloop.
root.mainloop()
#Each and every frame have different colors.