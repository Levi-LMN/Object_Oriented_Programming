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


