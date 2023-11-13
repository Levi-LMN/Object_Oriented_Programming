# Initialize variables
total_sum = 0
count = 0
number = 0

# Use a while loop to iterate through even numbers from 0 to 100
while number <= 100:
    total_sum += number
    count += 1
    number += 2  # Move to the next even number

# Calculate the average
average = total_sum / count

# Print the sum and average
print(f"Sum of even numbers: {total_sum}")
print(f"Average of even numbers: {average}")
