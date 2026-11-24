"""Assignment 2 - Question 17
Check even or odd using bitwise operator.
Run this file directly in VS Code.
"""

n = int(input("Enter a number: "))
print("Even" if (n & 1) == 0 else "Odd")
