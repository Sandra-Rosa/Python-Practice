# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# The user's inputs for the numbers and the operators
# Simple python code for basics mathematical operations such as Addition,Substractio,Multiplication and Division of two numbers
# Disadvantage: Only two numbers can be operated
# Asks the operator
Operator = input('Enter operator: ')
# Asks the numbers for operation
num1 = float(input('Enter your first number: '))
num2 = float(input('Enter your second number: '))
# if else operator
# if Operator is (+ | - | * | /) then  print out number 1 (+ | - | * | /) number 2
if Operator == '+':
    print(num1 + num2)
elif Operator == '-':
    print(num1 - num2)
elif Operator == '/':
    print(num1 / num2)
elif Operator == '*':
    print(num1 * num2)

# if the user didn't put an operator
else:
    print('Not a valid operator')
