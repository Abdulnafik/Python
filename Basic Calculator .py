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
    else:
        Selection == "D"
        print(f"{Division} and the reminder is {Remainder}")
def square():
    num = input("Enter your number: ")
    return float(num) * float(num)
def cube():
    num = input("Enter your number: ")
    return float(num) * float(num) * float(num)
print("Select the process")
print("input 1 for Basic Calculation\n input 2 to find square \n input 3 to find cube\n")
Selection = input("Select your choice: ")

if Selection == "1":
    print(basic())
elif Selection == "2":
    print(square())
else:
    Selection == "3"
    print(cube())
