try:
    userIndex = int(input("Enter an index: "))
    animals = ["Dog", "Cat", "Rabbit", "Duck", "Horse"]
    print(animals[(userIndex-1)])
except ValueError:
    print("Enter a valid int!")
except IndexError:
    print("That index does not exist!")