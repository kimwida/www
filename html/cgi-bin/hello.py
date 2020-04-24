#!/usr/bin/python3.7

import sqlite3
import cgi, cgitb
import os
import subprocess

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

strls = subprocess.check_output("aseqdump -l | awk 'NR>1 { printf \"%s %s \", $1, $2}'", shell=True, stderr=subprocess.STDOUT)
#strls = subprocess.run(['aseqdump','-l'], capture_output=True, text=True)
mystr = strls.decode()
mystr = mystr.split()

for x in mystr:
	print("<h1> %s </h1>" % x)
#print("<h1> %s </h1>" % mystr)
print("</body>")
print("</html>")
c.close()

