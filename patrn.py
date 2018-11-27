#!/bin/python3

import os
import sys
import re

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    print (s)
    sl=list(s)
    zone=sl[-2]+sl[-1]
    tl=s.split(':')
    tl2=re.findall(r'\d+',s)
    print (tl,tl2)
    if zone=='PM':
        if tl2[0]=='12':
            tym='12:'+tl2[1]+':'+tl2[2]
        else:
            tym=str(12+int(tl[0]))+':'+tl2[1]+':'+tl2[2]
    else:
        if tl2[0]=='12':
            print (' in else if ')
            tym='00:'+tl2[1]+':'+tl2[2]
        else:
            print (' in else else')
            tym=tl[0]+':'+tl2[1]+':'+tl2[2]
    
    return tym


s='12:40:22AM'

result = timeConversion(s)

print (result)