import argparse
import subprocess
import os
import platform
from .weebus import load_spreadsheet, generate_md, generate_docx


def open_with_default_app(filename):
    if platform.system() == 'Darwin':
        subprocess.call(('open', filename))
    elif platform.system() == 'Windows':
        os.startfile(filename)
    else:
        subprocess.call(('xdg-open', filename))


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
            open_with_default_app('output.docx')
