# methods to do in a list

# 1. append() - adds an element to the end of the list
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

# 2. insert() - adds an element at a specified index
numbers.insert(0, 10)
print(numbers)

# 3. remove() - removes an element from the list
numbers.remove(5)
print(numbers)

# 4. clear() - removes all elements from the list
numbers.clear()
print(numbers)

# 5. pop() - removes the last element from the list
numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

# 6. index() - returns the index of the specified element
numbers = [5, 2, 1, 7, 4]
print(numbers.index(5))
print(numbers.index(7))

# 7. count() - returns the number of times an element appears in the list
numbers = [5, 2, 1, 7, 4, 5]
print(numbers.count(5))

# 8. sort() - sorts the list
numbers = [5, 2, 1, 7, 4]
numbers.sort()
print(numbers)

# 9. reverse() - reverses the list
numbers = [5, 2, 1, 7, 4]
numbers.reverse()
print(numbers)

# 10. copy() - returns a copy of the list
numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()
print(numbers2)
print(numbers)

print("this is EXERCIESE")
# write a program to remove the duplicates in a list
numbers = [5, 2, 1, 7, 4, 5]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
print(numbers)

