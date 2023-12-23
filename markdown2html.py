#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:
   First argument is the name of the Markdown file.
   Second argument is the output file name
'''

import sys
import os.path
import markdown

if __name__ == '__main__':

    def create_markdown():
        """ Function that checks if an error exists, if not print nothing."""

        ''' Check if the script is correctly launch '''
        if len(sys.argv) < 3:
            error = "Usage: ./markdown2html.py README.md README.html"
            print(error, file=sys.stderr)
            exit(1)

        ''' Check if first arg exist '''
        if not os.path.isfile(sys.argv[1]):
            print(f"Missing {sys.argv[1]}", file=sys.stderr)
            exit(1)

        # Read the content of the Markdown file and convert it to HTML
        with open(sys.argv[1], 'r') as f:
            text = f.read()
            html = markdown.markdown(text)

        # Write the HTML content to the specified output file
        with open(sys.argv[2], 'w') as nf:
            nf.write(html)

        exit(0)

    create_markdown()
