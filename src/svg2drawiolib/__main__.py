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
import logging
import sys

from svg2drawiolib import convert

DEFAULT_STYLE=('shape=image;'
               'verticalLabelPosition=bottom;'
               'align=center;verticalAlign=top;' # label alignment
               'imageAlign=center;imageVerticalAlign=middle;' # image alignment
               'imageAspect=1;aspect=fixed')

def _setup_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', help='mode', default='xml', choices=['data', 'xml'])
    parser.add_argument('--output', help='filename to output', default='output.xml')
    parser.add_argument('--style', help='mxCell style', default=DEFAULT_STYLE)
    parser.add_argument('--width', default=40)
    parser.add_argument('--height', default=40)
    parser.add_argument('--prefix', help='prefix to add on shape name' , default='')
    parser.add_argument('--dirtitle', help='Use full path on shape name', default=False, action='store_true')
    parser.add_argument("--log-level", help="Configure the logging level.", default=logging.INFO, type=lambda x: getattr(logging, x))
    parser.add_argument('input', help='input files (iglob and/or directories)', nargs='*')
    args = parser.parse_args()

    if not args.input:
        print('Input files required')
        parser.print_usage()
        sys.exit(1)

    return args

def main():
    args = _setup_argparse()
    logging.basicConfig(level=args.log_level)

    output_str = convert(input_files=args.input, mode=args.mode, 
                         prefix=args.prefix, dirtitle=args.dirtitle,
                         style=args.style, height=args.height, width=args.width)
    with open(args.output, 'w', encoding='utf-8') as text_file:
        text_file.write(output_str)

if __name__ == '__main__':
    main()
