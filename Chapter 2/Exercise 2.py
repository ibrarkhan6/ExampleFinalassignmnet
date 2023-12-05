import tkinter as tk

class MyFourLabelsApp:
    def __init__(self, mymaster):
        self.mymaster = mymaster
        mymaster.title("My Four Labels App")

        label1 = tk.Label(mymaster, text="Label 1", bg="red", fg="white", width=20)
        label2 = tk.Label(mymaster, text="Label 2", bg="green", fg="white", width=20)
        label3 = tk.Label(mymaster, text="Label 3", bg="blue", fg="white", width=20)
        label4 = tk.Label(mymaster, text="Label 4", bg="yellow", fg="black", width=20)

        label1.pack(side="top", padx=5, pady=5)
        label2.pack(side="left", padx=5, pady=5)
        label3.pack(side="right", padx=5, pady=5)
        label4.pack(side="bottom", padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyFourLabelsApp(root)
    root.mainloop()

        
                            