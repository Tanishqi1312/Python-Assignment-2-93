"""Assignment 2 - Question 3
Calculate remainder without modulus.
Run this file directly in VS Code.
"""

a = int(input("Dividend: "))
b = int(input("Divisor: "))
if b == 0:
    print("Division by zero is not allowed.")
else:
    remainder = a - (a // b) * b
    print("Remainder =", remainder)
