#!/usr/bin/python3
'''
markdown2html.py - Convert Markdown to HTML

This script takes a Markdown file as input and generates an HTML file as output

Usage:
  ./markdown2html.py [input_file] [output_file]
'''

import sys
import os.path

# Assign command line arguments to variables
input_file = sys.argv[1]
output_file = sys.argv[2]

def create_markdown():
    """
    Function that checks if an error exists, if not print nothing.
    """

    if len(sys.argv) < 2:
        error = "Usage: ./markdown2html.py README.md README.html"
        print(error, file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f"Missing {input_file}")
        exit(1)

    print()
    exit(0)

if __name__ == "__main__":
    create_markdown()
