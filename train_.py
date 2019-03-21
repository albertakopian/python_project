def train_encode(file):
    string = []
    uppercase = [0] * 26
    lowercase = [0] * 26
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
            string.append(str(round((elem / uppernumber) * 10000)) + ' ')

    string.append('\n')

    if lowernumber != 0:
        for elem in lowercase:
            string.append(str(round((elem / lowernumber) * 10000)) + ' ')
    return ''.join(string)
