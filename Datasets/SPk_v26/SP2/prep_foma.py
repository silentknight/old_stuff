#!/usr/bin/env python
# coding=utf-8

import os
import sys
import zipfile

from io import open

if os.path.exists('train.txt'):
    print('Tokenized SP already exists - skipping processing')
    sys.exit()

data = open('Data', 'r', encoding='utf-8').read()
data = data[0:20000000]

print('Length of text8: {}'.format(len(data)))

num_test_chars = 1000000

train_data = data[: -2 * num_test_chars]
valid_data = data[-2 * num_test_chars: -num_test_chars]
test_data = data[-num_test_chars:]

for fn, part in [('train.txt', train_data), ('valid.txt', valid_data), ('test.txt', test_data)]:
    print('{} will have {} bytes'.format(fn, len(part)))
    print('- Tokenizing...')
    # Change space ' ' to underscore '_'
    part_str = ' '.join(['_' if c == ' ' else c for c in part.strip()])
    print('- Writing...')
    f = open(fn, 'w').write(part_str)
    f = open(fn + '.raw', 'w', encoding='utf-8').write(part)
