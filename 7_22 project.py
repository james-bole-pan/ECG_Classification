# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:32:05 2018

@author: Administrator
"""

import os
import glob
import wfdb
import numpy as np

dirpath = 'C:\\Users\\Administrator\\Desktop\\ECG-incart_pt\\*.atr'
datpath = 'C:\\Users\\Administrator\\Desktop\\ECG-incart_pt\\*.dat'
atrs_pathlist=glob.glob(dirpath)
dats_pathlist=glob.glob(datpath)
print (dats_pathlist)
x=wfdb.rdsamp(atrs_pathlist[0][:-4])
print(x[0])

samplist=[]
atrslist=[]
for i in dats_pathlist:
    tempsamp=wfdb.rdsamp(i[:-4])
    tempatr=wfdb.rdann(i[:-4],'atr')
    tempsamp=tempsamp[0]
    samplist.append(tempsamp)
    atrslist.append(tempatr)
print(len(samplist),len(atrslist))

np.save('samplist.npy',np.array(samplist))
np.save('atrslist.npy',np.array(atrslist))