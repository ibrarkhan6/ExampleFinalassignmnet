from tkinter import *
import random
app = Tk() # Create the top-level window
app.title("GUI Example 4") # OPTIONALLY set the title
bA = Label(app, text="A", width=12 ,bg='red', relief=GROOVE, bd=5)
bB = Label(app, text="B", width=12, bg='yellow')
bC = Label(app, text="C", width=12, bg='blue')
bD = Label(app, text="D", width=12, bg='white')
bA.pack(side='top',fill=X, expand=1)
bB.pack(side='bottom')
bC.pack(side='left', fill=Y, expand=1)
bD.pack(side='right')
app.mainloop() #Start the main loop