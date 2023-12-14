# return statement is used to return a value from a function
def square(number):
    return number * number

print(square(3))
# here you get 9 as output

def square(number):
    print(number * number)

print(square(3))

# here you get 9 as output but also None as output
# this is because the function does not return anything
# so it returns None by default



# we can also use return statement to exit a function
