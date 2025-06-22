# --- New Code for Set Operations and List De-duplication ---

print("---Set Operations---")

# Create two sets
set_a={ 10,20,30,40,50}
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