import module

input_string = input("Enter string separated by spaces: ")
list_input_string = input_string.split()

list_length1 = module.get_string_lengths(list_input_string)
print("Length list 1:\n", list_length1)

read_lines = module.read_file()

print("Strings 2:\n", read_lines)
list_length2 = module.get_string_lengths(read_lines)
print("Length list 2:\n", list_length2)

module.write_list_to_file(list_length2)
