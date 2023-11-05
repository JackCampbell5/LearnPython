print("\nPart A:\n")  # Part A
num = 10
if num == 10:
    print("The num is 10")
myStr = "Hello"
if myStr is str:
    print("myStr is a String")

print("\nPart B:\n")  # Part B
num = 15
if num > 0:
    print("Positive Num")
else:
    print("Negetive Num")

age = 22
if age < 2:
    print("Baby")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 55:
    print("Adult")
else:
    print("Old")

print("\nPart C:\n")  # Part C
userInput = input("Type Something: ")
print(userInput)
username = input("Username:")
password = input("Password:")
if username == "Jack" and password == "password":
    print("Access Granted")

print("\nPart D:\n")  # Part D
num = input("Enter a number: ")
num = input(num)
num += 10
print(num)
