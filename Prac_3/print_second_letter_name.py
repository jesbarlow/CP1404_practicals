while True:
    name = input("What is your name?: ")
    if name.isalpha():
        break
    else:
        print("Sorry, i didn't understand that.")

print (name[::2])