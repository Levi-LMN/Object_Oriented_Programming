# if statements in Python
# if statements are used to check if a condition is true or false.
# If the condition is true, the code inside the if statement is executed.
# If the condition is false, the code inside the if statement is skipped.
# Syntax:
# if condition:
#     statements
# else:
#     statements
# Example:
# # if statements
# is_hot = False
# is_cold = True

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# imagine the price of a house is $1M. If the buyer has good credit, they need to put down 10% otherwise they need to put down 20%.
# print the down payment

# price is 1M
price = 1000000
credit = str(input('Do you have a good credit (yes/no) '))
if credit == 'yes':
    depo = price * 0.1
    print(f'you need to put down 10% which is {depo}')
elif credit == 'no':
    depo = price * 0.2
    print(f'you need to put down 20% which is {depo}')
else:
    print("invalid input")