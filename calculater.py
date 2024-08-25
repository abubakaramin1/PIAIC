x = input("Enter first number:")
y = input("Enter second number:")
operator = input("Enter operator(+,-,/,*):")
result : int = 0
if operator == "+":
    result = int(x) + int(y)
    print(f'Sum of {x} and {y} is ', result)
elif operator == "-":
    result = int(x) - int(y)
    print(f'Subraction of {x} and {y} is ', result)
elif operator == "*":
    result = int(x) * int(y)
    print(f'Multiplication of {x} and {y} is ', result)
elif operator =="/":
    result = int(x) / int(y)
    print(f'Division of {x} and {y} is ', result)
else:
    print('Invalid operator! Enter a valid operator.')