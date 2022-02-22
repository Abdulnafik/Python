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
Function ```basic()``` used to find all the basic calculation for provided ```float()``` variables ```num1``` & ```num2```, also ```if``` statements with variable ```op```  will only accept the operators such as ```+```, ```-```, ```*```, and ```/``` for addition, Subtraction, Multiplication and Division repectively as ```str```, for all other input which will provide an output as ```invalid operator```

### Output of Basic Calculation
>Addition  
>![image](https://user-images.githubusercontent.com/86762727/155142254-19c04e76-f2e0-4adc-ae7e-7da64e5aeba2.png)  
Subtraction  
>![image](https://user-images.githubusercontent.com/86762727/155142765-366b39c4-f61c-4c36-a333-6113e9b8d399.png)  
Multiplication  
>![image](https://user-images.githubusercontent.com/86762727/155143062-4ce32a2c-f49a-4559-9372-d7dc12d503e9.png)  
Division  
>![image](https://user-images.githubusercontent.com/86762727/155143315-e64d4fb6-fa32-4aa9-b09e-871f371eec18.png)  
For any other selection of Operator  
>![image](https://user-images.githubusercontent.com/86762727/155144190-eba86811-c615-4512-83f2-dfea96d00352.png)  

    
Function ```square()``` used to find square of any number and will return the output as a ```float()```, and ```num``` is the variable and ```**``` is used to find power of any number, here we have to find power of 2 for provided ```input```, hence using ```** 2```.



```sh
def square():
    num = input("Enter your number: ")
    return float(num) ** 2
```


### Output of Square function  
>![image](https://user-images.githubusercontent.com/86762727/155146971-3caae698-ffcc-42e6-bc5d-f0aa63420664.png)  



Function ```cube()``` used to find square of any number and will return the output as a ```float()```, and ```num``` is the variable and ```**``` is used to find power of any number, here we have to find power of 3 for provided ```input```, hence using ```** 3```.



```sh
def cube():
    num = input("Enter your number: ")
    return float(num) ** 3
```  

### Output of Cube function
>![image](https://user-images.githubusercontent.com/86762727/155147865-dfe5890d-6add-41b3-9e2b-bdafd16fcded.png)  


Function ```sqr_rt()``` used to find square root of any number and will return the output as a ```float()```, and ```num``` is the variable and ```**``` is used to find power of any number, here we have to find square root of provided ```input```, hence using ```** 0.5```, Which is same as square root.

```sh
def sqr_rt():
    num = input("Enter your number: ")
    return float(num) ** 0.5
```  
### Output of sqr_rt function
>![image](https://user-images.githubusercontent.com/86762727/155151826-31d72bf5-8539-43bf-886e-846145e2cf56.png)  
    

