"""Assignment 2 - Question 25
Check leap year.
Run this file directly in VS Code.
"""

year = int(input("Enter year: "))
leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
print("Leap year" if leap else "Not a leap year")
