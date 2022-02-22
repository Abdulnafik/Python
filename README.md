# Simple Calculator

Simple Calculator has few functions includes all the basic calculations and finding square, square root as well as cube.


## Features

- Basic calcualations such as  
--Addition  
--substarction  
--Multiplication  
--Division  
- To find Sqauare of any number
- To find Cube of any number
- To find Sqauare root of any number


## Prerequisites
> Any IDE(integrated development environment) which support Python

## Explaination


```sh
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

```
Fubction ```basic()``` used to find all the basic calculation for provided ```float()``` variables ```num1``` & ```num2```, also ```if``` statements with variable ```op```  will only accept the operators such as ```+```, ```-```, ```*```, and ```/``` for addition, Subtraction, Multiplication and Division repectively as ```str```, for all other input which will provide an output as ```invalid operator```

### Output of Basic Calculation
>![image](https://user-images.githubusercontent.com/86762727/155142254-19c04e76-f2e0-4adc-ae7e-7da64e5aeba2.png)
>![image](https://user-images.githubusercontent.com/86762727/155142765-366b39c4-f61c-4c36-a333-6113e9b8d399.png)
>![image](https://user-images.githubusercontent.com/86762727/155143062-4ce32a2c-f49a-4559-9372-d7dc12d503e9.png)
>![image](https://user-images.githubusercontent.com/86762727/155143315-e64d4fb6-fa32-4aa9-b09e-871f371eec18.png)
