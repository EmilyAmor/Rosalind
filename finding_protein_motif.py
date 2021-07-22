#!/usr/bin/env python

import click

@click.command()
@click.argument('inputfilename')
@click.argument('outputfilename')

def finding_prot_motif(inputfilename, outputfilename):

    """Given: At most 15 UniProt Protein Database access IDs.Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found."""

    

    import requests
    import re

    output_file = open(outputfilename, "a")
    motif= re.compile(r"[N][^P][S|T][^P]")
    
    # get the UniProt accession ID from inputfile
    ids = []
    f = open(inputfilename, "r")
    for line in f:
        ids.append(line.strip())
        
    # Get the protein sequences from Uniprot
    prot_dic = {}
    for acc in ids:
        link = "https://www.uniprot.org/uniprot/{}.fasta".format(acc)
        response = requests.get(link)
        data = response.text
        protein_seq=""
        for line in data.split('\n')[:-1]:
            if line.startswith(">"):
                continue
            else:
                protein_seq = protein_seq + line
        prot_dic[acc]=protein_seq

        # Find the motif in each iterator
        l= []
        for i in range(len(protein_seq) +1):
            subseq=protein_seq[i:]
            m = motif.match(subseq)
            if m is not None:
                 l.append(i+1)

        # get rid of uniprot accessions that dont have any motifs
        if l == []:
            continue
        else:
            print (acc, file=output_file)
            print (str(l).replace("[","").replace("]","").replace(",",""), file=output_file)
    output_file.close()

if __name__ == '__main__':
    finding_prot_motif()
