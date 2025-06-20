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

#Add a new student and their score to the dictionary.
new_student_name = "Grace"
new_student_score = 90
student_scores[new_student_name]=new_student_score
print(f"---Added New Student: {new_student_name} with score {new_student_score}")
for name, score in student_scores.items():
    print(f"{name}: {score}")
print("\n")

# Update the score for an existing student