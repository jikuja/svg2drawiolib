import base64
import os
import zlib


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
