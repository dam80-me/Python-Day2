import json
import datetime

# Create aPython dictionary representing produc information.
# The 'last_updated' timestamp is generated dynamically for demonstration
product_data = {
    "products": [
        {"id": "A1", "name": "Keyboard", "price":75.00, "available":True},
        {"id": "A2", "name": "Mouse", "price":25.50, "available":False},
        {"id": "A3", "name": "Monitor", "price":300.00, "available":True},
        {"id": "A4", "name": "Webcam", "price":50.00, "available":True},
        {"id": "A5", "name": "Headphones", "price":120.00, "available":False}

    ],
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}
#define the name 
json_file_name= "products.json"


try:
#Open the JSON file in write mode('w).
#Using 'with'statement ensures the file is properly closed.
    with open(json_file_name, mode='w', encoding='utf-8') as json_file:

        json.dump(product_data, json_file, indent=4)
        print(f"Successfully wrote product data to '{json_file_name}'.")
    
except IOError as e:
    print(f"Error: Could not write to file '{json_file_name}'.{e}")
except Exception as e:
    print(f"An unexpected error occured: {e}")

print(f"\nPlease check the '{json_file_name}' file manually in a text editor to verify")  


