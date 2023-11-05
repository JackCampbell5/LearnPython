# Part Four Arrays and Numpy

## In This Lesson
#### [Arrays](#part-a-arrays-)
#### [Dictionary](#part-b-dictionary-)
#### Numpy Arrays
#### 


## Part A Arrays:  
+ Arrays are a way to store large amounts of data very easily
+ Start at 0
+ You can create them you put varName = [data1,data2,data3,data4]
+ They can be any types of data
```python
arr = [1,2,3,4,5]
strArr = ["One","Two","Three","Four","Five"]
```
+ You can either print an array or loop through the value
+ You can also loop through the length of the array to get a position
```python
print(arr,strArr)
for a in arr:
    print(a)
for a in range(len(strArr)):
    print(a)
```
+ To edit an array you use brackets [] as long as it is the same type
```python
arr[0] = 10
```
#### You Try
+ Create an array of 1-5 and print it
+ Create an array of your favorite numbers and print all of them with the prefix "Fav Num #"
+ Create an array of 1-5 and then multiply each by 5


## Part B Dictionary: 
+ A dictionary stores value not based on numbers but on keys
+ Dictionary keys are strings but values can be any type and the type does not always have to be the same 
+ Dictonarys are created with {"key":val}
```python
username = "jack"
params = {"name":username,"age":100}
```
+ When looping through a dictionary you loop through based on keys 
```python
for a in params:
    print(a)
```
+ You can loop through and get both keys and the value you do "for(keys,val) in dictName.keys():"
```python
for keys,val in params.items():
    print(keys,val)
```
#### You Try
+ Make a dictionary containing a made up characters first name, last name, and age
+ Print out all the keys in your dictionary and add a 1 to all based on type
+ Print through the keys and values in your dictionary


## Part C Numpy: 
+ Numpy is a python library that is used to help with data science as it has special methods 
```python

```
+ 
```python

```
+ 
```python

```
#### You Try
+ 

## Part D: 
+ 
```python

```
+ 
```python

```
+ 
```python

```
#### You Try
+ 