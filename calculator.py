num1 = float(input("Please enter the first number: "))
operation = input("Please choose an arithmetical operation '+,-,*,/': ")
num2 = float(input("Please enter the second number: "))
if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
else:
    print("Incorrect character")
