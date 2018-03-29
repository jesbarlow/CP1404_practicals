def main():
    usernames = ['jimbo', 'glitson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', "InterpreterInterface", 'Startserver', 'bob']

    user = input("Enter your username: ")
    check_username(user)


def check_username(user, usernames):
    if user in usernames:
        print('Access Granted')
    else:
        print('Access Denied!')


