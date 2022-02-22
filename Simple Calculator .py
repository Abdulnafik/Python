def basic():
    num1 = float(input("Enter first number: "))
    op = input("Chose operator: ")
    num2 = float(input("Enter second number: "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("Invalid operator")
def square():
    num = input("Enter your number: ")
    return float(num) ** 2
def cube():
    num = input("Enter your number: ")
    return float(num) ** 3
def sqr_rt():
    num = input("Enter your number: ")
    return float(num) ** 0.5
print("Select the process")
print("input 1 for Basic Calculation\n input 2 to find square \n input 3 to find cube\n input 4 to find square root")
Selection = input("Select your choice: ")

if Selection == "1":
    basic()
elif Selection == "2":
    print(square())
elif Selection == "3":
    print(cube())
elif Selection == "4":
    print(sqr_rt())
else:
    print("Please chose the correct option")
