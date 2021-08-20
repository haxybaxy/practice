print ("Hello, world! This is Haxy's first pyhton code. This will be used as a tool to showcase outputs for different basic concepts of python. Please have the code open with the application.")
choice = input("What concept would you like to test?  ")

names = ["Majdi", "Ahmad", "Talal"] # needs to be globally declared and not declared in case of something

if choice == "conditions":
    n = int(input("Number: "))
    if n > 0:
        print(f"your number {n} is positive")
    elif n < 0: #else if
        print(f"your number {n} is negative")
    else:
        print("the number is zero")
elif choice == "lists":
    names1 = ["Majdi", "Ahmad", "Talal"] 
    names1.append("Zaid")
    names1.remove(names1[1])
    print(names)
elif choice == "sets":
    s = set()
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    s.add(3) #sets can only hace unique values
    s.remove(2)
    print(s)
    print(f"The set has {len(s)} unique elements")
elif choice == "loops":
    user = input("who r u")
    for i in range(6):
        print(i)
    for friends in names:
        print(friends)
    for character in user:
        print(character)
elif choice == "dictionaries":
    subjects = {"Zaid":"CS", "Majdi":"Bio"}
    subjects["Ahmad"] = "Bio"
    print(subjects["Ahmad"])
elif choice == "functions":
    def square(x):
        return x * x
    for i in range(10):
        print(f"the square of {i} is {square(i)}")
    from add1 import addone
    numero = int(input("enter a number to add one to it"))
    print(addone(numero))



close = input("press enter to end ")
print("code over")