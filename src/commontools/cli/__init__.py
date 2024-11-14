# SPDX-FileCopyrightText: 2024-present Matthew Wells <mattwells9@shaw.ca>
#
# SPDX-License-Identifier: MIT
import click
import commontools.cli.concatemerize as cat
from commontools.__about__ import __version__





@click.command(short_help="Concatemerize a multifasta file, displays output to stdout. So make sure to capture it!", no_args_is_help=True)
@click.option("-i", "--input", "input_file", type=click.Path(), help="A multifasta file to concatemerize. Only plain text is supported currently.")
@click.option("-l", "--linker-sequence", "linker", type=str, default="", help="An optional linker sequence to place in-between merged sequences.")
def concat(input_file, linker):
    """
    Concatemerize a set of sequences
    """
    parsed_fasta: tuple[list[str], list[str]]
    with open(input_file, 'r') as seq_in:
        parsed_fasta = cat.fasta_parse(seq_in)
    cat.write_sequences(parsed_fasta, linker)


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True, no_args_is_help=True)
@click.version_option(version=__version__, prog_name="CommonTools")
def commontools():
    pass


commontools.add_command(concat)

def main():
    return commontools()