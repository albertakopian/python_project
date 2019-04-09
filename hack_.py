import decode_and_encode


def hack(file, l1, l2):
    alphabet_size = 26
    upper_bar_chart = list(map(float, l1.split()))
    lower_bar_chart = list(map(float, l2.split()))
    string = []
    for shift in range(26):

        uppercase = [0] * alphabet_size
        lowercase = [0] * alphabet_size
        uppernumber = 0
        lowernumber = 0

        for elem in file:
            if 'A' <= elem <= 'Z':
                uppernumber += 1
                uppercase[(ord(elem) - ord('A') + alphabet_size - shift) % alphabet_size] += 1
            elif 'a' <= elem <= 'z':
                lowernumber += 1
                lowercase[(ord(elem) - ord('a') + alphabet_size - shift) % alphabet_size] += 1

        difference = 0
        if uppernumber != 0:
            for i in range(alphabet_size):
                difference += abs(upper_bar_chart[i] - uppercase[i] / uppernumber)
        else:
            for i in range(alphabet_size):
                difference += upper_bar_chart[i]
        if lowernumber != 0:
            for i in range(alphabet_size):
                difference += abs(lower_bar_chart[i] - lowercase[i] / lowernumber)
        else:
            for i in range(alphabet_size):
                difference += lower_bar_chart[i]

        if shift == 0 or mindifference > difference:
            key = shift
            mindifference = difference

    return decode_and_encode.caesar_decode(key, file)
