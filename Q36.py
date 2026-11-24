"""Assignment 2 - Question 36
Reverse integer using while loop.
Run this file directly in VS Code.
"""

n = abs(int(input("Enter integer: ")))
reverse = 0
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
print("Reversed =", reverse)
