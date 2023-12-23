#!/usr/bin/python3
"""
Test comment
Test comment
Test comment
"""

import sys
import os.path
import markdown
"""
Test comment
Test comment
Test comment
"""

def main():
    """
    Test comment
    Test comment
    Test comment
    """

    if len(sys.argv) < 3:
        error = "Usage: ./markdown2html.py README.md README.html"
        print(error, file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)

    with open(sys.argv[1], 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    with open(sys.argv[2], 'w') as nf:
        nf.write(html)

    exit(0)

if __name__ == "__main__":
    """
    Test comment
    Test comment
    Test comment
    """
    main()
