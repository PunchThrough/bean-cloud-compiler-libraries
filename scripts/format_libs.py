import os

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
LIBS_CSV = os.path.join(THIS_DIR, 'libs-prod.csv')
MARKDOWN_OUT = os.path.join(THIS_DIR, '..', 'platformio-libraries.md')

with open(LIBS_CSV, 'rb') as f:
    lines = f.readlines()

with open(MARKDOWN_OUT, 'wb') as f:

    # Write header
    header = '|PlatformIO ID|Name|Description|'
    f.write("{}\n".format(header))
    f.write("|-----|------|-------|\n")

    # Write lines
    for l in lines:
        stripped = l.strip('\r\n')
        cols = stripped.split(',', 2)
        f.write('|{}|{}|{}|\n'.format(cols[0], cols[1], cols[2]))
