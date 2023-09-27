import math

def print_circum(radius):
    circumference = 2 * math.pi * radius
    print(f"The circumference of a circle with radius {radius} is {circumference:.5f}")

# Calling the function with different radius values
print_circum(2.0)
print_circum(3.5)
print_circum(1.2)

'''
# Expected output:
The circumference of a circle with radius 2.0 is 12.56637
The circumference of a circle with radius 3.5 is 21.99115
The circumference of a circle with radius 1.2 is 7.53982
'''
