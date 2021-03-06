class Point():
    def __init__(self, inputx, inputy):
        self.x = inputx
        self.y = inputy
p = Point (2, 8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addpassenger(self,name):
        if not self.openseats():
            return False
        self.passengers.append(name)
        return True

    def openseats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Majdi", "Zaid", "Ahmad", "Talal"]

for person in people:
    
        success =  flight.addpassenger(person)
        if success:
            print(f"Added {person} to flight successfully")
        else:
            print(f"No available seats for {person}")

def announce(f):
    def wrapper():
        print("i will run")
        f()
        print("i ran")
    return wrapper

@announce
def hello():
    print("hi")

hello()

people = [
    {"name":"Ahmad Azzeh", "Subjects":"Bio/chem"},
    {"name":"Majdi Shehab", "Subjects":"Bio/chem"},
    {"name":"Zaid Saheb", "Subjects":"CS/Physics"},
    {"name":"Talal Barakat", "Subjects":"Business/Phyics"},
]
def mf(person):
    return person["name"]
people.sort(key=mf)
#people.sort(key=lambda person: person["name"])
print(people)

import sys
try:
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
except ValueError:
    print("numbers only")
    sys.exit(1)

try:
    result = num1 / num2
except ZeroDivisionError:
    print("dont divide by zero")
    sys.exit(1)
    
print(f"{num1} / {num2} = {result}")
