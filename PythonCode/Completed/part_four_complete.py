print("\nPart A:\n")  # Part A
arr = [1, 2, 3, 4, 5]
print(arr)
favNum = [8, 5, 15, 11, 12]
for a in favNum:
    print("Fav Num #", a)
arr2 = [1, 2, 3, 4, 5]
for a in range(len(arr2)):
    arr2[a] *= arr2[a]
print(arr2)
print("\nPart B:\n")  # Part B
params = {"first": "jack", "last": "Campbell", "age": 1000}
for a in params:
    if type(params[a]) is str:
        params[a] += "1"
    else:
        params[a]+=1
print(params)
# for a,b in params.items():
#     print(a,b)
print("\nPart C:\n")  # Part C

print("\nPart D:\n")  # Part D
