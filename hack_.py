import decode_and_encode
import config


def hack(file, l):
    bar_chart = list(map(float, l.split()))
    considered_bar_chart = [0] * config.alphabet_size
    number_of_letters = 0

    for elem in file:
        if elem.isalpha():
            number_of_letters += 1
            considered_bar_chart[ord(elem.capitalize()) - ord('A')] += 1

    for shift in range(config.alphabet_size):
        difference = 0
        if number_of_letters != 0:
            for i in range(config.alphabet_size):
                difference += abs(bar_chart[i] - considered_bar_chart[i] / number_of_letters)
        tmp = considered_bar_chart[0]
        del considered_bar_chart[0]
        considered_bar_chart.append(tmp)

        if shift == 0 or mindifference > difference:
            key = shift
            mindifference = difference

    return decode_and_encode.caesar_decode(key, file)
