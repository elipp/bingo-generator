from argparse import ArgumentParser
from pathlib import Path
from random import shuffle
import random
import logging
import os

import itertools

def partition(pred, iterable):
    'Use a predicate to partition entries into false entries and true entries'
    t1, t2 = itertools.tee(iterable)
    return list(itertools.filterfalse(pred, t1)), list(filter(pred, t2))


logger = logging.getLogger('bingo')

logging.basicConfig(
    level=os.environ.get('LOG_LEVEL', 'INFO').upper()
)

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

parser.add_argument(
    "--minimum-dares",
    type=int,
    default=5,
    help='Minimum number of "dare"s to include per sheet',
)

parser.add_argument(
    "--maximum-dares",
    type=int,
    default=12,
    help='Maximum number of "dare"s to include per sheet',
)

args = parser.parse_args()

with open(args.bingo_texts, "r", encoding="utf-8") as f:
    texts = [l.strip() for l in f.readlines() if l.strip()]
    observations, dares = partition(lambda t: t.startswith('🧩'), texts)
    logger.debug('observations: %s', observations)
    logger.debug('dares: %s', dares)


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
    shuffle(observations)
    shuffle(dares)
    text_rows = observations[:25]
    num_dares = random.randint(args.minimum_dares, args.maximum_dares)
    for (r, idx) in enumerate(random.sample(range(25), min(len(dares), num_dares))):
        logger.debug(f'replaced `{text_rows[idx]}` with `{dares[r]}`')
        text_rows[idx] = dares[r]
    
    content = (f'[{s}]' for s in text_rows)
    output = typst_table.format(CELL_CONTENT=",\n".join(content))
    with open(Path(args.output_folder)/f'{args.bingo_texts}-page{i:03}.typst', 'w') as f:
        f.write(base_template)
        f.write('\n')
        f.write(output)
