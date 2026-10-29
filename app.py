"""
Exception: What is thrown when an error in your application occurs
Crashes your program

print(4/0) - ZeroDivisionError : division by zero

str = "Cheese"
if str > 1:
    print(5)
TypeError: '>' not supported between instances of 'str' and 'int'

print(int("A"))

CoolFunction
NameError: name 'coolFunction' is not defined

Try: The code block that is potentially dangerous
Except: The code to run if an exception occurs
Finally: The block of code that runs after a try/except either way

"""
#try:
#    num1 = int(input("Enter the first number: "))
#    num2 = int(input("Enter the second number: "))
#    print(num1/num2)
#except ZeroDivisionError:
#    print("Cannot divide by zero")
#except ValueError:
#    print("Enter a valid integer")

#try:
#    num1 = int(input("Enter the first number: "))
#    num2 = int(input("Enter the second number: "))
#    print(num1/num2)
#except (ZeroDivisionError, ValueError):
#    print("An error occurred")

#try:
#    num1 = int(input("Enter the first number: "))
#    num2 = int(input("Enter the second number: "))
#    print(num1/num2)
#except Exception:
#    print("An error occurred")

file = open("somefile.txt", "w")

try:                                              
    num1 = int(input("Enter the first number: ")) 
    num2 = int(input("Enter the second number: "))
    print(num1/num2)                              
except ZeroDivisionError:                         
    print("Cannot divide by zero")
except ValueError:
    print("Enter a valid integer")
finally:
    print("Operation complete")