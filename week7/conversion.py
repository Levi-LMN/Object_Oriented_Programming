#Type conversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2023 -int(birth_year)
print(age)


#exercisee 3: ask user their weight in pounds,convert it to kgs and print to terminal
weight_lbs = input('what is your weight in pounds ')
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)

#exercise 4:temprature convert Write a Python program that converts a temperature from Fahrenheit to Celsius. Prompt the user to enter a temperature in Fahrenheit and then print out the equivalent temperature in Celsius.
temp_f = input('temperature in Farenheit? ')
temp_c = float(temp_f) - 32 * 5/9
print(temp_c)

#Write a Python program that converts a number of seconds to hours, minutes, and remaining seconds. Prompt the user to enter a number of seconds, and then print out the equivalent time in hours, minutes, and seconds.

# Prompt the user to enter a number of seconds
seconds = int(input("Enter the number of seconds: "))

# Calculate hours, minutes, and remaining seconds
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

# Print the equivalent time in hours, minutes, and seconds
print(f"Equivalent time: {hours} hours, {minutes} minutes, and {seconds} seconds.")

def binary_to_decimal(binary_string):
    decimal_num = 0
    binary_string = binary_string[::-1]  # Reverse the binary string for easier calculation
    
    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            decimal_num += 2 ** i
    
    return decimal_num

# Prompt the user to enter a binary number
binary_number = input("Enter a binary number: ")

# Check if the input is a valid binary number (contains only 0s and 1s)
if all(bit in '01' for bit in binary_number):
    decimal_equivalent = binary_to_decimal(binary_number)
    print(f"The decimal equivalent of {binary_number} is {decimal_equivalent}.")
else:
    print("Invalid input. Please enter a valid binary number.")





#Write a Python program that calculates the Body Mass Index (BMI) of a person. Prompt the user to enter their weight in kilograms and height in meters. 

# Prompt the user to enter weight in kilograms and height in meters
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate BMI using the formula: BMI = weight / (height^2)
bmi = weight_kg / (height_m ** 2)

# Round the BMI to two decimal places
bmi = round(bmi, 2)

# Print the calculated BMI
print(f"Your Body Mass Index (BMI) is: {bmi}")




