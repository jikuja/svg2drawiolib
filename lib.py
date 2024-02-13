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

import base64
import glob
import json
import os
import zlib

def _find_files(x):
    if os.path.exists(x) and os.path.isdir(x):
        return glob.iglob(x + '/**/*.svg', recursive=True)
    else:
        return glob.iglob(x, recursive=True)

def convert(input_files, mode, prefix, dirtitle, style, h, w):
    result = []
    filenames = [_find_files(i) for i in input_files]
    for filename_iter in filenames:
        for filename in filename_iter:
            if mode == 'data':
                shape = create_data_shape(filename,
                                          prefix=prefix, use_directory_on_title=dirtitle,
                                          w=w, h=h)
            elif mode == 'xml':
                shape = create_xml_shape(filename, style=style,
                                         prefix=prefix, use_directory_on_title=dirtitle,
                                         w=w, h=h)
            result.append(shape)

    output_str = '<mxlibrary>' + json.dumps(result) + '</mxlibrary>'
    return output_str

def create_data_shape(filename, 
                      prefix='', use_directory_on_title=False, w=40, h=40):
    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("ascii")
        title = prefix + (filename if use_directory_on_title else os.path.basename(filename))
        print(f'Converting {filename} with title {title}')
        shape = {
            "data": "data:image/svg+xml;base64," + encoded_string,
            "w": w,
            "h": h,
            "title": prefix + title
        }
        return shape

def create_xml_shape(filename, style='shape=image;verticalLabelPosition=bottom;verticalAlign=top;imageAspect=0;aspect=fixed', 
                     prefix='', use_directory_on_title=False, w=40, h=40):
    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("ascii")
        image = encoded_string
        style_prop_value = f"{style};image=data:image/svg+xml," + image
        raw_xml = '<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="2" value="" style="' + style_prop_value + '" vertex="1" parent="1"><mxGeometry width="40" height="40" as="geometry"/></mxCell></root></mxGraphModel>'
        compressed_xml = zlib.compress(raw_xml.encode(), wbits=-15)
        encoded_xml = base64.b64encode(compressed_xml).decode("ascii")
        title = prefix + (filename if use_directory_on_title else os.path.basename(filename))
        print(f'Converting {filename} with title {title}')
        shape = {
            "xml": encoded_xml,
            "w": w,
            "h": h,
            "title": title
        }
        return shape
