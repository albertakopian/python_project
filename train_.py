def train_encode(file):
    alphabet_size = 26
    string = []
    uppercase = [0] * alphabet_size
    lowercase = [0] * alphabet_size
    uppernumber = 0
    lowernumber = 0

    for elem in file:
        if 'A' <= elem <= 'Z':
            uppernumber += 1
            uppercase[ord(elem) - ord('A')] += 1
        elif 'a' <= elem <= 'z':
            lowernumber += 1
            lowercase[ord(elem) - ord('a')] += 1

    if uppernumber != 0:
        for elem in uppercase:
            string.append(str(elem / uppernumber) + ' ')

    string.append('\n')

    if lowernumber != 0:
        for elem in lowercase:
            string.append(str(elem / lowernumber) + ' ')
    return ''.join(string)
