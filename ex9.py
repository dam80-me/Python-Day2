import csv

# Define the name of the CSV file to read from
csv_file_name = "employees.csv"

# Define the department to filter by
target_department = "IT"

print(f"Attempting to read employee data from '{csv_file_name}' and ")

filtered_employees =[]

try:
    # Open the CSV file in read mode ('r').
    with open(csv_file_name, mode='r', newline='') as csv_file:
        # Create a csv.DictReader object.
        # This reader will treat each row as a dictionary using the header row
        reader=csv.DictReader(csv_file)

        # Iterate through each row in the CSV file
        for row in reader:
            # Check if the 'Department' value of the current row matchs the tar
            if row.get('Department')== target_department:
                filtered_employees.append(row)
    print(f"Filtered employee list : {filtered_employees}")

    print(f"\n--- Employees in the '{target_department}' Department---")
    if filtered_employees:
        # Print the Name and Salary of the filtered employees
        for employee in filtered_employees:
            # Using .get() for safer access in case a key is missing
            name=employee.get('Name', 'N/A')
            salary = employee.get('Salary', 'N/A')
        print(f"{filtered_employees}")

except FileNotFoundError:
    print(f"Error: The file '{csv_file_name}' was not found. Please")
except Exception as e:
    print(f"An unexpected error occured: {e}")