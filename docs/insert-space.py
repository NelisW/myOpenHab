"""Markdown requires spaces after heading #, so insert space where required.
If # is followed by anything other than a whitespace or a #, inset a space
"""

import pyradi.ryfiles as ryfiles
import re

filenames = ryfiles.listFiles('.','*.md', 0,0)

# print(filenames)

for filename in filenames:
    print(filename)
    # if '000-contents.md' in filename:
    linesOut = []
    with open(filename, 'rt') as f:
        lines = f.readlines()
        for line in lines:
            line = re.sub(r'(#+)([^\s#])', r'\1 \2', line)
            linesOut.append(line)
    with open(filename, 'wt') as f:
        f.writelines(linesOut)
