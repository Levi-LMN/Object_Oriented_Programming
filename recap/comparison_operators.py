# comparison opeartors are used to compare values
# There are 6 comparison operators in Python:
# equal to ==
# not equal to !=
# greater than >
# less than <
# greater than or equal to >=
# less than or equal to <=

# Example:
# if temperature is greater than 30 it will print it's a hot day otherwise it will print it's not a hot day

temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# Example:
# if name is less than 3 characters long it will print name must be at least 3 characters otherwise it will print name looks good
name = str(input("what is your name? "))
length = len(name)

if length < 3:
    print("name must be atleast three characters long")
elif length > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good")

