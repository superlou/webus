import argparse
import subprocess
import os
import platform
from .webus import load_spreadsheet, generate_md, generate_docx, lint_records
from rich.console import Console


console = Console()
print = console.print


def open_with_default_app(filename):
    if platform.system() == 'Darwin':
        subprocess.call(('open', filename))
    elif platform.system() == 'Windows':
        os.startfile(filename)
    else:
        subprocess.call(('xdg-open', filename))


def print_requirement_stats(df):
    requirement_count = len(df[df.id != ''])
    print(f'Requirement count: {requirement_count}')

    try:
        next_id = int(df[df.id != ''].id.astype(int).max()) + 1
        print(f'Next available ID: {next_id}')
    except ValueError:
        pass


def print_linter_warnings(df):
    linter_warnings = lint_records(df)

    row_width = max([len(str(warning[0])) for warning in linter_warnings])

    if len(linter_warnings) > 0:
        for warning in linter_warnings:
            print(f'[red]{warning[0]:{row_width}} {warning[1]}')


def command_line():
    parser = argparse.ArgumentParser('webus')
    parser.add_argument('input')
    parser.add_argument('-g', '--generate', action='store_true')
    parser.add_argument('-s', '--show', action='store_true')
    args = parser.parse_args()

    df = load_spreadsheet(args.input)
    print_requirement_stats(df)
    print_linter_warnings(df)

    if args.generate:
        generate_md(df, 'output.md')
        generate_docx('output.md', 'output.docx')

        if args.show:
            open_with_default_app('output.docx')
