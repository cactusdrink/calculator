import math
import cmath
import statistics

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def square_root(x):
    if x < 0:
        return "Error! Negative number."
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def log(x, base=10):
    if x <= 0 or base <= 0:
        return "Error! Logarithm undefined for non-positive values."
    return math.log(x, base)

def factorial(x):
    if x < 0 or not x.is_integer():
        return "Error! Factorial is not defined for negative or non-integer values."
    return math.factorial(int(x))

def arcsine(x):
    if x < -1 or x > 1:
        return "Error! Value out of domain for arcsine."
    return math.degrees(math.asin(x))

def arccosine(x):
    if x < -1 or x > 1:
        return "Error! Value out of domain for arccosine."
    return math.degrees(math.acos(x))

def arctangent(x):
    return math.degrees(math.atan(x))

def sinh(x):
    return math.sinh(math.radians(x))

def cosh(x):
    return math.cosh(math.radians(x))

def tanh(x):
    return math.tanh(math.radians(x))

def complex_magnitude(real, imag):
    return abs(complex(real, imag))

def complex_phase(real, imag):
    return math.degrees(cmath.phase(complex(real, imag)))

def mean(numbers):
    return statistics.mean(numbers)

def median(numbers):
    return statistics.median(numbers)

def std_dev(numbers):
    return statistics.stdev(numbers)

def main():
    print("Scientific Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Factorial")
    print("12. Arcsine")
    print("13. Arccosine")
    print("14. Arctangent")
    print("15. Hyperbolic Sine")
    print("16. Hyperbolic Cosine")
    print("17. Hyperbolic Tangent")
    print("18. Complex Magnitude")
    print("19. Complex Phase")
    print("20. Mean of a List")
    print("21. Median of a List")
    print("22. Standard Deviation of a List")

    choice = input("Enter choice (1-22): ")

    if choice in ('1', '2', '3', '4', '6', '10', '11'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: ")) if choice not in ('5', '10', '11') else None

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    elif choice == '5':
        num = float(input("Enter number: "))
        print(f"Result: {square_root(num)}")
    elif choice == '6':
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        print(f"Result: {power(base, exponent)}")
    elif choice == '7':
        angle = float(input("Enter angle in degrees: "))
        print(f"Result: {sine(angle)}")
    elif choice == '8':
        angle = float(input("Enter angle in degrees: "))
        print(f"Result: {cosine(angle)}")
    elif choice == '9':
        angle = float(input("Enter angle in degrees: "))
        print(f"Result: {tangent(angle)}")
    elif choice == '10':
        num = float(input("Enter number: "))
        base = float(input("Enter base (default 10): ") or 10)
        print(f"Result: {log(num, base)}")
    elif choice == '11':
        num = float(input("Enter number: "))
        print(f"Result: {factorial(num)}")
    elif choice == '12':
        num = float(input("Enter value for arcsine (between -1 and 1): "))
        print(f"Result: {arcsine(num)}")
    elif choice == '13':
        num = float(input("Enter value for arccosine (between -1 and 1): "))
        print(f"Result: {arccosine(num)}")
    elif choice == '14':
        num = float(input("Enter value for arctangent: "))
        print(f"Result: {arctangent(num)}")
    elif choice == '15':
        angle = float(input("Enter angle in degrees: "))
        print(f"Result: {sinh(angle)}")
    elif choice == '16':
        angle = float(input("Enter angle in degrees: "))
        print(f"Result: {cosh(angle)}")
    elif choice == '17':
        angle = float(input("Enter angle in degrees: "))
        print(f"Result: {tanh(angle)}")
    elif choice == '18':
        real = float(input("Enter real part: "))
        imag = float(input("Enter imaginary part: "))
        print(f"Result: {complex_magnitude(real, imag)}")
    elif choice == '19':
        real = float(input("Enter real part: "))
        imag = float(input("Enter imaginary part: "))
        print(f"Result: {complex_phase(real, imag)}")
    elif choice in ('20', '21', '22'):
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        if choice == '20':
            print(f"Result: {mean(numbers)}")
        elif choice == '21':
            print(f"Result: {median(numbers)}")
        elif choice == '22':
            print(f"Result: {std_dev(numbers)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
