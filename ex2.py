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



#Find the student with the highest score and print their name and score
if student_scores: #Ensure the dictionary is not empty
    highest_score = 0
    highest_scorer_name =""
    for name, score in student_scores.items():
        if score > highest_score:
            highest_score=score
            highest_scorer_name = name
    print(f"--- Student with the Highest Score ---")
    print(f"{highest_scorer_name}:{highest_score}\n")
else:
    print("The dictionary is empty, cannot find the highest score.\n")

#Create a new dictionary containing only students who scored 90 or