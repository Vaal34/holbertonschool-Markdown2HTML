#!/usr/bin/python3
""" This file is made to parse some Markdown to HTML """

import sys
import os.path
import markdown


# Function to convert Markdown to HTML and save to a file
def main():
    """ Function that checks if an error exists,
    if not print nothing. Comment
    """

    # Check if the correct number of command line arguments is provided
    if len(sys.argv) < 3:
        error = "Usage: ./markdown2html.py README.md README.html"
        print(error, file=sys.stderr)
        exit(1)

    # Check if the input Markdown file exists
    if not os.path.isfile(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)

    # Read the input Markdown file and convert it to HTML
    with open(sys.argv[1], 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    # Write the HTML to the specified output file
    with open(sys.argv[2], 'w') as nf:
        nf.write(html)

    exit(0)


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
