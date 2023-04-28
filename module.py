# func which return list lengths
from typing import List


def get_string_lengths(list_string):
    list_string_length = []
    for str in list_string:
        list_string_length.append(len(str))
    return list_string_length


# read data from file
def read_file():
    with open('strings.txt') as line:
        read_file = line.read().splitlines()
    return read_file


# write data to file
def write_list_to_file(list_length):
    with open(r'result.txt', 'w') as write_line:
        for item in list_length:
            write_line.write("%s\n" % item)
