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