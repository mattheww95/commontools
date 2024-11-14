"""
Concatamerize a multi fasta file into a single alignment

Matthew Wells: 2024-07-30
"""
import io
import sys
from typing import Optional



def fasta_parse(infile: io.StringIO) -> tuple[list[str], list[str]]:
    """
    Convert a fasta file into two lists of headers and sequences that can be written out.

    This function is adapted from what is presented here: https://rosettacode.org/wiki/FASTA_format#Python

    infile io.StringIO: input data from file
    """
    key = ''
    headers: list[str] = []
    sequences: list[str] = []

    for line in infile:
        if line.startswith('>'):
            if key:
                headers.append(key) 
                sequences.append(val)
            key, val = line[1:].rstrip().split()[0], ''
        elif key:
            val += line.rstrip()
    if key:
        headers.append(key)
        sequences.append(val)

    return (headers, sequences)



def write_sequences(data: tuple[list[str], list[str]], linker_sequence: str = '') -> None:
    """
    Write concatenated seqeunces to stdout

    data: output of fasta parse, position 0 are the headers, and position 1 are the sequences
    linker_sequence: optional string to inserte between sequence 
    """

    headers_joined: str = "_".join(data[0])
    sequences_joined: str = linker_sequence.join(data[1])
    sys.stdout.write(">{}\n".format(headers_joined))
    sys.stdout.write("{}\n".format(sequences_joined))
