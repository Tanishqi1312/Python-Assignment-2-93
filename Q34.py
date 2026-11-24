"""Assignment 2 - Question 34
Calculate factorial using loop.
Run this file directly in VS Code.
"""

n = int(input("Enter a non-negative integer: "))
factorial = 1
for i in range(1, n + 1): factorial *= i
print("Factorial =", factorial)
