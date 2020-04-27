#!/usr/bin/python3.7

import sqlite3
import cgi, cgitb
import os
import subprocess
import cgi, cgitb

form = cgi.FieldStorage()

device = form.getvalue('device_name')

conn = sqlite3.connect('/var/www/chinook.db')
c = conn.cursor()
c.execute('select FirstName, LastName from employees where EmployeeId =1')
result = c.fetchone()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello World - First CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Hello World! This is my first CGI program</h2>")
print("<h4> %s %s </h4>" % (result[0], result[1]) )

#strls = subprocess.check_output("aseqdump -l | awk 'NR>4'", shell=True, stderr=subprocess.STDOUT)
strls = subprocess.check_output("aseqdump -l | awk 'NR>1 { printf \"%s %s \", $1, $2}'", shell=True, stderr=subprocess.STDOUT)
#strls = subprocess.run(['aseqdump','-l'], capture_output=True, text=True)
mystr = strls.decode()
mystr = mystr.split()

#strKey = subprocess.check_output("ls /dev/input", shell=True, stderr=subprocess.STDOUT)
#strKey = strKey.decode()

#for x in mystr:
print("<h1><a href=LaunchControl.html> %s %s %s </a></h1>" % (mystr[0], mystr[1], mystr[2]))
#print("<h1> %s </h1>" % mystr)
#for y in strKey:
#print("<h3> %s </h3>" % strKey)
print("<h1> %s </h1>" % device)
print("</body>")
print("</html>")
c.close()

