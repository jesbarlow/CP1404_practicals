"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
       - value errors occur when the input os anything other than a number(including negative numbers),for example - the
       letter a
2. When will a ZeroDivisionError occur?
       - this will occur whenever the user inputs 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
       - yes, with input validation and a while loop that will just continue asking the user to
       re enter a number until that number is no longer 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")