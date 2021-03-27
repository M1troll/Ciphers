import sys
from random import choice
from termcolor import colored


def alphabet():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '-', '!', '?']


def read_string():
    s = ''

    while not s:
        s = input("Enter a message: ")
        if not s:
            print("The string cannot be empty!")

    return s


def create_box():
    box = [([choice(alphabet()) for x in range(8)]) for y in range(8)]
    return box


def key_card():
    card = [[0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1, 1, 1, 0],
            [1, 1, 1, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 1]]
    return card


def rotate_90(data, times=1):
    rot_data = []

    for t in range(times):
        m = len(data)
        n = len(data[0])
        rev_data = data[::-1]
        rot_data = [[rev_data[j][i] for j in range(m)] for i in range(n)]
        data = rot_data

    return rot_data


def insert_message(message, box):
    message += '✸'
    card = key_card()
    i, r, completed = 0, 0, False

    while not completed:
        for x in range(8):
            if i >= len(message):
                completed = True
                break

            for y in range(8):
                if card[x][y] == 0:
                    box[x][y] = message[i]
                    i += 1
                    if i == len(message):
                        completed = True
                        break

        if not completed:
            r += 1
            if r == 4:
                break
            card = rotate_90(card)

    return box


def extract_message(box):
    message = ''
    completed = False
    card = key_card()

    for j in range(4):
        for x in range(8):
            if completed:
                break

            for y in range(8):
                if card[x][y] == 0:
                    if box[x][y] == '✸':
                        completed = True
                        break
                    message += box[x][y]

        if completed:
            break
        card = rotate_90(card)

    return message


def start():
    message = read_string()
    box = create_box()
    card = key_card()

    print(colored("Create Matrix...", 'yellow', attrs=['bold']) + "\t\t\t\t\t\t\t"
          + colored("Create Grid... ", 'yellow', attrs=['bold']))
    for b, c in zip(box, card):
        print(colored(b, 'red') + "\t" + colored(c, 'cyan', attrs=['bold']))
    print(colored("Insert message in Matrix...", 'yellow', attrs=['bold'])+"\t\t\t\t\t"
          + colored("Grid-matrix: ", 'yellow', attrs=['bold']))
    for m, g in zip(insert_message(message, box), card):
        print(colored(m, 'green')+"\t"+colored(g, 'cyan', attrs=['bold']))
    print(colored("Extract message from Matrix...", 'yellow', attrs=['bold'])+f"\n{extract_message(box)}")


if __name__ == '__main__':
    sys.exit(start())
