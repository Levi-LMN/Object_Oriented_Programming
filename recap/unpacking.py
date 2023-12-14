# unpacking a tuple is to assign its values to a sequence of variables

coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
# this is the long way of unpacking a tuple

# this is the short way of unpacking a tuple
x, y, z = coordinates
print(x)
print(y)
print(z)

# unpacking a list
coordinates = [1, 2, 3]
x, y, z = coordinates
print(x)
print(y)
print(z)
