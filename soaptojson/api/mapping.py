//mapping logic

import re
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
    
        
print(our_keys)
