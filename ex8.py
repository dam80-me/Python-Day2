import csv

inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200, "stock": 50},
    {"id": "P002", "name": "Mouse", "price": 25, "stock": 150},
    {"id": "P003", "name": "Keyboard", "price": 75, "stock": 70},
    {"id": "P004", "name": "Monitor", "price": 300, "stock": 25},
    {"id": "P005", "name": "Webcam", "price": 50, "stock": 15}
]

with open("inventory.csv", "w", newline='') as csvfile:
    fieldnames = ["id", "name", "price", "stock"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # write column headers
    for product in inventory:
        writer.writerow(product)

print("Inventory written to inventory.csv")

loaded_inventory = []

with open("inventory.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert price and stock to integers
        row["price"] = int(row["price"])
        row["stock"] = int(row["stock"])
        loaded_inventory.append(row)

print("--- Loaded Inventory ---")
for product in loaded_inventory:
    print(product)