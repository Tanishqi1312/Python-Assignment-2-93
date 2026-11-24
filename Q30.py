"""Assignment 2 - Question 30
Calculate electricity charges using slabs and nested if.
Run this file directly in VS Code.
"""

units = float(input("Enter electricity units: "))
if units < 0:
    print("Units cannot be negative.")
else:
    if units <= 100: bill = units * 1.5
    elif units <= 200: bill = 100 * 1.5 + (units - 100) * 2.5
    else: bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    print("Bill amount =", bill)
