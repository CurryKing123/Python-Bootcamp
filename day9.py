# programming_dictionary = {
#     "Bug": "Error",
#     "Function": "Code to call again",
# }

# programming_dictionary["Loop"] = "The action of doing something over again"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score in range(91, 100):
        student_grades[student] = "Outstanding"
    elif score in range(81, 90):
        student_grades[student] = "Exceeds Expectations"
    elif score in range(71, 80):
        student_grades[student] = "Acceptable"
    elif score in range(0, 70):
        student_grades[student] = "Fail"