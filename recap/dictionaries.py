# dictionaires are key value pairs

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])

# using get method
print(customer.get("name"))
print(customer.get("birthdate", "Jan 1 1980"))

# updating values
customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 1 1980"
print(customer["name"])
print(customer["birthdate"])

# exercise
# write a program to convert numbers into words
phone = (input("input your number: "))
output = ""

mapping = {
    "1" : "one",
    "2" : "Two",
    "3" : "Three",
    "4" : "four"
}

for ch in phone:
   output += mapping.get(ch, "not") + " "
print(output)
