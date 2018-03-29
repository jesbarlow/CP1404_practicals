import random

def main():

    quick_picks = int(input("How many quick picks? "))
    print_quickpicks(quick_picks)


def print_quickpicks(quick_picks):
    for num in range(quick_picks):
        NUMBERS = [random.randrange(1, 46) for i in range(0, 6)]
        NUMBERS.sort()
        number_line = ['%.2d' % number for number in NUMBERS]
        print(*number_line)

main()



