# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:57:31 2016

@author: Emad
"""

import numpy as np
import cv,cv2
import cPickle as pickle

cap = cv2.VideoCapture(0)

yf1=open('yf1.txt','w')
Cbf1=open('Cbf1.txt','w')
Crf1=open('Crf1.txt','w')


for n in range(25):

    ret, frame = cap.read()
    
    if ret==True:
        Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255;       
    
        Cb=(0.49970*frame[:,:,0]-0.33107*frame[:,:,1]-0.16864*frame[:,:,2])/255;
   
        Cr=(-0.0812828*frame[:,:,0]-0.418531*frame[:,:,1]+0.499813*frame[:,:,2])/255;
        
        
        cv2.imshow('Original',frame)
        cv2.imshow('Luminanz Y',Y)
        cv2.imshow('colorcomponent Cb',np.abs(Cb))
        cv2.imshow('colorcomponent Cr',np.abs(Cr))
        
        
        
        reducedy1 = Y.copy()
        reducedy1=np.array(reducedy1,dtype='int8')
        
        reducedcb1 = Cb.copy()
        reducedcb1=np.array(reducedcb1,dtype='float16')
        
        reducedcr1 = Cr.copy()
        reducedcr1=np.array(reducedcr1,dtype='float16')
        
        pickle.dump(reducedy1,yf1)
        pickle.dump(reducedcb1,Cbf1)
        pickle.dump(reducedcr1,Crf1)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
yf1.close()
Cbf1.close()
Crf1.close()
cv2.destroyAllWindows()
        