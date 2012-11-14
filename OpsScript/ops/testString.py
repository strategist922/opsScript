'''
Created on 2012-11-14

@author: johnyang
'''

from datetime import datetime

if __name__ == "__main__":
    
    m="master.log.2012-11-14"
    i=m.find("log.")

    d=m[i+4:i+14]
    try:
        dateobject=datetime.strptime(d,"%Y-%M-%d")
        print "ok"
    except :
        print "error"
    
        
        
    