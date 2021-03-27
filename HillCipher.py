import numpy as np
import sys
from math import sqrt
from termcolor import colored


def alphabet():
    """Возвращает кодированный алфафит в виде словаря"""
    ABC = {
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
           '.': 26,
           ' ': 27,
           '@': 28
    }
    # Символ @ будет использован для дещифровки в случае,
    # если сообщение нельзя было разбить на одинаковые по длине, равной корню и зключа, блоки
    return ABC


def is_sqrt(x):
    """Проверяет, является ли число х квадратом целого числа"""
    return sqrt(x)**2 == x


def check_input(text):
    """Проверяет text на наличие неизвестных сиволов"""
    for i in text.upper():
        if i not in alphabet().keys():
            return False
    return True


def read_message(title='Insert message: '):
    """
    считывает, проверяет и возвращает сообщение/шифр введённое пользователем
    """
    message = ''
    while not message:
        message = input(colored(title, 'blue', attrs=['bold'])).upper()
        if not message:
            print("The message cannot be empty! Try again.")
        elif not check_input(message):
            print(colored("Unknown characters were entered. Try again.", 'red', attrs=['bold']))
            message = ''
    return message


def read_key():
    """
    считывает, проверяет и возвращает ключ введённый пользователем
    """
    key = ''
    while not key:
        key = input(colored("Insert key: ", 'blue', attrs=['bold'])).upper()
        if not key or key == ' ':
            print("The key cannot be empty! Try again.")
        elif not check_input(key):
            print(colored("Unknown characters were entered. Try again.", 'red', attrs=['bold']))
            key = ''
        if not is_sqrt(len(key)):
            print(colored("The key must be an integer square. Try again.", 'red', attrs=['bold']))
            key = ''
    return key


def key_matrix(key):
    """
    Преобразует ключ в матрицу
    """
    letters, matrix = [], []
    sq = int(sqrt(len(key)))

    for i in range(0, len(key), sq):
        letters.append(list(key[i:i+sq]))

    for x in letters:
        arr = []
        for y in x:
            arr.append(alphabet()[y])
        matrix.append(arr)

    return matrix


def message_matrix(message, key):
    """
    Преобразует сообщение в матрицу
    """
    sq = int(sqrt(len(key)))
    while len(message) % sq > 0:
        message += '@'

    letters = list(message)
    matrix = []

    for x in range(0, len(letters), sq):
        abc = alphabet()
        arr = []
        for i in range(sq):
            arr.append(abc[letters[x+i]])
        matrix.append(arr)

    return matrix


def check_def(key_matrix):
    """
    Проверяет знак определителя матрицы ключа
    """
    det = abs(np.linalg.det(key_matrix))
    if det == 1:
        return True
    else:
        return False


def encryption(message, key):
    """Шифрует и возвращает сообщение"""
    m_matrix = message_matrix(message, key)
    k_matrix = key_matrix(key)

    if not check_def(k_matrix):
        print(colored("Данная комбинация ключ|сообщение не позваолит дешифровать сообщение", 'red', attrs=['bold']))
        sys.exit(1)

    abc = alphabet()
    result = []
    cipher = ''

    for i in m_matrix:
        result.append(list(np.array(i).dot(k_matrix) % len(abc)))

    for line in result:
        for num in line:
            for letter in abc.keys():
                if abc[letter] == num:
                    cipher += letter

    return cipher


def decryption(cipher, key):
    """Дешифрует и возвращает сообщение"""
    c_matrix = message_matrix(cipher, key)
    k_matrix = key_matrix(key)

    back_matrix = np.linalg.inv(k_matrix)
    abc = alphabet()
    result = []
    message = ''

    for i in c_matrix:
        result.append(list(np.array(i).dot(back_matrix) % len(abc)))

    for line in result:
        for num in line:
            for letter in abc.keys():
                if abc[letter] == round(num, 0):
                    message += letter

    message = message.replace('@', '')
    return message


def menu():
    """Начальное меню"""
    answer = 0

    while answer == 0:
        try:
            answer = int(input(colored("Insert\n[1] - to encryption"
                                       "\n[2] - to decryption\nYour choice: ", "blue", attrs=['bold'])))
            if answer != 1 and answer != 2:
                raise ValueError
        except ValueError:
            print(colored("Incorrect input!", "red", attrs=['bold']))
            answer = 0

    key = read_key()

    if answer == 1:
        message = read_message()
        code = encryption(message, key)
        print(colored("Cipher: ", 'blue', attrs=['bold'])+"\t\t"+colored(code, 'magenta', attrs=['bold']))
    elif answer == 2:
        message = read_message("Insert cipher:  ")
        code = decryption(message, key)
        print(colored("Message: ", 'blue', attrs=['bold']) + "\t\t" + colored(code, 'magenta', attrs=['bold']))


if __name__ == '__main__':
    sys.exit(menu())

"""
Создаеся алфавит, в котором число сиволов будет простым (делится только на 1 и на себя)
Создается ключ - его длинна должная быть равна квадрату целого числа (1,4,9,16,25 и тд)
                  это нужно для того, чтобы сделать из него квадратную матрицу
Сообщение также разбивается на блоки, равные по длине корню из длинны ключа;
                если символов не хватает, то сообщение дополняется символами @;
Символы в матрице-ключе и матрице-сообщении заменяются на их цифровые эквиваленты в кодированном алфавите

Шифрование:
1) Производится матричное умножение каждого блока сообщения на матрицу ключа (np.array(a).dot(b))
2) Определитель матрицы ключа должен быть отличным от нуля, ина дешифровка будет недоступна 
3) Далее получившиеся блоки делятся по модулю на длинную алфавита (29)
4) Декодируем получившуюся матрицу по кодированному алфавиту

Дешифрование:
1) Шифротекст/ключ кодируется в цифры и разбивается на блоки
2) Находится определитель матрицы ключа (np.linalg.det(key_matrix))
3) Находим обратную матрицу - должна быть
"""
