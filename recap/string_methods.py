# len is used to find the length of a string
course = 'Python for Beginners'
print(len(course))

# upper is used to convert a string to uppercase
course.upper()
print(course.upper())

# lower is used to convert a string to lowercase
course.lower()
print(course.lower())

# find is used to find a character in a string
print(course.find('P')) # this is case sensitive
print(course.find('p')) # this is case sensitive if not found it returns -1
print(course.find('o'))

# replace is used to replace a character in a string
print(course.replace('Beginners', 'Absolute Beginners'))

# in is used to check if a character is in a string
print('Python' in course) # returns boolean value which is true.It is case sensitive

# in is used to check if a character is in a string and returns boolean value while
# find returns the index of the character