"""Assignment 2 - Question 39
Check prime using loop.
Run this file directly in VS Code.
"""

n = int(input("Enter integer: "))
if n < 2: prime = False
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
print("Prime" if prime else "Not prime")
