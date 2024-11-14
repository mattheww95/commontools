"""
Test of concatemerization functions of fastas
Matthew Wells: 2024-07-30
"""
import pytest
import io
from commontools.cli import concatemerize as cat



def test_fasta_parse():
    FASTA='''\
>Rosetta_Example_1
THERECANBENOSPACE
>Rosetta_Example_2
THERECANBESEVERAL
LINESBUTTHEYALLMUST
BECONCATENATED'''
    in_string = io.StringIO(FASTA)
    output = cat.fasta_parse(in_string)
    headers_expected = ["Rosetta_Example_1", "Rosetta_Example_2"]
    sequences_expected = ["THERECANBENOSPACE", 
                        "THERECANBESEVERALLINESBUTTHEYALLMUSTBECONCATENATED"]
    assert output[0] == headers_expected
    assert output[1] == sequences_expected