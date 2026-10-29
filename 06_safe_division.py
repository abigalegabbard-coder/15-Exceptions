try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Enter an int!")