
# 1. Variables
clothing_name = "trousers"
quantity = 2

print(clothing_name)
print(quantity)


# 2. Lists
clothes = ["trousers", "shorts", "shirts"]

print(clothes)


# 3. Dictionaries
quantities = {
    "trousers": 2,
    "shorts": 4,
    "shirts": 3
}

print(quantities)


# 4. Loops
for clothing, quantity in quantities.items():
    print(clothing, quantity)


# 5. Functions
def display_clothes():
    for clothing, quantity in quantities.items():
        print(clothing, quantity)


display_clothes()


# 6. Classes
# A class is a blueprint for creating objects.
class Clothing:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def display(self):
        print(self.name, self.quantity)


# Create an object from the Clothing class
clothing = Clothing("trousers", 2)
clothing.display()


# 7. Try / Except
# try runs code that might cause an error.
# except handles the error instead of stopping the program.
try:
    quantity = int(input("Enter quantity: "))
    print("Quantity:", quantity)
except ValueError:
    print("Please enter a number.")


# 8. Clothing Inventory Manager
# This class manages clothing and their quantities.
class ClothingInventoryManager:

    # Create an empty dictionary when the manager starts.
    def __init__(self):
        self.quantities = {}

    # Add clothing and its quantity to the dictionary.
    def add_clothing(self, name, quantity):
        try:
            # Convert the quantity into an integer.
            quantity = int(quantity)

            # Store the clothing name and quantity.
            self.quantities[name] = quantity

        except ValueError:
            # Display an error if the quantity is not a number.
            print("Quantity must be a number.")

    # Display all clothing and their quantities.
    def display_clothes(self):
        for clothing, quantity in self.quantities.items():
            print(clothing, quantity)


# Create a Clothing Inventory Manager object.
manager = ClothingInventoryManager()

# Add clothing to the inventory.
manager.add_clothing("trousers", 2)
manager.add_clothing("shorts", 4)
manager.add_clothing("shirts", 3)

# Display the inventory.
manager.display_clothes()