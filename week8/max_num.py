num1 = input('enter the first number: ')
num2 = input('enter the second number: ')
num3 = input('enter the third number: ')

if num1 >= num2 and num1 >= num3:
    print(f'{num1} is the maximum')
elif num2 >= num1 and num2 >= num3:
    print(f'{num2} is the maximum number')
else :
    print(f'{num3} is the maximum number')


