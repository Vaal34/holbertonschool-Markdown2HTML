#!/usr/bin/python3
"""
markdown2html.py - Convert Markdown to HTML

This script takes a Markdown file as input and generates an HTML file as output.

Usage:
  ./markdown2html.py [input_file] [output_file]

Parameters:
  input_file (str): The path to the Markdown file to be converted.
  output_file (str): The path to the HTML file where the converted output will be saved.

Example:
  ./markdown2html.py README.md README.html

"""


import sys
import os.path

input_file = sys.argv[1]
output_file = sys.argv[2]


def create_markdown():
    """ focntion that check if an error exist if not print nothing """

    if len(sys.argv) < 2:
        error = "Usage: ./markdown2html.py README.md README.html"
        print(error, file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f"Missing {input_file}")
        exit(1)

    print()
    exit(0)


create_markdown()
