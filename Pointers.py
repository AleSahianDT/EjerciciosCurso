#Intergers (are inmutable and can't be changed)
num1 = 11
num2 = num1

print("Before num2 value is updated: ")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("\nnum2 points to:", id(num2))

num2 = 22

print("\nAfter num2 value is updated: ")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

#Dictionary (we are able to change the value, and where the variables point to)

dict1 = {
        'value': 11
        }
dict2 = dict1

print("\nBefore value is updated: ")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("\ndict2 points to:", id(dict2))

dict2['value'] = 22

print("\nAfter value is updated: ")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("\ndict2 points to:", id(dict2))

#Garbage Collection: Where python sends values is any variable is pointing it