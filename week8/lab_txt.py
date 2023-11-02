
a = 7
b = 2
# addition
print ('Sum: ', a + b)
# subtraction
print ('Subtraction: ', a - b)
# multiplication
print ('Multiplication: ', a * b)
# division
print ('Division: ', a / b)
# floor division
print ('Floor Division: ', a // b)
# modulo
print ('Modulo: ', a % b)
# a to the power b
print ('Power: ', a ** b)
print('\n')



# assign 10 to a
a = 10
# assign 5 to b
b = 5
# assign the sum of a and b to a
a += b      # a = a + b
print(a)

print('\n')


a = 5
b = 2
# equal to operator
print('a == b =', a == b)
# not equal to operator
print('a != b =', a != b)
# greater than operator
print('a > b =', a > b)
# less than operator
print('a < b =', a < b)
# greater than or equal to operator
print('a >= b =', a >= b)
# less than or equal to operator
print('a <= b =', a <= b)

#print new line
print('\n')


#logical operators
#logical and
print(True and False) # False
#logical or
print(True or False) # True
#logical not
print(not True) # False


#Example 1: Python if statement
number = 10
# check if number is greater than 0
if number > 0:
    print('Number is positive.')
print('The if statement is easy')


#Example 2: Python if...else statement
number = 10
if number > 0:
    print('Positive number')
else:
    print('Negative number')
print('This statement is always executed')







##if age 1-18 print "You are young."
##if age 19-35 print "youth"
##if age 36-50 print "adult"
##if age 51-70 print "old"
##if age 71-100 print "senior citizen"
##if age >100 and <0 print "invalid age"

age = int(input("Enter your age: "))
if age >= 1 and age <= 18:
    print("You are young.")
elif age >= 19 and age <= 35:
    print("Youth")
elif age >= 36 and age <= 50:
    print("Adult")
elif age >= 51 and age <= 70:
    print("Old")
elif age >= 71 and age <= 100:
    print("Senior Citizen")
elif age > 100 or age < 0:
    print("Invalid Age")


languages = ['Swift', 'Python', 'Go', 'JavaScript']
# run a loop for each item of the list
for y in languages:
    print(y)
print('\n')

# run a loop for each character of the string
for x in 'python':
    print(x)
print('\n')

# run a loop for each number in the range
for x in range(0, 10):
    print(x)
print('\n')


# use of range() to define a range of values
values = range(4, 10)
# iterate from i = 0 to i = 3
for i in values:
    print(i)

