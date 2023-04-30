import json
import xml.etree.ElementTree as ET
class JsonMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 201 and response['content-type'] == 'application/json':
            # Convert the JSON data to XML
            xml = json_to_xml_(response.content)
            # Pretty-print the XML output
            xml_string = ET.tostring(xml, encoding="unicode")
            print(xml_string)
                        

        return response

def json_to_xml_(json_data, parent=None):
        if isinstance(json_data, dict):
            if parent is not None:
                elem = ET.SubElement(parent, "dict")
            else:
                elem = ET.Element("dict")
            for key, value in json_data.items():
                child = ET.SubElement(elem, key)
                json_to_xml_(value, child) 
        elif isinstance(json_data, list):
            if parent is not None:
                elem = ET.SubElement(parent, "list")
            else:
                elem = ET.Element("list")
            for item in json_data:
                json_to_xml_(item, elem)
        else:
            if parent is not None:
                elem = ET.SubElement(parent, "str")
            else:
                elem = ET.Element("str")
            elem.text = str(json_data)
        return elem  

    