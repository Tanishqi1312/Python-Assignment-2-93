"""Assignment 2 - Question 40
Print primes in a range.
Run this file directly in VS Code.
"""

start, end = map(int, input("Enter start and end: ").split())
for n in range(max(2, start), end + 1):
    if all(n % i for i in range(2, int(n ** 0.5) + 1)):
        print(n, end=" ")
print()
