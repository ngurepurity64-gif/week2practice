README.md
Clothing Inventory Manager

Description

The Clothing Inventory Manager is a simple console-based application for managing clothing stock.

This repository contains two versions of the application:

- Java version
- Python version

The applications allow the user to add clothing items, enter quantities, view available clothes and save/load inventory information using a file.

Technologies Used

- Java
- Python
- IntelliJ IDEA
- Visual Studio Code
- Git
- GitHub

Java Version

The Java version is a console application that uses a "Map" as the single source of truth for clothing items and their quantities.

Java Concepts Practiced

- Classes and objects
- Maps
- Loops
- Conditional statements
- Exception handling
- File handling
- User input using "Scanner"

How to Run the Java Version

1. Clone the repository.
2. Open the project in IntelliJ IDEA.
3. Open the "src" folder.
4. Open "ClothingInventorymanager.java".
5. Run the "ClothingInventorymanager" class.
6. Choose an option from the menu:
   - "1" — Add Clothing
   - "2" — View Clothes
   - "3" — Exit
7. Enter the clothing name and quantity when prompted.

The Java version uses "clothes.txt" for file storage.

Python Version

The Python version is a console application that uses a dictionary as the single source of truth for clothing items and their quantities.

Python Concepts Practiced

- Variables
- Lists
- Dictionaries
- Loops
- Functions
- Classes and objects
- Exception handling
- File handling
- User input

How to Run the Python Version

1. Clone the repository.
2. Open the project folder in Visual Studio Code.
3. Open "python basics.py".
4. Run the file using the Python Run button, or open the terminal and run:

python "python basics.py"

5. Enter the clothing name when prompted.
6. Enter the quantity when prompted.

The Python version uses "clothes.txt" for file storage.

File Storage

The inventory applications use "clothes.txt" to store clothing names and quantities.

The inventory is rewritten when it is saved instead of continually appending new copies of the data.

Database Schema

A database schema has been designed and written for the Clothing Store project.

The schema includes:

- Clothes
- Customers
- Orders
- OrderItems

The applications do not currently connect to a database. Database integration is planned for Week 3.

Git and GitHub

Git is used for version control and GitHub is used to store the repository.

Future Improvements

Possible future features include:

- Clothing photos
- More clothing categories
- Search and filtering
- Shoe inventory
- Customer accounts
- Shopping cart
- Clothing recommendationgit log --oneline -5