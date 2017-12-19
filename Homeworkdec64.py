# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:15:35 2016

@author: Emad
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 04:47:23 2016

@author: Emad
"""

import numpy as np
import cv2
import sys
import cPickle as pickle

yf=open('yf1.txt', 'r')
Cbf=open('Cbf1.txt', 'r')
Crf=open('Cbf1.txt', 'r')

while(True):
    
    

    reducedyf=pickle.load(yf)
    reducedcbf=pickle.load(Cbf)
    reducedcrf=pickle.load(Crf)
    
    reducedyf1=reducedyf.copy()
    reducedyf1=np.array(reducedyf1,dtype='float64')
    
    reducedcbf1=reducedcbf.copy()
    reducedcbf1=np.array(reducedcbf1,dtype='float64')
    
    reducedcrf1=reducedcrf.copy()
    reducedcrf1=np.array(reducedyf1,dtype='float64')
    
    R= 1.0 * reducedyf1 + 1.4025 * reducedcrf1
    G= 1*reducedyf1-0.34434*reducedcbf1-0.7144*reducedcrf1
    B= 1*reducedyf1+1.7731*reducedcbf1
 
 

    
    

    cv2.imshow('R',R)
    cv2.imshow('G',G)
    cv2.imshow('B',B)
    
    
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

yf.close()
Cbf.close()
Crf.close()
cv2.destroyAllWindows()
