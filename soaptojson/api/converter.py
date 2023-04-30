import xml.etree.ElementTree as ET
import json
import re
def stringtoxml(xmldata):
    root = ET.fromstring(xmldata)
    
    return root
root=stringtoxml("<root><element1>value1</element1><element2>value2</element2></root>")
print(root.tag)
xml_data = dict()
for child in root:
    xml_data[child.tag] = child.text
print(xml_data)

def stringtojson(jsondata):
    jsondata=json.loads(jsondata)
    return jsondata
jsondata=stringtojson('{"name":"John", "age":30, "city":"New York"}')
print(type(jsondata))
for x, y in jsondata.items():
  print(x, y)



        



'''
def stringtosoap(soapdata):
    # Define the SOAP envelope
    envelope = ET.Element('soapenv:Envelope', {'xmlns:soapenv': 'http://schemas.xmlsoap.org/soap/envelope/', 'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'})
    body = ET.SubElement(envelope, 'soapenv:Body')

    # Define the SOAP body content with dynamic parameters
    content = """
    <ns:MyRequest xmlns:ns="http://example.com/namespace">
        <ns:param1>{param1_value}</ns:param1>
        <ns:param2>{param2_value}</ns:param2>
    </ns:MyRequest>
    """
    formatted_content = content.format(param1_value='value1', param2_value='value2')

    # Add the formatted content to the body
    body_content = ET.fromstring(formatted_content)
    body.append(body_content)

    # Return the XML as a string    
    xml_String = ET.tostring(envelope, encoding='utf8', method='xml')
    return xml_String

print(stringtosoap('{"name":"John", "age":30, "city":"New York"}'))
'''


