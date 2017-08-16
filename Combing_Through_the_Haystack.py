#!/usr/bin/env python

import click
@click.command()
@click.argument('n')



def find_substring_in_string(n):

    import re # use Regular Expressions module to identify "patterns"

    # reading in and preparing file into suitable format
    file = open(n).read().split('\n')
    substring = file[1]
    string = file[0]

    # preparing substring input
    motif = substring
    s = motif[0] + '(?=' + motif[1:] + ')'

    # using re module, identify all substrings in the string
    matches = re.finditer(s, string)

    positions = []
    for m in matches:
        pos =  1 + m.start() # plus one to count like humans not pythons :)
        positions.append(pos)

    print (positions)

if __name__ == '__main__':
    find_substring_in_string()
