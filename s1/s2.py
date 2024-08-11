num1 =int(input("enter a number: "))
operator = input("enter an operator: ")
num2 = int(input("enter a number: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '%':
    print(num1 % num2)
else :
    print('invaled operator')
