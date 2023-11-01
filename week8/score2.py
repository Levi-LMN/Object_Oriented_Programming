from prettytable import PrettyTable

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

# Create a table and add rows
table = PrettyTable(['Student Number', 'Student Name', 'Unit Code', 'Unit Name', 'CAT Mark', 'Exam Mark', 'Final Score', 'Grade'])
table.add_row([student_number, student_name, unit_code, unit_name, cat_mark, exam_mark, cat_mark + exam_mark, grade])

# Print the table
print(table)

