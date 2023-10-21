# Bingo Generator
... for weddings and such.

Generates random bingo sheets as MS Word documents from a template file and a list of bingo texts.

## User notes

Editing bingo templates and printing the resulting sheets requires MS Word. Don't bother with Google Docs or anything else because the conversion will break something in the sheets.

Feel free to edit anything but the table in the template sheet to your liking. Editing the table will likely result in cataclysmic errors.

Bingo text formatting (hyphenation etc.) should be done beforehand on source text level because this program isn't smart enough to do that for you.

## Requirements

Requires python >= 3.7

Script requires the `python-docx` package, install with:
`pip install python-docx`

## Usage

Run script with defaults:
`python create_bingo_sheets.py`

```
usage: create_bingo_sheets.py [-h] [-t TEMPLATE] [-n NUM_SHEETS] [-b BINGO_TEXTS] [-o OUTPUT_FOLDER]

Generate random bingo sheets from a list of bingo texts.

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE, --template TEMPLATE
                        File containing a bingo sheet template.
  -n NUM_SHEETS, --number-of-sheets NUM_SHEETS
                        Number of bingo sheets to generate.
  -b BINGO_TEXTS, --bingo-texts BINGO_TEXTS
                        Text file containing bingo table texts.
  -o OUTPUT_FOLDER, --output-folder OUTPUT_FOLDER
                        Output folder for bingo sheets.
```