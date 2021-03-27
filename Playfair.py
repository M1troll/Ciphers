from termcolor import colored
import sys


def del_repeate(text):
    cut_txt = ''

    for i in text:
        if i not in cut_txt and i != ' ':
             cut_txt += i
        elif i == 'J' and 'I' not in cut_txt:
            cut_txt += 'I'

    print(colored("Short form: ", 'magenta', attrs=['bold']) + colored(cut_txt, 'cyan', attrs=['bold']))
    return cut_txt


def alphabet():
    abc = ['A', 'B', 'C', 'D', 'E',
           'F', ' G', 'H', 'I', 'K',
           'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']
    return abc


def check_input(text):
    for i in text.upper():
        if i not in alphabet():
            return False
    return True


def read_key():
    key = ''

    while not key:
        key = input(colored("Insert key: ", 'magenta', attrs=['bold'])).upper()
        key = del_repeate(key)

        if not key:
            print(colored("The key cannot be empty! Try again.", 'white', attrs=['bold']))
        elif not check_input(key):
            print(colored("Unknown characters were entered. Try again.", 'red', attrs=['bold']))
            key = ''
        elif len(key) > 25:
            key = ''
            print(colored("Sorry, but the key is too long. Try again.", 'blue', attrs=['bold']))

    return key


def create_table(key):
    for i in alphabet():
        if i not in key:
            key += i

    matrix = [[key[i+j] for i in range(5)] for j in range(0, 25, 5)]
    print(colored('Creating of Matrix... ', 'magenta', attrs=['bold']))

    for i in matrix:
        print(colored(i, 'cyan', attrs=['bold']))

    return matrix


def read_message():
    message = ''

    while not message:
        message = input(colored("Insert message: ", 'magenta', attrs=['bold'])).upper()
        if 'J' in message or ' ' in message:
            repl = ''
            for m in message:
                if repl:
                    if m == repl[len(repl)-1] or (m == 'J' and repl[len(repl)-1]):  # Rule №1: None char
                        repl += 'X'
                if m == 'J':
                    repl += 'I'
                elif m != ' ':
                    repl += m
            message = repl

        if len(message) % 2 == 1:
            message += 'X'
        if not message:
            print("The message cannot be empty! Try again.")
        elif not check_input(message):
            print(colored("Unknown characters were entered. Try again.", 'red', attrs=['bold']))
            message = ''

    message = [message[i:i+2] for i in range(0, len(message), 2)]
    return message


def read_cipher():
    cipher = ''

    while not cipher:
        cipher = input(colored('Insert cipher:  ', 'magenta', attrs=['bold'])).upper()
        if not cipher:
            print("The message cannot be empty! Try again.")
        elif not check_input(cipher):
            print(colored("Unknown characters were entered. Try again.", 'red', attrs=['bold']))
            cipher = ''

    cipher = [cipher[i:i + 2] for i in range(0, len(cipher), 2)]
    return cipher


def encryption(message, matrix):
    code = []

    for pair in message:
        x1, x2, y1, y2 = -1, -1, -1, -1
        check_1, check_2 = False, False

        for x in range(5):
            if all([check_1, check_2]):
                break
            for y in range(5):
                if matrix[x][y] == pair[0]:
                    x1, y1 = x, y
                    check_1 = True
                if matrix[x][y] == pair[1]:
                    x2, y2 = x, y
                    check_2 = True
                if all([check_1, check_2]):
                    break

        A, B = '', ''
        if y1 == y2:     # Rule №2: in one column
            if x1 == 4:
                x1 = -1
            if x2 == 4:
                x2 = -1
            A = matrix[x1+1][y1]
            B = matrix[x2+1][y2]
        elif x1 == x2:  # Rule №3: in one row
            if y1 == 4:
                y1 = -1
            if y2 == 4:
                y2 = -1
            A = matrix[x1][y1+1]
            B = matrix[x2][y2+1]
        else:   # Rule №3: in different rows and columns
            A = matrix[x1][y2]
            B = matrix[x2][y1]
        code.append(A+B)

    return code


def decryption(code, matrix):
    message = []

    for pair in code:
        x1, x2, y1, y2 = -1, -1, -1, -1
        check_1, check_2 = False, False
        for x in range(5):
            if all([check_1, check_2]):
                break
            for y in range(5):
                if matrix[x][y] == pair[0]:
                    x1, y1 = x, y
                    check_1 = True
                if matrix[x][y] == pair[1]:
                    x2, y2 = x, y
                    check_2 = True
                if all([check_1, check_2]):
                    break

        A, B = '', ''
        if y1 == y2:    # Rule №2: in one column
            if x1 == 0:
                x1 = 5
            if x2 == 0:
                x2 = 5
            A = matrix[x1 - 1][y1]
            B = matrix[x2 - 1][y2]
        elif x1 == x2:   # Rule №3: in one row
            if y1 == 0:
                y1 = 5
            if y2 == 0:
                y2 = 5
            A = matrix[x1][y1 - 1]
            B = matrix[x2][y2 - 1]
        else:   # Rule №3: in different rows and columns
            A = matrix[x1][y2]
            B = matrix[x2][y1]
        message.append(A + B)

    return message


def menu():
    answer = 0
    matrix = []
    message, key, code = '', '', ''

    while answer == 0:
        try:
            answer = int(input(colored("Insert\n[1] - to encryption\n"
                                       "[2] - to decryption\nYour choice: ", "magenta", attrs=['bold'])))
            if answer != 1 and answer != 2 and answer != 3:
                raise ValueError
            else:
                key = read_key()
                matrix = create_table(key)
        except ValueError:
            print(colored("Incorrect input!", "red", attrs=['bold']))
            answer = 0

    if answer == 1:
        message = read_message()
        for i in encryption(message, matrix):
            code += i
        print(colored("Cipher: ", 'magenta', attrs=['bold'])+"\t\t"+colored(code, 'cyan', attrs=['bold']))
    elif answer == 2:
        message = read_cipher()
        for i in decryption(message, matrix):
            code += i
        print(colored("Message: ", 'magenta', attrs=['bold']) + "\t\t" + colored(code, 'cyan', attrs=['bold']))


if __name__ == '__main__':
    sys.exit(menu())
