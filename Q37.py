"""Assignment 2 - Question 37
Count digits in an integer.
Run this file directly in VS Code.
"""

n = abs(int(input("Enter integer: ")))
count = 1 if n == 0 else 0
while n > 0:
    count += 1
    n //= 10
print("Number of digits =", count)
