import math
import time

# Basic Calculator
"""
Features:
    Run till typed "exit"
    Addition
    Subtraction
    Multiplication
    Division
    Power
    Square root
    factorial
    Modulus
    Series features : reverse, even , odd (optional)

    Input options:
    2 numbers
    list of numbers

"""


# use * when you wanna pass infinite number of arguments not list
def add(numbers):
    total = 0
    for number in numbers:
        total += number
    print(f"sum of {numbers} = {total}")


def subtract(x, y):
    if x >= y:
        print(x - y)
    else:
        print(y - x)


def multiply(numbers):
    total = 1
    for number in numbers:
        total *= number
    print(f"multiplication of {numbers} = {total}")


def divide(x, y):
    print(x / y)


def power(x, y):
    print(f"{x} to the power {y} = {pow(x, y)}")


def root_over(x, y):
    print(f"{x} root over {y} = {x ** (1. / y)}")


def square_root(x):
    print(f" square root of {x} = {math.sqrt(x)}")


def modulus(x, y):
    print(f"{x} mod {y} = {x % y}")


def factorial(x):
    if x == 1:
        return 1
    else:
        # recursive call to the function
        return x * factorial(x - 1)


def to_radian(x):
    print(math.radians(x))


def find_sin(x):
    print(f" sin{x} = {math.sin(math.radians(x))}")


def find_degree_of_sin(x):
    print(f" inverse sin of {x}= {math.degrees(math.asin(x))} degrees")


def find_cos(x):
    print(f" cos{x} = {math.cos(math.radians(x))}")


def find_degree_of_cos(x):
    print(f" inverse cosine of {x}= {math.degrees(math.acos(x))} degrees")


def find_tan(x):
    if x != 90:
        print(f" tan{x} = {math.cos(math.radians(x))}")


def find_degree_tan(x):
    print(f" inverse tan of {x}= {math.degrees(math.atan(x))} degrees")


def multiple_input():
    a = list(map(int, input("Enter multiple values: ").split()))
    return a


def two_input():
    x, y = [int(x) for x in input("Enter two values: ").split()]
    return x, y


def menu_selector():
    time.sleep(0.2)
    x = int(input("""
           BASIC CALCULATOR
           *****************
           Select Your operation: 
               0. Return to main menu
               1. Addition
               2. Subtraction 
               3. Multiplication 
               4. Division
               5. Modulus 
               6. Power
               7. Square root 
               8. x root over y 
               9. Degree to radian conversion
               10. Find sin
               11. Find cosine 
               12. Find tan
               13. Find inverse sin
               14. Find inverse cosine
               15. Find inverse tan
               16. Find factorial

           """))
    if x > 16 or x < 0:
        print("Invalid Input. Try again")
        menu_selector()
    else:
        menu(x)


def menu(x):
    if x == 0:
        run()
    if x == 1:
        add(multiple_input())
    elif x == 2:
        subtract(*two_input())
    elif x == 3:
        multiply(multiple_input())
    elif x == 4:
        divide(*two_input())
    elif x == 5:
        modulus(*two_input())
    elif x == 6:
        power(*two_input())
    elif x == 7:
        square_root(int(input("Enter a number to find square root:")))
    elif x == 8:
        root_over(*two_input())
    elif x == 9:
        to_radian(float(input("Enter degree to convert: ")))
    elif x == 10:
        find_sin(float(input("Enter degree: ")))
    elif x == 11:
        find_cos(float(input("Enter degree: ")))
    elif x == 12:
        find_tan(float(input("Enter degree: ")))
    elif x == 13:
        find_degree_of_sin(float(input("Enter degree")))
    elif x == 14:
        find_degree_of_cos(float(input("Enter degree")))
    elif x == 15:
        find_degree_tan(float(input("Enter degree")))
    elif x == 16:
        print(factorial(int(input("Enter number: "))))


def run():
    select = input("""
            BASIC CALCULATOR
            ****************
            Enter anything to begin
            Enter 'quit' to exit
    """)
    while True:
        if select.lower() != "quit":
            menu_selector()
        else:
            break


run()
