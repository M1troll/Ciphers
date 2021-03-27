import os
import sys
from termcolor import colored


def tabula_info():
    info = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25,
        ' ': 26,
    }
    return info


def tabula_recta():
    tabula = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', ' '],
        ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
         'X', 'Y', 'Z', ' ', 'A'],
        ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', ' ', 'A', 'B'],
        ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
         'Z', ' ', 'A', 'B', 'C'],
        ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         ' ', 'A', 'B', 'C', 'D'],
        ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ',
         'A', 'B', 'C', 'D', 'E'],
        ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A',
         'B', 'C', 'D', 'E', 'F'],
        ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B',
         'C', 'D', 'E', 'F', 'G'],
        ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C',
         'D', 'E', 'F', 'G', 'H'],
        ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D',
         'E', 'F', 'G', 'H', 'I'],
        ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E',
         'F', 'G', 'H', 'I', 'J'],
        ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F',
         'G', 'H', 'I', 'J', 'K'],
        ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'J', 'K', 'L'],
        ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L', 'M'],
        ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'N'],
        ['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O'],
        ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
         'L', 'M', 'N', 'O', 'P'],
        ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q'],
        ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R'],
        ['T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S'],
        ['U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
         'P', 'Q', 'R', 'S', 'T'],
        ['V', 'W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U'],
        ['W', 'X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
         'R', 'S', 'T', 'U', 'V'],
        ['X', 'Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W'],
        ['Y', 'Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
         'T', 'U', 'V', 'W', 'X'],
        ['Z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y'],
        [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z']]
    return tabula


def alphabet():
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', ' ']


def check_input(message):
    for i in message:
        if i not in alphabet():
            return False
    return True


def read_key():
    key = ''

    while not key:
        key = input(colored("Insert key: ", 'yellow', attrs=['bold'])).upper().replace(' ', '')
        if not key or key == ' ':
            print("The key cannot be empty! Try again.")
        elif not check_input(key):
            print(colored("Unknown characters were entered. Try again.", 'red', attrs=['bold']))
            key = ''

    return key


def read_message(text="Insert message: "):
    message = ''

    while not message:
        message = input(colored(text, 'yellow', attrs=['bold'])).upper()
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
    tabula, info = tabula_recta(), tabula_info()
    key_str = substitution(len(message), key)
    code = ''

    for m, c in zip(message, key_str):
        x, y = info[m], info[c]
        code += tabula[x][y]

    print(colored("Cipher: ", 'yellow', attrs=['bold']) + "\t\t" + colored(code, 'magenta', attrs=['bold']))
    return code


def decryption(code, key):
    message = ''
    tabula, info = tabula_recta(), tabula_info()
    key_str = substitution(len(code), key)

    for c, k in zip(code, key_str):
        for i in alphabet():
            if c == k:
                message += tabula[0][0]
                break
            x, y = info[k], info[i]
            if tabula[x][y] == c:
                message += i
                break

    print(colored("Message: ", 'yellow', attrs=['bold']) + "\t\t" + colored(message, 'magenta', attrs=['bold']))
    return message


def start():
    answer = 0

    while answer == 0:
        try:
            answer = int(input(
                colored("Insert\n[1] - to encryption\n[2] - to decryption", "yellow", attrs=['bold']) + colored(
                    "\nYour choice: ", "yellow", attrs=['bold'])))
            if answer != 1 and answer != 2:
                raise ValueError
        except ValueError:
            print(colored("Incorrect input!", "red", attrs=['bold']))
            answer = 0

    key = read_key()

    if answer == 1:
        message = read_message()
        encryption(message, key)
    else:
        message = read_message("Insert cipher:  ")
        decryption(message, key)


if __name__ == '__main__':
    sys.exit(start())
