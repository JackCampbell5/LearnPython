# Part Three

## In This Lesson
#### [For Loops](#part-a-for-loops-)
#### [While Loops](#part-b-while-loops-)
#### [Try Except(Simple)](#part-c-try-except-)
#### [Methods](#part-d-methods-)


## Part A For Loops:  
+ To create a loop for a certain amount of time put "for in range(num)"
+ a starts at 0 NOT 1 and goes to the number before the range
```python
for a in range(10):
    print(a)
# 0 1 2 3 4 5 6 7 8 9
```
+ To loop through characters in a string "for x in strName:" when x represents the char
```python
var = "Name"
for a in var:
    print(a)
```
+ You can use continue if you want to immediately start the next loop
```python
for a in range(10):
    if a%2 == 0:
        continue
    print(a)
```
+ If you want to stop the loop immediately type break 
```python
for a in range(12):
    if a == 10:
        break
    print(a)
```
#### You Try
+ Print the odd numbers 1-20
+ Print the characters in "characters" on new lines


## Part B While Loops: 
+ You can do while loops for while a boolean var is true while(boolean_val):
```python
val = True
num = 70
while(val):
    if num ==70:
        val = False
```
+ You can do while true to do an infinite loop until a break command

```python
while True:
    num = input("Number:")
    num += 10
    if num == 70:
        print(num)
        break
```
+ You can also increment it like a normal for loop
```python
num = 0
while num <100:
    print(num)
    num+=num
```
#### You Try
+ Print out the odd numbers 1-100 using a while loop 


## Part C Try Except: 
+ Try Except is how to track for error(especially in user input) in python
```python
try:
    jack = "test"
    jack+=10
except:
    print("This did error but not crash")
```
+ You can add the specified name of an error and run a condition based on it
+ If you are getting user input you want Value Error
+ For any other error look at the console and copy and paste the answer
```python
try:
    num = input("Num: ")
    num = int(num)
    num += 10
except ValueError:
    print("That was not a number :(")
print(num)

```
+ You can add a while loop to keep getting user input until its accurate 
```python
while True:
    try:
        num = input("Num: ")
        num = int(num)
        break
    except ValueError:
        print("That was not a number, please try again!")
num += 10
print(num)
```
#### You Try
+ Get user input until it is a float, add 10 then print it

## Part D Methods: 
+ To type a method do "def method_name():"
+ you do not need a return type for python Methods
+ You can access methods by doing "method_name()"
    + You can use return to return a value
```python
def get_miles():
    return 1234
num = get_miles()
print(num)
```
+ To add params a method do "method_name(param_name1,param_name2):"
```python
def add_24(param):
    return param+24
num = 10
num = add_24(num)
print(num)
```
+ You can use return blank to just auto return
```python
def check_val(val):
    try:
        val = int(val)
        print("This is an int value")
    except ValueError:
        print("Not an int value")
check_val(input("Enter a value"))
```
#### You Try
+ Make a method to add 100 to any value given
+ Make a method to print out if the value given is True or False