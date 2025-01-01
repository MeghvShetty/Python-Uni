def make_pizza(crust, sauce, topping):
    print(f"Preparing {crust} dough.")
    print(f"Preparing {sauce} sauce")
    print(f"Adding toppings {','.join(topping)}.")
    print("Baking the pizza.")
    print("Pizza is ready to be served!")
    return "Pizza made successfully"


# Define the requirements
crust = "thin crust"
sauce = "tomato"
topping =["mozzarella","pepperoni","olives"]


# Make the pizza 
result = make_pizza(crust,sauce,topping)

print (result)