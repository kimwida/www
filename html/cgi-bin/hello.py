#!/usr/bin/python3.7

import sqlite3
import cgi, cgitb
import os
import subprocess

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>MIDI Monster Web Setting Program</title>")
print("</head>")
print("<body>")
print("<h1>Hi! This is MIDI Monster Web Setting Program</h1>")

#find out MAX-Falcon keyboard's event number
device = subprocess.check_output("cat /proc/bus/input/devices | grep \'[NH]\' | paste - - | grep \'MAX\' | grep -v \'leds\' | grep -v \'mouse\' | awk \'{ print $NF } \'", shell=True, stderr=subprocess.STDOUT)
device = device.decode()
device = device.split()

if device == '':
	print ("No Device is Connected.<br>")
else:
	for x in device:
		print ("<a href=MAX-Falcon.py>MAX-Falcon</a> is connected %s<br>" % x)

#find out koolertron keyboard's event number
device = subprocess.check_output("cat /proc/bus/input/devices | grep \'[NH]\' | paste - - | grep \'Thumb\' | grep -v \'mouse\' | awk \'{ print $NF } \'", shell=True, stderr=subprocess.STDOUT)
device = device.decode()
device = device.split()

if device == '':
	print ("No Device is Connected.<br>")
else:
	for x in device:
		print ("<a href=Koolertron.py>Koolertron</a> is connected to %s<br>" % x)

device = subprocess.check_output("aseqdump -l | awk 'NR>4 { printf \"%s%s \", $2, $3}'", shell=True, stderr=subprocess.STDOUT)
device = device.decode()
device = device.split()

if device == '':
	print ("No Device is Connected.<br>")
else:
	for x in device:
		if x == 'LaunchControl':
			print ("<a href=LaunchControl.py>%s</a> is connected<br>" % x)
		elif x == 'APCMINI':
			print ("<a href=APCMINI.py>%s</a> is connected<br>" % x)

form = cgi.FieldStorage()
device = form.getvalue('device_name')
conn = sqlite3.connect('/var/www/midimonster.db')
strSQL = 'select id, name, mode from midi_device where name like \'%' + device + '%\' and mode = \'in\';'
c = conn.cursor()
c.execute('PRAGMA foreign_keys=1;')
c.execute(strSQL)
result = c.fetchall()

if result != None:
	for x in result:
		print("Id : %s<br>Name : %s<br>mode : %s<br>" % (x[0], x[1], x[2]) )
else:
	print("No data<br>")

strls = subprocess.check_output("aseqdump -l | awk 'NR>4 { printf \"%s %s %s \", $1, $2, $3}'", shell=True, stderr=subprocess.STDOUT)
mystr = strls.decode()
mystr = mystr.split()

print("<a href=LaunchControl.html> %s%s </a></h2>" % (mystr[1], mystr[2]))

print("</body>")
print("</html>")
c.close()

