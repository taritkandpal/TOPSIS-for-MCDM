# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:54:40 2020

@author: Tarit
"""

import pandas as pd
import sys
import topsis as tp

cla=sys.argv
datafile=str(cla[1])
weights=cla[2].split(',')
pn=cla[3].split(',')
ds=pd.read_csv(datafile)

n=len(ds.columns)
if len(weights)!=n-1 or len(pn)!=n-1:
    print("Number of column weights or column +/- is incorrect")
    sys.exit()
for temp in pn:
    if temp!='+' and temp!='-':
        print("Incorect argument type")
        sys.exit()

i=tp.calbest(ds,weights,pn)
print("It is clear that the optimal choice with the highest performance score is :",ds.iloc[i,0])