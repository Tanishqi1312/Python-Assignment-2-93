"""Assignment 2 - Question 33
Sum first N natural numbers.
Run this file directly in VS Code.
"""

n = int(input("Enter N: "))
print("Sum =", n * (n + 1) // 2 if n >= 0 else "Enter a non-negative number")
