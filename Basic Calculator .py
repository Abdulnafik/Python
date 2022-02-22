def basic():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    add =float(num1) + float(num2)
    subtract = float(num1) - float(num2)
    multiply = float(num1) * float(num2)
    Division = float(num1) // float(num2)
    Remainder = num1 % num2
    print("input A for add\n input S for subtract\n input M for multiplication\n input D for Division\n")
    action = input("Chose an action: ")
    if action == "A":
        print(add)
    elif action == "S":
        print(subtract)
    elif action == "M":
        print(multiply)
    elif Selection == "D":
        print(f"{Division} and the reminder is {Remainder}")
    else:
        print("Please chose the correct input")
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
    print(basic())
elif Selection == "2":
    print(square())
elif Selection == "3":
    print(cube())
elif Selection == "4":
    print(sqr_rt())
else:
    print("Please chose the correct option")
