# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 09:34:42 2018

@author: Administrator
"""

import numpy as np 
import matplotlib.pyplot as plt 
import pywt

#--------------------小波变换-----------------
allheartbeats=np.load('D:\\pbl\\samples.npy')
alllabels=np.load('D:\\pbl\\labels.npy')
asamp=allheartbeats[0,:,0]
cA1,cD1=pywt.wavedec(asamp,'db1',level=1)#[cA1,cD1]
plt.plot(range(len(asamp)),asamp)
plt.show()
plt.plot(range(len(cA1)),cA1)
plt.show()

#-------------------对所有信号小波滤波----------------
wavelet_samps=[]
for item in allheartbeats:
	wavelet_leads=[]
	for j in range(12):
		alead=item[:,j]#---一个导联
		tempcoffs=pywt.wavedec(alead,'db1',level=1)
		wavelet_leads.append(tempcoffs[0])
	wavelet_samps.append(wavelet_leads)
print(wavelet_samps[0][0].shape)

np.save('D:\\pbl\\finalheartbeats.npy',np.array(wavelet_samps))
np.save('D:\\pbl\\finallabels.npy',np.array(alllabels))
