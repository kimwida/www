#import os
import subprocess

strText = subprocess.check_output('ls', shell=True)
print ( "%s"  % strText)
