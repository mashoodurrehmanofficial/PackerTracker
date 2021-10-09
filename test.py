data = [{'barcode': 'SRig10', 'total_jumps': '3'}, {'barcode': 'SRig1', 'total_jumps': '4'}, {'barcode': 'SRig4', 'total_jumps': '4'}, {'barcode': 'Srig5', 'total_jumps': '3'}, {'barcode': 'SRig14', 'total_jumps': '16'}, {'barcode': 'SRig13', 'total_jumps': '0'}, {'barcode': 'SRig10', 'total_jumps': '3'}, {'barcode': 'SRig1', 'total_jumps': '4'}, {'barcode': 'SRig4', 'total_jumps': '4'}, {'barcode': 'Srig5', 'total_jumps': '3'}, {'barcode': 'SRig14', 'total_jumps': '16'}, {'barcode': 'SRig13', 'total_jumps': '0'}, {'barcode': 'SRig10', 'total_jumps': '3'}, {'barcode': 'SRig10', 'total_jumps': '3'}, {'barcode': 'SRig10', 'total_jumps': '3'}, {'barcode': 'SRig1', 'total_jumps': '4'}, {'barcode': 'SRig4', 'total_jumps': '4'}, {'barcode': 'Srig5', 'total_jumps': '3'}, {'barcode': 'SRig14', 'total_jumps': '16'}, {'barcode': 'SRig13', 'total_jumps': '0'}, {'barcode': 'SRig10', 'total_jumps': '3'}, {'barcode': 'SRig1', 'total_jumps': '4'}, {'barcode': 'SRig4', 'total_jumps': '4'}, {'barcode': 'Srig5', 'total_jumps': '3'}, {'barcode': 'SRig14', 'total_jumps': '16'}, {'barcode': 'SRig13', 'total_jumps': '0'}, {'barcode': 'SRig10', 'total_jumps': '12'}, {'barcode': 'SRig1', 'total_jumps': '16'}, {'barcode': 'SRig4', 'total_jumps': '16'}, {'barcode': 'Srig5', 'total_jumps': '12'}, {'barcode': 'SRig14', 'total_jumps': '16'}, {'barcode': 'SRig13', 'total_jumps': '14'}, {'barcode': 'SRig10', 'total_jumps': '3'}, {'barcode': 'SRig1', 'total_jumps': '4'}, {'barcode': 'SRig4', 'total_jumps': '4'}, {'barcode': 'Srig5', 'total_jumps': '3'}, {'barcode': 'SRig14', 'total_jumps': '16'}, {'barcode': 'SRig13', 'total_jumps': '0'}, {'barcode': 'SRig10', 'total_jumps': '0'}, {'barcode': 'SRig1', 'total_jumps': '0'}, {'barcode': 'SRig4', 'total_jumps': '0'}, {'barcode': 'Srig5', 'total_jumps': '0'}, {'barcode': 'SRig14', 'total_jumps': 
'0'}, {'barcode': 'SRig13', 'total_jumps': '0'}, {'barcode': 'SRig10', 'total_jumps': '3'}, {'barcode': 'SRig1', 'total_jumps': '4'}, {'barcode': 'SRig4', 'total_jumps': '4'}, {'barcode': 'Srig5', 'total_jumps': '3'}, {'barcode': 'SRig14', 'total_jumps': '16'}, 
{'barcode': 'SRig13', 'total_jumps': '14'}, {'barcode': 'SRig10', 'total_jumps': '0'}, {'barcode': 'SRig1', 'total_jumps': '0'}, {'barcode': 'SRig4', 'total_jumps': '0'}, {'barcode': 'Srig5', 'total_jumps': '0'}, {'barcode': 'SRig14', 'total_jumps': '0'}, {'barcode': 'SRig13', 'total_jumps': '0'}, {'barcode': 'SRig10', 'total_jumps': '3'}, {'barcode': 'SRig1', 'total_jumps': '4'}, {'barcode': 'SRig4', 'total_jumps': '4'}, {'barcode': 'Srig5', 'total_jumps': '3'}, {'barcode': 'SRig10', 'total_jumps': '0'}, {'barcode': 'SRig1', 'total_jumps': '0'}, {'barcode': 'SRig4', 'total_jumps': '0'}, {'barcode': 'Srig5', 'total_jumps': '0'}, {'barcode': 'SRig10', 'total_jumps': '0'}, {'barcode': 'SRig1', 'total_jumps': '0'}, {'barcode': 'SRig4', 'total_jumps': '0'}, {'barcode': 'Srig5', 'total_jumps': '0'}, {'barcode': 'SRig10', 'total_jumps': '0'}, {'barcode': 'SRig1', 'total_jumps': '0'}, {'barcode': 'SRig4', 'total_jumps': '0'}, {'barcode': 'Srig5', 'total_jumps': '0'}, {'barcode': 'SRig14', 'total_jumps': '16'}, {'barcode': 'SRig13', 'total_jumps': '14'}, {'barcode': 'SRig10', 'total_jumps': '0'}, {'barcode': 'SRig1', 'total_jumps': '0'}, {'barcode': 'SRig4', 'total_jumps': '0'}, {'barcode': 'Srig5', 'total_jumps': '0'}, {'barcode': 'SRig14', 'total_jumps': '0'}, {'barcode': 'SRig13', 'total_jumps': '0'}, {'barcode': 'SRig10', 'total_jumps': '3'}, {'barcode': 'SRig1', 'total_jumps': '4'}, {'barcode': 'SRig4', 'total_jumps': '4'}, {'barcode': 'Srig5', 'total_jumps': '3'}, {'barcode': 'SRig14', 'total_jumps': '16'}, {'barcode': 'SRig13', 'total_jumps': '14'}]



import re
container  = {}
for rig in data:
    if rig['barcode'] in list(container.keys()):  container[rig['barcode']] =  int(container[rig['barcode']] ) +  int(rig['total_jumps'] )  # add + 
    else:   container[rig['barcode']] = int(rig['total_jumps'] )
        
# pip install natsort==3.3.0

 
from natsort import natsorted

labels = natsorted(list(container.keys()))
data_set = [container[x] for x in labels]
print (labels)
print (data_set)
