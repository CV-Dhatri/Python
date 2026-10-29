# Task 20 
# Print products whose stock is below 10. 
# String Processing Tasks

products = [
    {"name": "Product 1", "stock": 5},
    {"name": "Product 2", "stock": 15},
    {"name": "Product 3", "stock": 8},
    {"name": "Product 4", "stock": 20}
]

for product in products:
    if product["stock"] < 10:
        print(f"Product: {product['name']}, Stock: {product['stock']}")