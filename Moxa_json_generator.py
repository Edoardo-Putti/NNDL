''' 
this function generate the json file that associate to each images its class based 
on the number of mask detected by the Pascal Voc.
The json file is created such that it is coherent with the script split_dataset.py 
'''

import json
import xml.etree.ElementTree as ET
import os

data = {}
for el in os.listdir("Moxa3K/annotations/Pascal Voc/")[1:]:
    root = ET.parse(os.path.join("Moxa3K/annotations/Pascal Voc/", str(el))).getroot()
    mask=0
    nomask=0
    for tt in root.findall('object'):
        if tt[0].text == "mask":
            mask= mask+1
        else:
            nomask = nomask+1
    if mask == len(root.findall('object')):
        data[root[1].text] = 1
    elif nomask == len(root.findall('object')):
        data[root[1].text] = 0
    else:
        data[root[1].text] = 2

with open('train_gt.json', 'w') as outfile:
    json.dump(data, outfile)

''' 
this addition is used to crate a single json file to merge the two datasets

f1data = "path to moxa json"
f2data = "path to Maskdataset json" 

with open('MaskDataset/train_gt.json') as f2: 
  f2data = '\n' + f2.read()
    
with open('train_gt.json','a+') as f1:
    f1.write(f2data)
'''