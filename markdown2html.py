#!/usr/bin/python3
""" This file is made to parse some Markdown to HTML """

# Import necessary modules
import sys  # Import the sys module for command line arguments
import os.path  # Import the os.path module for file existence checking
import markdown  # Import the markdown module for Markdown to HTML conversion

"""
Test comment
Test comment
Test comment
"""

# Define the main function
def main():
    """
    Test comment
    Test comment
    Test comment
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
