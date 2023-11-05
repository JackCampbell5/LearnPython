print("\nPart A:\n")  # Part A
for a in range(100):
    if a % 2 == 0:
        continue
    print(a)
var = "characters"
for a in var:
    print(a)

print("\nPart B:\n")  # Part B
num = 1
while num < 100:
    print(num)
    num += 2

print("\nPart C:\n")  # Part C
while True:
    try:
        num = input("Float: ")
        num = float(num)
        break
    except ValueError:
        print("That was not a Float, please try again!")
print(num)

print("\nPart D:\n")  # Part D


def add_100(num):
    return num + 100


def bool_print(bool_val):
    if bool_val:
        print("Value is True")
    else:
        print("Value is False")


num = add_100(10)
bool_print(True)
