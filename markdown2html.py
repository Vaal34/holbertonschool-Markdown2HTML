#!/usr/bin/python3

import sys
import os.path

input_file = sys.argv[1]
output_file = sys.argv[2]

def create_markdown():
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f"Missing {input_file}")
        exit(1)

    print()
    exit(0)

create_markdown()
