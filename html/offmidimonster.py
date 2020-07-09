#!/usr/bin/python

import os
import subprocess

print ("Content-type:text/html\r\n\r\n")
print ("midimonster is Off")

#os.system ("/usr/bin/midimonster /etc/midimonster/midimonster.cfg")
subprocess.Popen(['/bin/sh','/usr/bin/killmidimonster'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

