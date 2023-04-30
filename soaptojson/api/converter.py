#mapping logic
#jshon to xml
import re
import xml.etree.ElementTree as ET
jshon={"pid":10,"pname":"riya","oid":1}
keys=jshon.keys()
our_keys={}
for key in keys:
    if re.search("^o[a-z_]{0,7}[id|no|num|number]+$",key):
        our_keys['order_id']=jshon[key]
    elif re.search("^p[a-z_]{0,9}[name|n]$",key):
        our_keys['product_name']=jshon[key]    
    elif re.search("^p[a-z_]{0,9}[id|no|num|number]+$",key):
        our_keys['product_id']=jshon[key]
    
root = ET.Element('root')
for key, value in our_keys.items():
    child = ET.Element(key)
    if isinstance(value, dict):
        for k, v in value.items():
            sub_child = ET.Element(k)
            sub_child.text = str(v)
            child.append(sub_child)
    else:
        child.text = str(value)
    root.append(child)

xml_data = ET.tostring(root, encoding='unicode')

print(xml_data)
print(our_keys)
