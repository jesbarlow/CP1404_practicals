def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
    print(MENU)
    choice = input(">>> ").upper()


    def convert_to_fahrenheit():
        global fahrenheit
        fahrenheit = celsius * 9.0 / 5 + 32


    def convert_to_calsius():
        global celsius
        celsius = 5 / 9 * (fahrenheit - 32)


    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_to_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            convert_to_calsius()
            print("Result: {:.2f} C".format(celsius))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()