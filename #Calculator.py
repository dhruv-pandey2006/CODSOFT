#Calculator
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
print("Choose Operator :")
print("+ for Addition")
print("- for Subtraction")
print("* for multiplication")
print("/ for division")
operation = input("Enter operation:")
if operation == '+':
    print("Result:",num1+num2)
elif operation =='-':
    print("Result:",num1-num2)
elif operation =='*':
    print("Result:",num1*num2)
elif operation =='/':
    print("Result:",num1/num2)
else:
    print("Invalid Operator")
