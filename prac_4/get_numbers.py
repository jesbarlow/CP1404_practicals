def main():
    numbers = []
    get_numbers()
    print_numbers()

def get_numbers(numbers):
    for i in range(5):
        number = int(input("Enter a number:"))
        numbers.append(numbers)

def print_numbers(numbers):
    print("The first number is", numbers[0])
    print("The last number ", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is ", max(numbers))
    print("The average of all numbers is", sum(numbers) / len(numbers))


print_numbers()