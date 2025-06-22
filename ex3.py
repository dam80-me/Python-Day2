# --- New Code for Set Operations and List De-duplication ---

print("---Set Operations---")

# Create two sets
set_a={ 10,20,30,40,50,100}
set_b= {40,50,60,70,80}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

#Find the union of set_a and set_b and print the result.
#The union contains all unique elements from both sets.

union_set = set_a.union(set_b)
print(f"Union of Set A and Set B: {union_set}")

#Find the intersection of set_a and set_b and print the result.
#The intersection contains elements common to both sets.

intersection_set = set_a.intersection(set_b)
print(f"Intersection of Set A and Set B: {intersection_set}")

difference_set = set_a.difference(set_b)
print(f"Difference ( Set A - Set B): {difference_set}")

print("n--- List De-duplication using Sets ---")

# Create a list with duplicate elements
my_list =[1,2,2,3,4,4,5,1,6]
print(f"Original list with duplicates: {my_list}")

#Convert my_list to a set to remov duplicates.
#Sets inherently store only unique elements.
unique_elements_set = set(my_list)
print(f"List converted to set (duplication removed):{unique_elements_set}")

unique_list = list(unique_elements_set)