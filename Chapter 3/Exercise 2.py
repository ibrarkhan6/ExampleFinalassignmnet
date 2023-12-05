#First we have to import  tkinter as tk.
import tkinter as tk
#After that from tkinter we have to import messagebox
from tkinter import messagebox
#Selecting class
class YourCoffeeVendingMachine:
    def __init__(myself, root):
       myself.root = root
       myself.root.title("Your Coffee Vending Machine")

       #Now we have to intialize the variables below.
       myself.coffee_type = tk.StringVar()
       myself.sugar = tk.IntVar()
       myself.ice = tk.Intvar()
       myself.milk = tk.Intvar()

       #Now we have to create labels below.
       #I am planning to make four labels.
       tk.Label(root, text="Select Your Favourite Coffee Type:").pack()
       myself.coffee_menu = tk.OptionMenu(root, myself.coffee_type, "Red Eye", "Irish", "Mocha")
       myself.coffee_menu.pack

       tk.Label(root, text="Select Sugar Level:").pack()
       tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, variable=myself.sugar).pack()

       tk.Label(root, text="Select Milk Level").pack()
       tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, variable=myself.milk).pack()

       #Now we have to make a button below.
       tk.Button(root, text="Make My Coffee", command=myself.make_coffee).pack()
       #Options mentioned below
    def make_coffe(myself):
        coffee_type = myself.coffee_type.get()
        coffee_type = myself.sugar.get()
        coffee_type = myself.milk.get()
        #Now we have to display the selected options using a message box.

        message = f"You ordered:\nCoffee Type: {coffee_type}\nSugar Level: {sugar_level}\nMilk Level: {milk_level}"
        messagebox.showinfo("Order Summary", message)

        #Now we have to handle the money of the customer (extesnion)
        myself.handle_money()
    
    def handle_money(myself):
        #In the real-life world scenario, you would really have to integrate a payement system here.
        #For simplicity, we will assume a fixed price for the coffee and therfore setting a price below.
        coffee_price = 5.50
        money_received = float(input("Enter the amount of money you're planning to insert: "))
       # Now usibg the if function below.
        if money_received >= coffee_price:
            change = money_received - coffee_price
            print(f"Thank you! for being our valuable customer Your Change is: ${change:.2f}" )
          # Now usibg the else function below.  
        else:
            print("Insufficient funds you have inserted. Please insert more money as required.")
if __name__ == "__main__":
    root = tk.Tk()
    app =  YourCoffeeVendingMachine
    root.mainloop()