#!/usr/bin/env python
# coding: utf-8

# ### Various modules loaded:

import numpy as np
from numpy import diff
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import re
import csv


# Extract data for each sector and write in a separate file:



keyList = []
dataList = []
startnew=False
firsttime=True
flist=[]
# Replace with the name of your file in the following line:
with open('/home/stefan/Downloads/jython/fin.txt','r') as f:
    for line in f:
        if line.startswith('#'):
            if startnew:
                startnew=False
                fname=a[0]+'_'+b[0]+'_'+c[0]+'.csv' # file name  
                with open(fname,'w',newline='') as file:
                    write=csv.writer(file, delimiter=',')
                    write.writerows(dataList)
                dataList=[]
                flist.append(fname)
                file.close()
            if line.startswith("# index"):
                a=(re.findall('\d+', line ))
            if line.startswith("# iIndex"):
                b=(re.findall('\d+', line ))
            if  the namline.startswith("# jIndex"):
                c=(re.findall('\d+', line ))
            #key, comment = line.split('\n')
            #keyList.append(key[1:])
        else:
            startnew=True
            nums = line.split() # split the line into a list of strings by whitespace
            nums = [float(i) for i in nums]
            dataList.append([nums[6],nums[1]])

# Re-open each individual file to find the distance

resa=[];resb=[];
for fi in flist:
    df = pd.read_csv(fi,header=None)
    dfm=df.as_matrix()
    dff=dfm[:,1]
    nt=len(dff)
    pos=np.linspace(0,nt,nt)
    difdff=diff(dff)
    mipos=np.argmax(difdff>0)
    mival=dff[mipos]
    fit = np.polyfit(pos[int(nt/2):nt],dff[int(nt/2):nt],1)
    fit_fn = np.poly1d(fit)
    dist=fit_fn(mipos)-mival
    resa.append([fi,dist])
    buf=[int(i) for i in       fi.split('.')[0].split('_')]
    buf.append(dist)
    resb.append(buf)


# Save all results by 'index, iIndex, jIndex, distance':

with open('results','w',newline='') as file:
                    write=csv.writer(file, delimiter=',')
                    write.writerows(resb)





