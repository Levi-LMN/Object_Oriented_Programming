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




#Ask the user for a string and a number, and then print the string repeated that many times using formatted strings.
strng = input('Enter a string: ')
num = int(input("enter a number: "))
print("the repeated string is", strng * num)




#Create a program that asks the user for a temperature in Celsius and converts it to Fahrenheit using a formatted string. The conversion formula is: F = (C * 9/5) + 32.
temp_cel = input("Enter the temperature in Celsius: ")
temp_f = (int(temp_cel) * 9/5) + 32
print(f'{temp_cel} degrees celsius is equal to  {temp_f}F')

