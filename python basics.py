
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


# 8. Clothing Inventory Manager
# The dictionary is the single source of truth for the inventory.
class ClothingInventoryManager:

    def __init__(self):
        self.quantities = {}

    # Add clothing and quantity to the dictionary.
    def add_clothing(self, name, quantity):
        self.quantities[name] = quantity

    # Save the inventory by rewriting the file.
    def save_clothes(self):
        with open("clothes.txt", "w") as file:
            for clothing, quantity in self.quantities.items():
                file.write(f"{clothing},{quantity}\n")

    # Load the inventory from the file.
    def load_clothes(self):
        try:
            with open("clothes.txt", "r") as file:
                for line in file:
                    line = line.strip()

                    if line:
                        clothing, quantity = line.rsplit(",", 1)
                        self.add_clothing(clothing, int(quantity))

        except FileNotFoundError:
            pass

    # Display all clothing and quantities.
    def display_clothes(self):
        for clothing, quantity in self.quantities.items():
            print(clothing, quantity)

    # Get clothing name and quantity from the user.
    def run(self):
        self.load_clothes()

        name = input("Enter clothing name: ").strip()

        while True:
            quantity = input("Enter quantity: ").strip()
# Try / Except
# try runs code that might cause an error.
# except handles the error instead of stopping the program.
            try:
                quantity = int(quantity)

                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue

                break

            except ValueError:
                print("Please enter a number.")

        self.add_clothing(name, quantity)
        self.save_clothes()

        print("\nClothing Inventory:")
        self.display_clothes()


# Create the inventory manager.
manager = ClothingInventoryManager()

# Start the program.
manager.run()