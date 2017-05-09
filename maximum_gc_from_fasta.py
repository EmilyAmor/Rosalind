#!/usr/bin/env python

import click

@click.command()
@click.argument('fastafile')

def gc_content(fastafile):
    """From a fasta file, returns the ID of a sequence that has the highest GC content (as well as
    the GC percent - rounded to 6 decimal figures)"""
    #import file
    input = open(fastafile)
    file = input.readlines()
    # remove end of line characters
    new_list = []
    for line in file:
        new_list.append(line.replace('\n', ''))
    appended_list = []
    # make tuple/dictionary of information
    appended_list = []
    my_tuple = {}
    key_list = []
    value = ''
    for line in new_list:
        if line.startswith('>'):
            my_tuple[line.strip('>')] = 0
            key_list.append(line.strip('>'))
            key = line.strip('>')
            appended_list = line.strip('>')
            value = ""
        else:
            value += line.strip('>')
            my_tuple[key] = value
    # calculate gc content
    index = 0
    gc_percent = dict()
    for i in key_list:
        gene_name = key_list[index]
        index += 1
        sequence = my_tuple[gene_name]
        g = sequence.count('G')
        c = sequence.count('C')
        total = len(value)
        gc_content = ((g + c)/total) * 100
        gc_percent[gene_name] = round(gc_content, 6)
    #return gene with biggest gc percent
    maximum = max(gc_percent, key=gc_percent.get)  # Just use 'min' instead of 'max' for minimum.
    print (maximum)
    print(gc_percent[maximum])

if __name__ == '__main__':
    gc_content()
