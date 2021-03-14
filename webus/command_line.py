import argparse
import subprocess
from .weebus import load_spreadsheet, generate_md, generate_docx


def command_line():
    parser = argparse.ArgumentParser('webus')
    parser.add_argument('input')
    parser.add_argument('-g', '--generate', action='store_true')
    parser.add_argument('-s', '--show', action='store_true')
    args = parser.parse_args()

    df = load_spreadsheet(args.input)

    if args.generate:
        generate_md(df, 'output.md')
        generate_docx('output.md', 'output.docx')

        if args.show:
            subprocess.run(['libreoffice', 'output.docx'], check=True)
