"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        number = int(input("Please enter a integer:"))
        result = 0 + number
        break
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
