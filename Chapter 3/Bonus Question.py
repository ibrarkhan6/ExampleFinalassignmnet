# Using the def function for display menu.
def display_menu():
    # Using print Below
    print("Welcome To RAK Burger Shack! Menu:")
    print("1. Beef Burger")
    print("2. Chicken Burger")
    print("3. Vegetarian Burger")
# Using the def function to choose burger for the user.
def choose_burger():
    mychoice = input("Kindly enter the nuumber of the burger you'd like to order: ")
    # The three types of burgers that will be avaiable for the user are mentioned below.
    myburgers = ["Beef Burger", "Chicken Burger", "Vegetarian Burger"]

    if mychoice.isdigit() and 1 <= int(mychoice) <= len(myburgers):
        # Using below the return function.
        return myburgers[int(mychoice) - 1]
    # Using the else function below for Invalid choice.
    else:
        print("Invalid choice. Kindly please enter a valid number.")
        return choose_burger() # Using the return here.
  # Using the def fucntion to  add toppings for  the user.  
def add_toppings():
    #Below are the four types of toppings that will be available for the user.
    mytoppings = ["Cheese", "Peanut Butter", "Avocado"]
    print("\nChoose toppings (comma-separated):")
    print(", ".join(mytoppings))
    selected_toppings = input().split(", ")
    # Using the return function.
    return [topping for topping in selected_toppings if topping in mytoppings]
# Using the def function to add condiments for the user.
def add_condiments():
    mycondiments =  ["Ketchup", "Mayonnaise", "BBQ Sauce"]
    print("\nChoose condiments (comma-separated):")
    print(", ".join(mycondiments))
    selected_condiments  = input().split(",  ")
    # Uisng the return function.
    return [condiments for condiments in selected_condiments if condiments in condiments]
# Using the def function to add sides for the user.
def add_sides():
# The three sides that will be available for the user.
    mysides = ["Fries", "Drink"]
    print("\nChoose sides (comma-separated):")
    print(", ".join(mysides))
    selected_sides = input().split(", ")
    # Using the return function.
    return [sides for sides in selected_sides if sides in sides]
# Once again using the def function in order to set up and calculate the prices for the orders.
def calculate_total(order):
    #The prices for burgers, topping, condiments, and sides are mentioned below. 
    myburger_prices = {"Beef Burger": 5.0, "Chicken Burger": 4.5, "Vegetarian Burger": 4.0}
    mytopping_price = 0.5
    mycondiment_price = 0.3
    myside_price = 2.0

    total = myburger_prices[order["burger"]]
    total += len(order["toppings"]) * mytopping_price
    total += len(order["condiments"]) * mycondiment_price
    total += len(order["sides"]) * myside_price
 # Using return function for the total.
    return total
# Using def function for to handle the payment.
def userhandle_payment(total):
    print("\nYour total is: $", total)
    payment = float(input("Enter the amount you're paying: $"))
    if payment < total: # Using the if function.
        print("Insufficient payment. Please Enter a valid amount.")
        return userhandle_payment(total)
    # Using below  the else function to calculate  the change , payment and total for a particular order.
    else:
        change = payment - total
        print("Thank your for  your order! your change is: $", change)
# Using below the def function for the main.
def main():
    order = {}
# Displaying the menu.
    display_menu()
    order["burger"] = choose_burger()
    order["toppings"] = add_toppings()
    order["condiments"] = add_condiments()
    order["sides"] = add_sides()
# The grandtotal is given below.
    Grandtotal = calculate_total(order)
    userhandle_payment
#Using the if function in order to define the name at the very
if __name__ =="__main__":
    main()