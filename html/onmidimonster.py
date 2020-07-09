#!/usr/bin/python

import os
import subprocess

print ("Content-type:text/html\r\n\r\n")
print ("midimonster is On")

#os.system ("/usr/bin/midimonster /etc/midimonster/midimonster.cfg")
subprocess.Popen(['/usr/bin/midimonster','/etc/midimonster/midimonster.cfg'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

