import csv

# Create a list of dictionaries, where each dictionary represents an
employees_data = [
        {"Name": "Alice Smith", "Department": "HR", "Salary":60000},
        {"Name": "Bob Johnson", "Department": "IT", "Salary":75000},
        {"Name": "Charlie Brown", "Department": "Finace", "Salary":80000},
        {"Name": "Diana Prince", "Department": "Marketing", "Salary":65000},
        {"Name": "Eve Adams", "Department": "IT", "Salary":70000}
        ]

# Define the name of the CSV file
csv_file_name = "employees.csv"

# Define the feild names (headers) for the csv file
# These should match the keys in your employee dictionaries
fieldnames = ["Name", "Department", "Salary"]

print(f"Attempting to write employee data to '{csv_file_name}' ...")

try:
    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()
        print("CSV headers written.")

        #Write all employee data rows
        writer.writerows(employees_data)
        print(f"Successfully wrote {len(employees_data)} employee recordes to '{csv_file_name}'")

except IOErroras as e:
    print(f"Error: Could not write to file '{csv_file_name}.{e}")
except Exception as e:
    print(f"An unexpected error occured: {e}")