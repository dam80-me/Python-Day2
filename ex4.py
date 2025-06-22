# Represent an inventory using a list of dictionaries.
#Each dictionary represents a product with keys like id, name, price and stock
inventory = [
    {"id":"P001", "name": "Laptop", "price": 1200, "stock":50},
    {"id":"P002", "name": "Mouse", "price": 25, "stock":150},
    {"id":"P003", "name": "Keyboard", "price": 75, "stock":70},
    {"id":"P004", "name": "Monitor", "price": 300, "stock":25},
    {"id":"P005", "name": "Webcam", "price": 50, "stock":15} #Examp
]

print("--- Initial inventory ---")
for product in inventory:
    print(f"ID: {product['id']}, Name: {product['name']}, Stock:{product['stock']}")
print("\n")

def update_stock(product_id, quantity):
    """ Updates the stock for """

    found = False
    for product in inventory:
        if product['id'] ==product_id:
        #Ensure stock does not bo below zero
            if product['stock']  >0:
                product['stock'] =  product['stock'] + quantity
                print(f"Updated stock for {product['name']} (ID: {product_id}. New stock : {product_id['stock']})")
            else:
                print(f"Error: Not enough stock for {product['name']}")
            found = True
            break
    
    if not found:
        print(f"Error: Product with ID '{product_id}' not found in inventory")

def get_low_stock_products (threshold):

    get_low_stock_products = []
    for product in inventory:
        if product['stock'] <threshold:
            get_low_stock_products.append(product['name'])
        return get_low_stock_products
#---Demonstrate the functions---
    
    print("--- Demonstrating Stock Updates---")
    #Demonstrate updating stock for two different products
    update_stock("P001",-10)
    update_stock("P001",-10)
    update_stock("P001",-10)
    update_stock("P001",-10)




        
    
