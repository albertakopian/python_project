import config


def train_encode(file):
    string = []
    bar_chart = [0] * config.alphabet_size

    number_of_letters = 0

    for elem in file:
        if elem.isalpha():
            number_of_letters += 1
            bar_chart[ord(elem.capitalize()) - ord('A')] += 1

    if number_of_letters != 0:
        for elem in bar_chart:
            string.append(str(elem / number_of_letters) + ' ')

    return ''.join(string)
