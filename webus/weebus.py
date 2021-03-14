#!/usr/bin/python3
import pandas as pd
import subprocess
import argparse


def load_spreadsheet(filename):
    try:
        df = pd.read_excel(filename, dtype={
            'id': str,
            'style': str,
            'text': str,
            'trace': str,
        }, usecols=range(4))
    except FileNotFoundError:
        print(f'Unable to load {filename}')
        exit()

    df = df.fillna('')
    return df


def generate_md(df, filename):
    with open(filename, 'w') as md:
        for i, item in df.iterrows():
            metadata = []
            if item.id:
                metadata.append('REQ-' + item.id)

            if item.trace:
                metadata.append('Trace: ' + item.trace)

            if len(metadata) > 0:
                metadata_str = ', '.join(metadata)
                md.write(f'<div custom-style="metadata">{metadata_str}</div>\n\n')

            md.write(item.text + '\n\n')


def generate_docx(input_filename, output_filename):
    subprocess.run(['pandoc', input_filename,
                    '--reference-doc', 'custom-reference.docx',
                    '-o', output_filename], check=True)


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
