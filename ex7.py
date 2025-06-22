# Represent an inventory using a list of dictionaries.
# Each dictionary represents a product with keys like id, name, price and stock
inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200, "stock": 50},
    {"id": "P002", "name": "Mouse", "price": 25, "stock": 150},
    {"id": "P003", "name": "Keyboard", "price": 75, "stock": 70},
    {"id": "P004", "name": "Monitor", "price": 300, "stock": 25},
    {"id": "P005", "name": "Webcam", "price": 50, "stock": 15}
]

print("--- Initial inventory ---")
for product in inventory:
    print(f"ID: {product['id']}, Name: {product['name']}, Stock: {product['stock']}")
print("\n")


def update_stock(product_id, quantity):
    """Updates the stock for a product by a given quantity"""
    found = False
    for product in inventory:
        if product['id'] == product_id:
            new_stock = product['stock'] + quantity
            if new_stock < 0:
                print(f"Error: Cannot reduce stock of {product['name']} below zero.")
            else:
                product['stock'] = new_stock
                print(f"Updated stock for {product['name']} (ID: {product_id}). New stock: {product['stock']}")
            found = True
            break

    if not found:
        print(f"Error: Product with ID '{product_id}' not found in inventory.")


def get_low_stock_products(threshold):
    """Returns a list of product names that have stock below the given threshold"""
    low_stock = []
    for product in inventory:
        if product['stock'] < threshold:
            low_stock.append(product['name'])
    return low_stock


# --- Demonstrate the functions ---
print("--- Demonstrating Stock Updates ---")
update_stock("P001", -10)
update_stock("P001", -10)
update_stock("P001", -10)
update_stock("P001", -10)

print("\n--- Products with Low Stock (threshold < 20) ---")
low_stock_items = get_low_stock_products(20)
print("Low stock products:", low_stock_items)