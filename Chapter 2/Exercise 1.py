import tkinter as tk

class WelcomeMyapp:
    def __init__(self,mymaster):
        self.master = mymaster
        mymaster.title("WelcomeMyapp")

        #Now we have to create a lable in order to display the welcome message.
        mywelcome_label = tk.Label(mymaster, text="Welcome to my very first Gui Program!", font=("Arial", 16,"bold" ))
        mywelcome_label.pack(pady=20)

        #Now we have to set the default window size..
        mymaster.geometry("400x200")

        #Now we have to disable resizing the window.
        mymaster.resizable(False,False)

        #Now we have to default the window size.
        mymaster.configure(bg="#e6e6e6")

        root = tk.Tk()
        app = WelcomeMyapp
        root.mainloop()
