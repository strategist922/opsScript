#!/usr/bin/env python
# encoding: utf-8
'''
NamenodeLogParse.CleanNameNodeLog -- clean namenode log ,only reserve 5 days



@author:     johnyang
            
@copyright:  2012 organization_name. All rights reserved.
            
@license:    license

@contact:    user_email
@deffield    updated: Updated

'''

import sys
import os
import socket
from datetime import date,timedelta,datetime


__all__ = []
__version__ = 0.1
__date__ = '2012-11-12'
__updated__ = '2012-11-12'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

today=date.today()

namenodelogpath="/home/hadoop/cluster-data/hadoop-logs/hadoop-hadoop-namenode-"
namenodedir="/home/hadoop/cluster-data/hadoop-logs/"
hostname=socket.gethostname()


def getDayStr(n):

    if n<0:
        n=abs(n)

        return today-timedelta(n)
    else:
        return today+timedelta(n)
    

def cleanLog(keepday):
    os.chdir(namenodedir)
    keepdaystr=str(getDayStr(-keepday))
    for i in os.listdir(namenodedir):
            
        if i.find("namenode-"+hostname)!=-1 :
            m=i.find("log.")
            if m!=-1:
                d=i[m+4:m+14]

                try: 
                    dateobject=datetime.strptime(d,"%Y-%M-%d")
                    if d<keepdaystr:
                        print "prepare to delete :" + i 
                        os.remove(i)
                except Exception,e:
                    print e
            

def main(keepday):
                
    cleanLog(int(keepday))
    


if __name__ == "__main__":
    
    sys.exit(main(keepday=sys.argv[1]))