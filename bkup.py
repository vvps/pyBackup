import os, sys
import zipfile
from time import *
import datetime
import balloontip as bt

startTime = datetime.datetime.now()
lf = open('C:/pyBackup.log', 'w')
lf.write("Starting backup.. " + strftime("%a, %d %b %Y %H:%M:%S", localtime()) + "\n");

sourceLocation = 'E:'
destinationLocation = 'V:/backupdata'

def zip(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(os.path.abspath(src)):]
            lf.write("Zipping %s \n" % arcname)
            zf.write(absname, arcname) #Comment this line during testing!
    zf.close()

try:
    zip(sourceLocation, destinationLocation)
    elapsedTime = datetime.datetime.now() - startTime
    lf.write("End backup " + strftime("%a, %d %b %Y %H:%M:%S", localtime()) + "\n");
    lf.write("Total time elapsed %s" % str(elapsedTime))
    btMessage = ("Backup successful!\nTotal time elapsed %s" % str(elapsedTime))
except:
    e = sys.exc_info()[0]
    lf.write( "Error: %s" % e )
    btMessage = ("Backup failed!\nError: %s" % e )
        
lf.close()
bt.balloon_tip('Backup script', btMessage)
