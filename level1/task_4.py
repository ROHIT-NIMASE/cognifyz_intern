def calculator():
    print("Welcome to the Python Calculator!")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter operator (+, -, *, /, %): ").strip()
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        elif operator == '%':
            result = num1 % num2
        else:
            return "Error: Invalid operator."

        return f"The result is: {result}"
    
    except ValueError:
        return "Error: Please enter valid numbers."

print(calculator())

#Enter the first number: 15
#Enter operator (+, -, *, /, %): /
#Enter the second number: 5
#The result is: 3.0

