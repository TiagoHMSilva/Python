alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def readint(message):
    """
    Function that receives a whole number data by the user and checks if a correct number was informed.
    :param message: Given that the user typed
    :return: Returns the number informed
    """
    while True:
        try:
            n = int(input(message))
        except (ValueError, TypeError):
            print('\033[31mERRO: Please enter a valid whole number.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mERRO: User preferred not to enter a number.\033[m')
            return 0
        else:
            return n


def readsrt(message):
    """
    Function that receives a text data by the user and checks if a correct number has been informed.
    :param message: Given that the user typed
    :return: Returns the number informed
    """
    while True:
        t = str(input(message)).upper()
        if t.isnumeric() or t == '':
            print('\033[31mERRO: Please enter valid text.\033[m')
        else:
            return t


def menu(roster):
    """
    Function that creates an interactive menu, containing the options of encrypting, decrypting and exiting.
    :param roster: Receive a list of interaction options that the user can choose
    :return: Returns the user's choice
    """
    print()
    print('_' * 30)
    print('{:^30}'.format("Cesar's Cipher"))
    print('_' * 30)
    c = 1
    for item in roster:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    choice = readint('\033[33mYou Choice: \033[m')
    return choice


def encrypt():
    """
    Function that takes a certain text and encrypts it using the logic of the cipher of cesar, where each letter
    of the text is replaced by another one, which is presented in the alphabet. Using a key to find out which letter
    to replace.
    :return: Returns nothing
    """
    print('_' * 30)
    txt = readsrt('\033[32mType your text: \033[m')
    key = readint('\033[33mKey: \033[m')

    textlist = list(txt)
    newtext = []
    cont = 0
    while cont < len(textlist):
        if textlist[cont] == ' ':
            newtext.append(' ')
        if textlist[cont] == ',':
            newtext.append(',')
        if textlist[cont] in alphabet:
            x = alphabet.index(textlist[cont]) + key
            if x > len(alphabet):
                x -= len(alphabet)
                newtext.append(alphabet[x])
            else:
                newtext.append(alphabet[x])
        cont += 1

    print(f'\033[33mOriginal text: \033[m{txt}\033[m')
    print(f'\033[33mEncrypted text: \033[m', end='')
    for l in newtext:
        print(l, end='')


def decrypt():
    """
    Function that takes a certain text and decrypts it using the cipher cipher logic, where each letter of the text
    is replaced by another letter, which is presented in the alphabet. Using a key to find out which letter to replace.
    :return: Returns nothing
    """
    print('_' * 30)
    txt = readsrt('\033[32mType your text: \033[m')
    key = readint('\033[33mKey: \033[m')

    textlist = list(txt)
    newtext = []
    cont = 0
    while cont < len(textlist):
        if textlist[cont] == ' ':
            newtext.append(' ')
        if textlist[cont] == ',':
            newtext.append(',')
        if textlist[cont] in alphabet:
            x = alphabet.index(textlist[cont]) - key
            if x > len(alphabet):
                x -= len(alphabet)
                newtext.append(alphabet[x])
            else:
                newtext.append(alphabet[x])
        cont += 1

    print(f'\033[33mOriginal text: \033[m{txt}\033[m')
    print(f'\033[33mEncrypted text: \033[m', end='')
    for l in newtext:
        print(l, end='')
