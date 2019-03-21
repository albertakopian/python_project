def code(chiper, key, file):
    string = []
    if chiper == 'caesar':
        key = int(key)
        for elem in file:
            if 'a' <= elem <= 'z':
                string.append(chr((ord(elem) - ord('a') + key) % 26 + ord('a')))
            elif 'A' <= elem <= 'Z':
                string.append(chr((ord(elem) - ord('A') + key) % 26 + ord('A')))
            else:
                string.append(elem)
        return ''.join(string)

    if chiper == 'vigenere':
        i = 0
        for elem in file:
            if 'a' <= elem <= 'z' and 'a' <= key[i % len(key)] <= 'z':
                string.append(chr((ord(elem) - ord('a') + ord(key[i % len(key)]) - ord('a')) % 26 + ord('a')))
            elif 'A' <= elem <= 'Z' and 'A' <= key[i % len(key)] <= 'Z':
                string.append(chr((ord(elem) - ord('A') + ord(key[i % len(key)]) - ord('A')) % 26 + ord('A')))
            else:
                string.append(elem)
            i += 1
        return ''.join(string)
