"""Assignment 2 - Question 10
Calculate sum of digits of a two-digit number.
Run this file directly in VS Code.
"""

number = abs(int(input("Enter a two-digit number: ")))
print("Sum of digits =", number // 10 + number % 10)
