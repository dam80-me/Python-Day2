# Create the list named temperatures
temperatures =[25.5,28.1,22.9,30.2,27.8,24.3, 29.5]

#Add 31.0 to the end of the temperature list
temperatures.append(31.0)

#Remove the third element (index 2) from the list
temp = temperatures.pop(2)
print(temp)

#Find the maximum and minimum temperature in the list
max_temperature = max(temperatures)
min_temperature = min(temperatures)

#Calculate the average temperature
average_temperature = sum(temperatures)/len(temperatures)

#Print the modofied list, the maximum, minimum, and average temperature
print(f"Modified temperatures list: {max_temperature}")
print(f"Maximum temperatures list: {max_temperature}")
print(f"Minimum temperatures list: {max_temperature}")
print(f"Average temperatures list: {average_temperature: .2f}")