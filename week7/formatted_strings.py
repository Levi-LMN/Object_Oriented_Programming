#formatted strings
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

#exercise :Create a formatted string that asks for a user's name and their age, and then prints a message using this information.
name = input('what is your name? ')
age = input('what is your age? ')
msg = f'Hello {name} you are {age} years old'
print(msg)

#execise 2:Write a program that asks the user for an amount in dollars and converts it to euros using a formatted string. Assume the exchange rate is 0.85.
amount = input('The the amount in dollars: ')
eur = int(amount) * 0.85
amt = f'${amount} is equal to {eur} Euros'
print(amt)

