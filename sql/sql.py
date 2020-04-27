f = open ("test.sql","w")

strSQL = ''

#insert midi_device data
midiDevice = ["Launch Control", "APC mini", "Launch Pad MKII"]
i = 1
for x in midiDevice:
	strSQL = strSQL + 'insert into midi_device values (' + str(i) + ', \'' + x + '\', \'in\');\n'
	i += 1

#insert midi_control data
control_num = 1
i = 0
while i < 8:
	strSQL = strSQL + 'insert into midi_control values (1, \'knob\',' + str(control_num) + ',0,\'cc\',' + str(i+21) + ');\n'
	i += 1
	control_num += 1

i = 0
while i < 8:
	strSQL = strSQL + 'insert into midi_control values (1, \'knob\',' + str(control_num) + ',0,\'cc\',' + str(i+41) + ');\n'
	i += 1
	control_num += 1

control_num = 1
i = 0
while i < 4:
	strSQL = strSQL + 'insert into midi_control values (1, \'button\',' + str(control_num) + ',0,\'note\',' + str(i+9) + ');\n'
	i += 1
	control_num += 1

i = 0
while i < 4:
	strSQL = strSQL + 'insert into midi_control values (1, \'button\',' + str(control_num) + ',0,\'note\',' + str(i+25) + ');\n'
	i += 1
	control_num += 1

i = 0
while i < 4:
	strSQL = strSQL + 'insert into midi_control values (1, \'button\',' + str(control_num) + ',0,\'cc\',' + str(i+114) + ');\n'
	i += 1
	control_num += 1

#insert sacn data
ip_address = '2.1.1.2'
universe = '221'
strSQL = strSQL + 'insert into sacn values (1, \'' + ip_address + '\', ' + universe + ',\'out\');\n'

#insert sacn_channel data

f.write(strSQL)
f.close()
