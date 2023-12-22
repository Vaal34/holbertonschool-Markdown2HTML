#!/usr/bin/python3
"""
comment
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
