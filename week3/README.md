##Week 3: Conditional Statements, Boolean Logic, and Comparison Operators
1. Conditional Statements (if, elif, else)
Conditional statements in Python are used to make decisions based on the evaluation of conditions. The basic syntax includes if, elif (short for "else if"), and else.

Example:
```
# Conditional statement with if, elif, and else
x = 10

if x > 0:
    print("x is positive.")
elif x == 0:
    print("x is zero.")
else:
    print("x is negative.")
```
In this example:

If x is greater than 0, it prints "x is positive."
If x is equal to 0, it prints "x is zero."
If x is negative, it prints "x is negative."
2. Boolean Logic (and, or, not)
Boolean operators (and, or, not) are used to combine conditional statements and perform logical operations.

Example:
```
# Boolean logic operators
is_sunny = True
is_warm = False

if is_sunny and is_warm:
    print("It's a sunny and warm day.")
elif is_sunny or is_warm:
    print("It's either sunny or warm.")
else:
    print("It's neither sunny nor warm.")
```
In this example:

and: True if both conditions are true.
or: True if at least one condition is true.
not: True if the condition is false.
3. Comparison Operators (<, <=, >, >=, ==, !=)
Comparison operators are used to compare values and return a boolean result (True or False).

Examples:
```
# Comparison operators
a = 5
b = 10

print(a < b)  # Output: True
print(a >= b)  # Output: False
print(a == b)  # Output: False
print(a != b)  # Output: True
```


In this example:

<: Less than
<=: Less than or equal to
>: Greater than
>=: Greater than or equal to
==: Equal to
!=: Not equal to
Understanding conditional statements, boolean logic, and comparison operators allows you to create programs that make decisions based on specific conditions. Practice creating different conditional statements and combining them with boolean logic to control the flow of your programs effectively.





