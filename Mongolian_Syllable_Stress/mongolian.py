import os
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

vowels = ['a', 'e', 'i', 'o', 'u', 'ø', 'y']


def load_data(path, separator):
    file = open(path, encoding='utf-8')
    longest = 0
    lines = list()
    for line in file:
        line = line.strip().strip('\ufeff').split(separator)[0]
        lines.append(line)
        syl_length = len(line.split('.'))
        longest = longest if longest > syl_length else syl_length
    file.close()

    inputs = list()
    outputs = list()
    for line in lines:
        inputs.append(create_input(line, longest))
        outputs.append(create_output(line, longest))

    return inputs, outputs, longest


def create_input(line, longest):
    input_data = list()
    syllables = line.split('.')
    for syllable in syllables:
        if is_long_vowel(syllable):
            input_data.append(1.0)
        else:
            input_data.append(0.0)

    for i in range(longest - len(syllables)):
        input_data.append(0.0)

    return input_data


def create_output(line, longest):
    output_data = list()
    syllables = line.split('.')
    for syllable in syllables:
        if '\'' in syllable:
            output_data.append(1.0)
        else:
            output_data.append(0.0)
    for i in range(longest - len(syllables)):
        output_data.append(0.0)

    return output_data


def is_long_vowel(syllable):
    vowel_num = 0
    for letter in syllable:
        if letter in vowels:
            if vowel_num == 0:
                vowel_1 = letter
                vowel_num += 1
            elif letter == vowel_1:
                return True
    return False


path = os.path.join(os.getcwd(), 'traing_data.txt')
inputs, outputs, longest = load_data(path, '\t')

print(inputs)
print(outputs)
