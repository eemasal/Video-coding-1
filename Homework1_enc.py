# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:21:21 2016

@author: Emad
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:57:31 2016

@author: Emad
"""

import numpy as np
import cv,cv2
import cPickle as pickle

cap = cv2.VideoCapture(0)

yf=open('yf.txt', 'w')
Cbf=open('Cbf.txt', 'w')
Crf=open('Crf.txt', 'w')

for n in range(25):

    ret, frame = cap.read()
    
    if ret==True:
        Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255       
    
        Cb=(0.49970*frame[:,:,0]-0.33107*frame[:,:,1]-0.16864*frame[:,:,2])/255
   
        Cr=(-0.0812828*frame[:,:,0]-0.418531*frame[:,:,1]+0.499813*frame[:,:,2])/255
       
        
      
      
        pickle.dump(Y,yf)
        pickle.dump(Cb,Cbf)
        pickle.dump(Cr,Crf)


      
        cv2.imshow('Original',frame)
        cv2.imshow('Luminanz Y',Y)
        cv2.imshow('colorcomponent Cb',np.abs(Cb))
        cv2.imshow('colorcomponent Cr',np.abs(Cr))
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
yf.close()
Cbf.close()
Crf.close()
cv2.destroyAllWindows()
        