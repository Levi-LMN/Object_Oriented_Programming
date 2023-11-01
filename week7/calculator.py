

num1 = int(input("please input number 1: "))
sign = (input("please input sign: "))
num2 = int(input("please input number 2: "))
if sign == '+':
    z = num1 + num2
    print(z)
elif sign == '-':
    z = num1 - num2
    print(z)
elif sign == '/':
    z = num1 / num2
    print(z)
elif sign == '*':
    z = num1 * num2
    print(z)
else:
    print("done")

