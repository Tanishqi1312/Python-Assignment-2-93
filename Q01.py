"""Assignment 2 - Question 1
Perform addition, subtraction, multiplication and division.
Run this file directly in VS Code.
"""

a = float(input("First number: "))
b = float(input("Second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", "undefined" if b == 0 else a / b)
