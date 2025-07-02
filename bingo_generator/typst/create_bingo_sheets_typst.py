from argparse import ArgumentParser
from pathlib import Path
from random import shuffle


parser = ArgumentParser(
    description="Generate random bingo sheets from a list of bingo texts."
)

parser.add_argument(
    "-t",
    "--template",
    default="template.typst",
    help="A file containing a bingo sheet template.",
)

parser.add_argument(
    "-n",
    "--number-of-sheets",
    dest="num_sheets",
    type=int,
    default="50",
    help="Number of bingo sheets to generate.",
)

parser.add_argument(
    "-b",
    "--bingo-texts",
    default="bingo_texts.txt",
    help="Text file containing bingo table texts.",
)

parser.add_argument(
    "-o",
    "--output-folder",
    default="./output",
    help="Output folder for bingo sheets."
)

args = parser.parse_args()

with open(args.bingo_texts, "r", encoding="utf-8") as f:
    texts = [l.strip() for l in f.readlines() if l.strip()]

Path(args.output_folder).mkdir(parents=True, exist_ok=True)

typst_table = '''
#table(
columns: (1fr, 1fr, 1fr, 1fr, 1fr),
rows: (3.15cm, 3.15cm, 3.15cm, 3.15cm, 3.15cm),
inset: 10pt,
align: horizon,
{CELL_CONTENT}
)
'''

with open(Path(args.template), 'r') as f:
    base_template = f.read()

for i in range(args.num_sheets):
    shuffle(texts)
    text_rows = [texts[j : j + 5] for j in range(0, 25, 5)]
    content = (f'[{i.strip()}]' for s in text_rows for i in s)
    output = typst_table.format(CELL_CONTENT=",\n".join(content))
    with open(Path(args.output_folder)/f'{args.bingo_texts}-page{i:03}.typst', 'w') as f:
        f.write(base_template)
        f.write('\n')
        f.write(output)
