"""Assignment 2 - Question 38
Calculate sum of digits.
Run this file directly in VS Code.
"""

n = abs(int(input("Enter integer: ")))
total = 0
while n:
    total += n % 10
    n //= 10
print("Sum of digits =", total)
