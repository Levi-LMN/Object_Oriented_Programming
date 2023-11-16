#if mark 70 - 100 assign Grade A and message as excelent
#if mark 60 - 69 assign Grade B and message as GOOD
#if mark 50 - 59 assign Grade C and message as Fair
#if mark 40 - 49 assign Grade D and message as Below average
#if mark 0 - 39 assign Grade F and message as Poor work
#if mark >100 and <100 assign Grade I and message as invalid

#input mark
mark = int(input("Enter your mark: "))
#check mark and assign grade
if mark >= 70 and mark <= 100:
    grade = "A"
    message = "Excellent"
elif mark >= 60 and mark <= 69:
    grade = "B"
    message = "Good"
elif mark >= 50 and mark <= 59:
    grade = "C"
    message = "Fair"
elif mark >= 40 and mark <= 49:
    grade = "D"
    message = "Below average"
elif mark >= 0 and mark <= 39:
    grade = "F"
    message = "Poor work"
else:
    grade = "I"
    message = "Invalid"
#output grade and message
print("Your grade is: ", grade)
print("Message: ", message)

