import tkinter as tk
from tkinter import messagebox

items_in_stock = [
    {"item_id": 0, "item_name": "Milky Bar", 'item_price': 60},
    {"item_id": 1, "item_name": "Fanta", 'item_price': 90},
    {"item_id": 2, "item_name": "Kurkure", 'item_price': 25},
    {"item_id": 3, "item_name": "Thumbs Up", 'item_price': 90},
    {"item_id": 4, "item_name": "Wai-Wai", 'item_price': 20},
]

class VendingmachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine")

        # Using the variables below.
        self.the_item = []
        self.reciept = tk.StringVar(value="PRODUCT -- PRICE")

        # Using GUI components below.
        self.label_title = tk.Label(root, text="Vending Machine", font=("Helvetica", 16))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_instruction = tk.Label(root, text="Select items to purchase:")
        self.label_instruction.grid(row=1, column=0, columnspan=2)

        # Now we have to  create a button for each and every item.
        for i, item in enumerate(items_in_stock):
            btn_item = tk.Button(root, text=f"{item['item_name']} - ${item['item_price']}", command=lambda idx=i: self.add_item(idx))
            btn_item.grid(row=i + 2, column=0, pady=5)

        self.label_total = tk.Label(root, text="Total: $0")
        self.label_total.grid(row=len(items_in_stock) + 2, column=0, pady=10)

        self.button_print_receipt = tk.Button(root, text="Print Receipt", command=self.print_receipt)
        self.button_print_receipt.grid(row=len(items_in_stock) + 3, column=0, pady=10)

    def add_item(self, idx):
        self.the_item.append(items_in_stock[idx])
        self.update_total_label()
    
    def update_total_label(self):
        total_price = sum(item['item_price'] for item in self.the_item)
        self.label_total.config(text=f"Total: ${total_price}")

    def print_receipt(self):
        receipt_text = create_receipt(self.the_item)
        messagebox.showinfo("Receipt", receipt_text)
    
def create_receipt(the_item):
    receipt_text = "PRODUCT -- PRICE\n"

    for item in the_item:
        receipt_text += f"{item['item_name']}-- {item['item_price']}\n"

    total_price = sum(item['item_price'] for item in the_item)
    receipt_text += f"\nTotal --- ${total_price}\n"

    return receipt_text

if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineApp(root)
    root.mainloop()
