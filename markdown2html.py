#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:
   First argument is the name of the Markdown file.
   Second argument is the output file name
'''

import sys
import os.path

if __name__ == '__main__':

    def create_markdown():
        """ Function that checks if an error exists, if not print nothing."""

        if len(sys.argv) < 3:
            error = "Usage: ./markdown2html.py README.md README.html"
            print(error, file=sys.stderr)
            exit(1)

        if not os.path.isfile(sys.argv[1]):
            print(f"Missing {sys.argv[1]}", file=sys.stderr)
            exit(1)

        print()
        exit(0)

    create_markdown()
