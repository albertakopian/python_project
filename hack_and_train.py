import decode_and_encode
import config


def fill_curr_bar_chart(file):
    number_of_letters = 0
    curr_bar_chart = [0] * config.alphabet_size
    for elem in file:
        if elem.isalpha():
            number_of_letters += 1
            curr_bar_chart[ord(elem.capitalize()) - ord('A')] += 1
    return number_of_letters, curr_bar_chart


def train_encode(file):
    string = []
    number_of_letters, bar_chart = fill_curr_bar_chart(file)

    if number_of_letters != 0:
        for elem in bar_chart:
            string.append(str(elem / number_of_letters) + ' ')

    return ''.join(string)


def hack(file, l):
    bar_chart = list(map(float, l.split()))
    number_of_letters, considered_bar_chart = fill_curr_bar_chart(file)
    key = 0

    if number_of_letters != 0:
        for shift in range(config.alphabet_size):
            difference = 0

            for i in range(config.alphabet_size):
                    difference += abs(bar_chart[i] - considered_bar_chart[(i + shift) % config.alphabet_size] / number_of_letters)

            if shift == 0 or mindifference > difference:
                key = shift
                mindifference = difference

    return decode_and_encode.caesar_decode(key, file)
