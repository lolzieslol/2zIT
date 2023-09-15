"""
import random as rd

mint = 0

while (mint < 20):
    mint+=rd.randint(1,7)
    print("mint:", mint, end=", ")

print()
print("concluded")
"""

intager = input("input a number: ")

try: 
    intager = int(intager)
    print(f"you wrote {intager}. ")
except ValueError:
    print("needs to be an intager. ")
    
    print(f"asdf {intager}")
    print("asdf "+intager)
    
    