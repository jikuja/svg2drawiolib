# Copyright (c) 2024 Janne Kujanpää

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import sys

from lib import convert

DEFAULT_STYLE='shape=image;verticalLabelPosition=bottom;verticalAlign=top;imageAspect=0;aspect=fixed'

def _setup_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', help='mode', default='xml', choices=['data', 'xml'])
    parser.add_argument('--outfile', help='filename to output', default='output.xml')
    parser.add_argument('--style', help='style to use', default=DEFAULT_STYLE)
    parser.add_argument('--width', default=40)
    parser.add_argument('--height', default=40)
    parser.add_argument('--prefix', default='')
    parser.add_argument('--dirtitle', default=False, action='store_true')
    parser.add_argument('input', help='input files (iglob and/or directories)', nargs='*')
    args = parser.parse_args()

    if not args.input:
        print('Input files required')
        parser.print_usage()
        sys.exit(1)

    return args

def _main(args):
    mode = args.mode
    outfile = args.outfile
    input_files = args.input
    prefix = args.prefix
    h = args.height
    w = args.width
    style = args.style
    dirtitle= args.dirtitle

    output_str = convert(input_files=input_files, mode=mode, prefix=prefix, dirtitle=dirtitle,
                         style=style, h=h, w=w)
    with open(outfile, 'w', encoding='utf-8') as text_file:
        text_file.write(output_str)

if __name__ == '__main__':
    _main(_setup_argparse())
