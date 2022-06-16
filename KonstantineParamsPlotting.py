# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 10:57:06 2022

@author: gera2396
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy
import pandas as pd
dpath=r"C:\Users\gera2396\OneDrive - University of Idaho\NASA Ballonn\Waves from sharepoint\Balloons and Gravity Waves\waveDetectionHodograph\Results\konstantine_result"
file=r"\T1_params.csv"
begin=r"\T"
en=r"_params.csv"

x=1
for x in range(1,19):   #the file names in order there is no 20 so skipping 20 required a second loop latter
    path = dpath + begin + str(x) + en
    df = pd.read_csv(path)
    df.head()
    
    a=df['Time (s)']    #slicing the needed data
    b=df['Alt. [km]']   #slicing the needed data
    R=df['Int. Freq.(rad/s)']   #slicing the needed data
    plt.plot(a,R)
    plt.xlabel ('a (time)')
    plt.ylabel('R (intrinsic)')
    y=str(x)    #taking flight number and making it a string
   
    plt.title('flight ' +y)
    plt.show()
    
    plt.plot(b,R)
    plt.xlabel ('b (height)')
    plt.ylabel('R (intrinsic)')
    plt.title('flight '+ y)
    plt.show()


for x in range(21,51):
    path = dpath + begin + str(x) + en
    df = pd.read_csv(path)
    df.head()
    
    a=df['Time (s)']
    b=df['Alt. [km]']
    R=df['Int. Freq.(rad/s)']
    plt.plot(a,R)
    plt.xlabel ('a (time)')
    plt.ylabel('R (intrinsic)')
    y=str(x)
   
    plt.title('flight '+ y)
    plt.show()
    
    plt.plot(b,R)
    plt.xlabel ('b (height)')
    plt.ylabel('R (intrinsic)')
    plt.title('flight '+ y)
    plt.show()
    https://github.com/konst789/gravity-waves.git
    