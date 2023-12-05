import tkinter as tk

def validate_login():
    # Placeholder validation function
    print("Login button pressed")

root = tk.Tk()
root.title("Login Page")

# Username Label and Entry
tk.Label(root, text="Username:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password Label and Entry
tk.Label(root, text="Password:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
password_entry = tk.Entry(root, show="")  # Show '' for password
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()