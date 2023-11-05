# Part Two

## In This Lesson
#### If statements
#### If else statements
#### User Input
#### Casting


## Part A:  
+ If statements are done with just the "if" keyword and a ':' at the end
+ You do not need to have () around a if statement but it will not error
+ You can use the below conditionals to compare
+ Instead of using {} you just indent with tab 

| Condition | What it does             |
|-----------|--------------------------|
| ==        | Equals                   |
| !=        | Not Equals               |
| <         | Less Than                |
| \>        | Greater Than             |
| <=        | Less Than or Equal to    |
| >=        | Greater Than or Equal to |

```python
num = 10
if num == 10:
    print("Hello")
# Will print Hello as num does = 19
```
+ To figure out if a variable is a certain type you can use the is condition
+ When an object has not been initialized the value is None so you can compare to it like a type

```python
# num is initialized to an Integer so checking if it is an integer 
num = 10
if num is int:
    print("Num is an Integer")
```
+ To check 2 conditions you use the and operator by simply typing and
+ If you want to know if 1 var equals 2 things you have to do it independently
+ If you want to check a range of values you can put a value inside < and > sign

```python
num = 30
var = True
if num > 5 and var:
    print("Greater than 5 and True")
if 10 > num > 5:
    print("Num is in the correct range")
```
+ To check 2 conditions you use the or operator by simply typing or
+ This will run if either condition is true and will skip subsequent conditions if the first one is true 

```python
num = 30
var = False
if num > 5 or var:
    print("Greater than 5 and True")
```
+ To check if a boolean is true you can just put if and then the var name
+ TO check if it is not true put not in front of the var name 
```python
var = True
if var:
    print("Var is True")
if not var:
    print("Var is false")
```
#### You Try
+ Create an int value and check if it is equal to its value and print a statement 
+ Create a String value and check if it is a String and print var 


## Part B:If else statements 
+ TO include an else statement you go back on your tabs and type "else:" 
```python
var  = True
if var:
    print("Value is True")
else:
    print("Value is false")
```
+ Else if in python is "elif:"
+ An else if can be included anywhere after an if and before and else as long as it is aligned with the indent 
```python
var  = 10
if var == 9:
    print("Var = 9")
elif var == 8:
    print("Var is 8")
else:
    print("Var is neither 8 or 9")
```
#### You Try
+ Make a num value and print a message if it is positive and something different if it is negetive
+ Make a num value and print whether someone is baby,child,teen,adult, or old


## Part C User Input: 
+ To get user input in python you assign a variable to input("The message you want to show before the input")
```python
inputVar = input()
print(inputVar)
```
#### You Try
+ Take input from the user and print it 
+ Take a input for a username and password form the user and check if sign in is valid 

## Part D Casting: 
+ To cast var you assign a variable to a type(var_you_cast)
```python
num = 10
num2 = float(num)
print(num2)
# 0.0
```
#### You Try
+ Take a number input from the user cast it to a int, add 10 to it and print it
  + Note: If you run into errors do not care we will worry about it later