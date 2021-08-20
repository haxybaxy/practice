print ("Hello, world!")
name = input("Name:  ")
print(f"Hello, {name}")
#variables and command structure

n = int(input("Number: "))
if n > 0:
    print(f"your number {n} is positive")
elif n < 0:
    print(f"your number {n} is negative")
else:
    print("the number is zero")
#conditions

names = ["Majdi", "Ahmad", "Talal"]
names.append("Zaid")
names.remove(names[1])
print(names)
#lists

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.remove(2)
print(s)
print(f"The set has {len(s)} unique elements")
#sets

user = input("who r u")
for i in range(6):
    print(i)
for friends in names:
    print(friends)
for character in user:
    print(character)
#for loops

subjects = {"Zaid":"CS", "Majdi":"Bio"}
subjects["Ahmad"] = "Bio"
print(subjects["Ahmad"])
#dictionaries

def square(x):
    return x * x
for i in range(10):
    print(f"the square of {i} is {square(i)}")
from add1 import addone
numero = int(input("enter a number to add one to it"))
print(addone(numero))
#functions


close = input("press enter to end ")
print("code over")