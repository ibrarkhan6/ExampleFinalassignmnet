import tkinter as tk

root = tk.Tk()

#Now here now I am writing for left frame which will have part A and B
Myleft_frame = tk.Frame(root, borderwidth=5, background='Light grey')
Myleft_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

mylabel_a = tk.Label(Myleft_frame, text='A', background='DarkBlue')
mylabel_a.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

mylabel_b = tk.Label(Myleft_frame, text='B', background='White')
mylabel_b.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

MyRight_frame = tk.Frame(root, borderwidth=5, background='Light Grey')
MyRight_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

mylabel_c = tk.Label(MyRight_frame, text='C', background='White')
mylabel_c.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

mylabel_d = tk.Label(MyRight_frame, text='D', background='DarkBlue')
mylabel_d.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

root.mainloop()