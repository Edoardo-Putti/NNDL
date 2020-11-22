import pandas as pd
import os

data1 = pd.read_csv("path to first csv")
data2 = pd.read_csv("path to first csv")

data1 = pd.DataFrame(data1)

results = {'Id' : [],
           'Category' : []}
'''
the idea behind this function was to use two network trained to distinguished between two classes.
One network was trained using a dataset with as positive class images with only masks and 
imagise with peaple with masks and no togheter and as negative samples images with people 
without masks.
The oter network was trained using a dataset with as positive class images with people with masks
and as negative class images without and mixed masks.

the idea was to combine the results of the two network in order to generate a prediction of the
three classes NoMask(0) Mask(1) Mixed(2).

first network n1:
 -Mask + mixed = 0
 -NoMask = 1

Second network n2:
 -Mask = 0
 -NoMask + mixed = 1

 result:
 n1  n2  res
 0 + 0 = 1
 0 + 1 = 2
 1 + 0 = 2
 1 + 1 = 0

'''

for x in range(0,len(data1['Id'])):
    results['Id'].append(data1["Id"][x])
    for y in range(0,len(data1['Id'])):
        if data1["Id"][x] == data2["Id"][y]:
            if data2["Category"][x] == 0 and data1["Category"][x] == 0:
                results["Category"].append(1)
            elif data2["Category"][x] == 1 and data1["Category"][x] == 0:
                results["Category"].append(2)
            elif data2["Category"][x] == 0 and data1["Category"][x] == 1:
                results["Category"].append(2)
            elif data2["Category"][x] == 1 and data1["Category"][x] == 1:
                results["Category"].append(0)
            else:
                results["Category"].append(2)

df = pd.DataFrame(results, columns = ['Id','Category'])

df.to_csv(os.path.join(os.getcwd(),'results.csv'),index=False)