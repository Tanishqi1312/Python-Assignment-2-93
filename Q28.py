"""Assignment 2 - Question 28
Check vowel or consonant.
Run this file directly in VS Code.
"""

ch = input("Enter a single alphabet: ").lower()
if len(ch) != 1 or not ch.isalpha(): print("Please enter one alphabet.")
elif ch in "aeiou": print("Vowel")
else: print("Consonant")
