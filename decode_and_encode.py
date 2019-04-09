def modify_char(elem, shift):
    alphabet_size = 26
    if 'a' <= elem <= 'z':
        return chr((ord(elem) - ord('a') + shift) % alphabet_size + ord('a'))
    elif 'A' <= elem <= 'Z':
        return chr((ord(elem) - ord('A') + shift) % alphabet_size + ord('A'))
    else:
        return elem


def multipurpose_caesar(key, file):
    string = []
    for elem in file:
        string.append(modify_char(elem, key))
    return ''.join(string)


def multipurpose_vigenere(key, file, flag):
    i = 0
    string = []
    for elem in file:
        if 'a' <= elem <= 'z' and 'a' <= key[i % len(key)] <= 'z':
            string.append(modify_char(elem, flag*(ord(key[i % len(key)]) - ord('a'))))
        elif 'A' <= elem <= 'Z' and 'A' <= key[i % len(key)] <= 'Z':
            string.append(modify_char(elem, flag*(ord(key[i % len(key)]) - ord('A'))))
        else:
            string.append(elem)
        i += 1
    return ''.join(string)


def caesar_encode(key, file):
    key = int(key)
    return multipurpose_caesar(key, file)


def caesar_decode(key, file):
    key = int(key)
    return multipurpose_caesar((-1)*key, file)


def vigenere_encode(key, file):
    return multipurpose_vigenere(key, file, 1)


def vigenere_decode(key, file):
    return multipurpose_vigenere(key, file, -1)
