#!/usr/bin/python3
# 2.print_alphabet.by
for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end='')
