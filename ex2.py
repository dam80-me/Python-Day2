# Create a dictionary named student_scores where keys are student names and values are their scores (integers)

student_scores = {
    "Alice":85,
    "Bob":92,
    "Charlie":78,
    "David":95,
    "Eve":88,
    "Frank":70 #Added an extra student for more data
}

print("---Initial Student Scores---")
#Iterate through the dictionary and print each student's name and
for name, score in student_scores.items():
    print(f"{name}: {score}")
print("\n")
