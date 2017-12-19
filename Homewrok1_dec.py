# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 04:47:23 2016

@author: Emad
"""

import numpy as np
import cv2
import sys
import cPickle as pickle

#Program to open a video input file 'videorecord.txt' (python txt format using pickle) and display it on the screen.
#This is a framework for a simple video decoder to build.
#Gerald Schuller, April 2015

yf=open('yf.txt', 'r')
Cbf=open('Cbf.txt', 'r')
Crf=open('Cbf.txt', 'r')

while(True):
#load next frame from file f and "de-pickle" it, convert from a string back to matrix or tensor:
    reducedyf=pickle.load(yf)
    reducedcbf=pickle.load(Cbf)
    reducedcrf=pickle.load(Crf)
    
    R= 1.0 * reducedyf + 1.4025 * reducedcrf
    G= 1*reducedyf-0.34434*reducedcbf-0.7144*reducedcrf
    B= 1*reducedyf+1.7731*reducedcbf
 
 

    #here goes the decoding:
    
    

    cv2.imshow('R',R)
    cv2.imshow('G',G)
    cv2.imshow('B',B)
    
    #Wait for key for 50ms, to get about 20 frames per second playback 
    #(depends also on speed of the machine, and recording frame rate, try out):
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

yf.close()
Cbf.close()
Crf.close()
cv2.destroyAllWindows()
