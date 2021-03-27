import sys
from termcolor import colored


def alphabet():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.']
    return abc


def table():
    table = {
        ('A', 'B'): (['a', 'b', 'p', 'q', 'e', 'r', 'g', 'h', 'i', 'j', 'k', 'l', 'o', 'f'],
                     ['x', 'c', 'd', 'y', 'z', '.', 'u', 'w', 't', 'v', 'n', 's', 'm', ' ']),
        ('C', 'D'): (['c', 'd', 'e', ' ', 'x', 'j', 'k', 'l', 'm', 'q', 'r', 'w', 't', 'v'],
                     ['a', 'b', 'f', 'g', 'h', 'i', 'y', 'n', 'o', 'p', 'z', 's', '.', 'u']),
        ('E', 'F'): (['w', 'a', 'c', 'b', ' ', 'd', 'g', 'f', 'm', 'l', 't', 's', 'r', 'e'],
                     ['h', 'z', 'x', '.', 'y', 'v', 'j', 'u', 'n', 'k', 'o', 'p', 'q', 'i']),
        ('G', 'H'): (['b', 'c', 'f', 'g', 'h', 'i', 'j', 'o', ' ', 'q', 'r', 'z', 'y', 'p'],
                     ['.', 'd', 'e', 'n', 'm', 'l', 'k', 'v', 'u', 't', 's', 'w', 'x', 'a']),
        ('I', 'J'): (['a', 'b', '.', 'd', 'e', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'c'],
                     ['n', 'o', 'p', 'q', 'r', 'f', ' ', 'h', 'i', 'j', 'k', 'l', 'm', 'g']),
        ('K', 'L'): (['s', 'r', 'q', 'n', 'm', 'l', 'k', ' ', 'g', 'f', 'e', 'b', 'a', 'h'],
                     ['t', 'u', 'p', 'o', 'v', 'w', '.', 'i', 'x', 'y', 'd', 'c', 'z', 'j']),
        ('M', 'N'): (['z', 'y', 'x', '.', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'w'],
                     [' ', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'm']),
        ('O', 'P'): (['a', 'b', 'c', 'g', 'h', ' ', 'm', 'n', 'o', 's', 't', 'u', 'z', 'i'],
                     ['d', '.', 'f', 'j', 'k', 'l', 'p', 'q', 'r', 'v', 'w', 'x', 'y', 'e']),
        ('Q', 'R'): (['a', 't', 'u', 'c', 'd', 'e', 'f', 'g', 'n', 'o', 'p', 'q', ' ', 'r'],
                     ['b', 's', 'v', 'h', 'i', 'j', 'k', 'l', 'm', 'w', 'x', '.', 'y', 'z']),
        ('S', 'T'): (['c', '.', 'w', 'a', 'b', 'e', 'm', 's', 'p', 'o', 't', 'u', 'y', 'r'],
                     [' ', 'q', 'x', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'z', 'v', 'd']),
        ('U', 'V'): (['e', 'p', '.', 'a', 'g', 'k', 'c', 'j', 'm', 'v', 'w', 'x', 's', 'y'],
                     ['f', 'o', 'z', 'b', 'h', 'l', 'd', 'i', ' ', 'u', 't', 'q', 'r', 'n']),
        ('W', 'X'): (['g', 'n', 'a', 'c', 'i', ' ', 'f', 't', 's', 'r', 'u', 'w', 'x', 'e'],
                     ['h', 'm', 'b', 'd', 'j', '.', 'l', 'o', 'p', 'q', 'v', 'z', 'y', 'k']),
        ('Y', 'Z'): (['i', 'l', 'c', 'e', 'a', 'b', 'o', 'q', 'r', 's', 't', 'u', 'v', '.'],
                     ['j', 'k', 'd', 'f', 'g', 'h', 'm', 'n', 'p', 'z', 'y', 'x', 'w', ' ']),
        ('.', ' '): (['x', 'a', '.', 'c', 'o', 'e', 'q', 'g', 't', 'i', 'u', 'k', 'w', 'm'],
                     ['z', ' ', 'b', 'n', 'd', 'p', 'f', 'r', 'h', 's', 'j', 'v', 'l', 'y'])
    }
    return table


def check(table):
    for i in table:
        all = 0
        for j in alphabet():
            if not (j in table[i][0] or j in table[i][1]):
                print(colored(f"ERROR! Character [{j}] NOT FOUND! in {i}", "red", attrs=['bold']))
            else:
                all += 1

        if all == 28:
            print(str(i) + "-" + colored("OK", 'green', attrs=['bold']))


def check_input(text):
    for i in text.lower():
        if i not in alphabet():
            return False
    return True


def read_key():
    key = ''

    while not key:
        key = input(colored("Insert key: ", 'yellow', attrs=['bold'])).upper()
        if not key or key == ' ':
            print("The key cannot be empty! Try again.")
        elif not check_input(key):
            print(colored("Unknown characters were entered. Try again.", 'red', attrs=['bold']))
            key = ''

    return key


def read_message(text="Insert message: "):
    message = ''

    while not message:
        message = input(colored(text, 'yellow', attrs=['bold'])).lower()
        if not message:
            print("The message cannot be empty! Try again.")
        elif not check_input(message):
            print(colored("Unknown characters were entered. Try again.", 'red', attrs=['bold']))
            message = ''

    return message


def substitution(len_message, key):
    key_str = ''
    count, ost = len_message // len(key), len_message % len(key)

    if count > 0:
        for i in range(count):
            key_str += key
    if ost > 0:
        for i in range(ost):
            key_str += key[i]

    print(colored("Substitution...", 'yellow', attrs=['bold']) + ' ' + colored(key_str, 'blue', attrs=['bold']))
    return key_str


def encryption(message, key):
    code = ''
    key_str = substitution(len(message), key)

    for m, k in zip(message, key_str):
        two_abc = []

        for pair in table().keys():
            if k in pair:
                two_abc = table()[pair]
                break

        if m in two_abc[0]:
            index = two_abc[0].index(m)
            code += two_abc[1][index]
        elif m in two_abc[1]:
            index = two_abc[1].index(m)
            code += two_abc[0][index]

    return code


def decryption(code, key):
    message = ''
    key_str = substitution(len(code), key)

    for c, k in zip(code, key_str):
        two_abc = []

        for pair in table().keys():
            if k in pair:
                two_abc = table()[pair]
                break

        if c in two_abc[0]:
            index = two_abc[0].index(c)
            message += two_abc[1][index]
        elif c in two_abc[1]:
            index = two_abc[1].index(c)
            message += two_abc[0][index]

    return message


def menu():
    answer = 0

    while answer == 0:
        try:
            answer = int(input(
                colored("Insert\n[1] - to encryption\n[2] - to decryption\n[3] - to check table\nYour choice: ",
                        "yellow", attrs=['bold'])))
            if answer != 1 and answer != 2 and answer != 3:
                raise ValueError
        except ValueError:
            print(colored("Incorrect input!", "red", attrs=['bold']))
            answer = 0

    if answer == 1:
        key = read_key()
        message = read_message()
        code = encryption(message, key)
        print(colored("Cipher: ", 'yellow', attrs=['bold']) + "\t\t" + colored(code, 'magenta', attrs=['bold']))
        # return code
    elif answer == 2:
        key = read_key()
        message = read_message("Insert cipher:  ")
        code = decryption(message, key)
        print(colored("Message: ", 'yellow', attrs=['bold']) + "\t\t" + colored(code, 'magenta', attrs=['bold']))
        # return code
    elif answer == 3:
        check(table())
        # return 0


if __name__ == '__main__':
    sys.exit(menu())
