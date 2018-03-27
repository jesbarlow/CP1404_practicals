def main():

    name = get_name()

    print_name(name)


def print_name(name):
    print(name[::2])


def get_name():
    while True:
        name = input("What is your name?: ")
        if name.isalpha():
            break
        else:
            print("Sorry, i didn't understand that.")
    return name


main()