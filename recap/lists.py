# finding largest number

num1 = int(input("input number 1: "))
num2 = int(input("input number 2: "))
num3 = int(input("input number 3: "))

if num1 > num2 and num1 > num3:
    print(f'{num1} is the largest')
elif num2 > num1 and num2 > num3:
    print(f'{num2} is the largest')
else:
    print(f'{num3} is the largest')

# the largest number in a list
mylist = [4, 5, 7, 1, 9]
maximum = mylist[0]

for item in mylist:
    if item > maximum:
        maximum =item
print(maximum)