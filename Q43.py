"""Assignment 2 - Question 43
Print multiplication tables 1 to 10 using nested loops.
Run this file directly in VS Code.
"""

for i in range(1, 11):
    for j in range(1, 11): print(f"{i*j:4}", end="")
    print()
