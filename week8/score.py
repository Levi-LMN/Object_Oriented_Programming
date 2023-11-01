# Function to calculate final score and determine grade
def calculate_grade(cat_mark, exam_mark):
    final_score = cat_mark + exam_mark
    if final_score >= 70:
        return 'A'
    elif final_score >= 60:
        return 'B'
    elif final_score >= 56:
        return 'C'
    elif final_score >= 50:
        return 'D'
    else:
        return 'F'

# Capture student information
student_number = input("Enter student number: ")
student_name = input("Enter student name: ")
unit_code = input("Enter unit code: ")
unit_name = input("Enter unit name: ")
cat_mark = float(input("Enter CAT mark: "))
exam_mark = float(input("Enter exam mark: "))

# Calculate final score and determine grade
grade = calculate_grade(cat_mark, exam_mark)

# Display information in tabular format
print("\nStudent Information")
print("---------------------------")
print(f"Student Number: {student_number}")
print(f"Student Name: {student_name}")
print(f"Unit Code: {unit_code}")
print(f"Unit Name: {unit_name}")
print(f"CAT Mark: {cat_mark}")
print(f"Exam Mark: {exam_mark}")
print(f"Final Score: {cat_mark + exam_mark}")
print(f"Grade: {grade}")

