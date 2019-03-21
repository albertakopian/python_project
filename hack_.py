def hack(file, l1, l2):
    upper_bar_chart = list(map(int, l1.split()))
    lower_bar_chart = list(map(int, l2.split()))
    string = []
    for shift in range(26):

        uppercase = [0] * 26
        lowercase = [0] * 26
        uppernumber = 0
        lowernumber = 0

        for elem in file:
            if 'A' <= elem <= 'Z':
                uppernumber += 1
                uppercase[(ord(elem) - ord('A') + 26 - shift) % 26] += 1
            elif 'a' <= elem <= 'z':
                lowernumber += 1
                lowercase[(ord(elem) - ord('a') + 26 - shift) % 26] += 1

        difference = 0
        if uppernumber != 0:
            for i in range(26):
                difference += abs(upper_bar_chart[i] - round((uppercase[i] / uppernumber) * 10000))
        else:
            for i in range(26):
                difference += upper_bar_chart[i]
        if lowernumber != 0:
            for i in range(26):
                difference += abs(lower_bar_chart[i] - round((lowercase[i] / lowernumber) * 10000))
        else:
            for i in range(26):
                difference += lower_bar_chart[i]

        if shift == 0 or mindifference > difference:
            key = shift
            mindifference = difference

    for elem in file:
        if 'a' <= elem <= 'z':
            string.append(chr((ord(elem) - ord('a') + 26 - key) % 26 + ord('a')))
        elif 'A' <= elem <= 'Z':
            string.append(chr((ord(elem) - ord('A') + 26 - key) % 26 + ord('A')))
        else:
            string.append(elem)
    return ''.join(string)
