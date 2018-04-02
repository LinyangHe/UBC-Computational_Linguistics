import os

present_suffixes = ['ó', 'ő']
future_suffixes = ['andó', 'endő']
front_vowels = ['ö', 'ő', 'ü', 'ű']
back_vowels = ['a', 'á', 'o', 'ó', 'u', 'ú']
neutral_vowels = ['e', 'é', 'i', 'í']


def open_file(path, separator):
    file = open(path, encoding='utf-8')
    words = []
    for line in file:
        line = line.strip().strip('\ufeff')
        if not line:
            continue
        line = line.split(separator)
        words.append(line[1])
    file.close()
    return words


def is_back_class(word):
    for letter in word:
        if letter in back_vowels:
            return True
    return False


def get_suffix(suffixes):
    for suffix in suffixes:
        if is_back_class(suffix):
            back_suffix = suffix
        else:
            front_suffix = suffix
    return back_suffix, front_suffix


read_path = os.path.join(os.getcwd(), 'Hungarian verb list.csv')
hungarian_wordlist = open_file(read_path, '\t')

file_present = open(os.path.join(os.getcwd(), 'present.csv'), encoding='utf-8', mode='w')
file_future = open(os.path.join(os.getcwd(), 'future.csv'), encoding='utf-8', mode='w')

present_back_suffix, present_front_suffix = get_suffix(present_suffixes)
future_back_suffix, future_front_suffix = get_suffix(future_suffixes)

for word in hungarian_wordlist:
    if is_back_class(word):
        file_present.write(word + ',' + word + present_back_suffix + '\n')
        file_future.write(word + ',' + word + future_back_suffix + '\n')
    else:
        file_present.write(word + ',' + word + present_front_suffix + '\n')
        file_future.write(word + ',' + word + future_front_suffix + '\n')

file_present.close()
file_future.close()
