f = open ("insert.sql","w")

strSQL = ''

#insert midi_device data
midiDevice = ["LaunchControl", "APCMINI", "LaunchPadMK2"]
for x in midiDevice:
	strSQL = strSQL + 'insert into midi_device ( name, mode ) values (\'' + x + '\', \'in\');\n'
	strSQL = strSQL + 'insert into midi_device ( name, mode ) values (\'' + x + '\', \'out\');\n'
	strSQL = strSQL + 'insert into midi_device ( name, mode ) values (\'' + x + '\', \'off\');\n'
strSQL = strSQL +'\n'

#insert midi_control (Launch Control) data
def insert_midi_control ( midi_device_id, name, num, ch, signal_type, signal_num):
	strSQL = 'insert into midi_control ( id_midi_device, name, num, ch, signal_type, signal_num ) values (' + str(midi_device_id) + ',\'' + name + '\',' + str(num) + ',' + str(ch) + ',\'' + signal_type + '\',' + str(signal_num) + ');\n'
	return strSQL

control = 'knob'
channel = 0
signal_type = 'cc'
signal_num = 21
control_num = 0

i = 0
while i < 8:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 1, control, control_num, channel, signal_type, i+21)
	i += 1
strSQL = strSQL +'\n'

i = 0
while i < 8:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 1, control, control_num,channel, signal_type, i+41)
	i += 1
strSQL = strSQL +'\n'

control = 'button'
signal_type = 'note'
control_num = 0
i = 0
while i < 4:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 1, control, control_num,channel, signal_type, i+9)
	i += 1
strSQL = strSQL +'\n'

i = 0
while i < 4:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 1, control, control_num,channel, signal_type, i+25)
	i += 1
strSQL = strSQL +'\n'

i = 0
signal_type = 'cc'
while i < 4:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 1, control, control_num,channel, signal_type, i+114)
	i += 1
strSQL = strSQL +'\n'

#====================================================midi_device id:2===============================
control = 'knob'
channel = 0
signal_type = 'cc'
signal_num = 21
control_num = 0

i = 0
while i < 8:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 2, control, control_num, channel, signal_type, i+21)
	i += 1
strSQL = strSQL +'\n'

i = 0
while i < 8:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 2, control, control_num,channel, signal_type, i+41)
	i += 1
strSQL = strSQL +'\n'

control = 'button'
signal_type = 'note'
control_num = 0
i = 0
while i < 4:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 2, control, control_num,channel, signal_type, i+9)
	i += 1
strSQL = strSQL +'\n'

i = 0
while i < 4:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 2, control, control_num,channel, signal_type, i+25)
	i += 1
strSQL = strSQL +'\n'

i = 0
signal_type = 'cc'
while i < 4:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 2, control, control_num,channel, signal_type, i+114)
	i += 1
strSQL = strSQL +'\n'

#=======================================================midi_device id:3===============================
control = 'knob'
channel = 0
signal_type = 'cc'
signal_num = 21
control_num = 0

i = 0
while i < 8:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 3, control, control_num, channel, signal_type, i+21)
	i += 1
strSQL = strSQL +'\n'

i = 0
while i < 8:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 3, control, control_num,channel, signal_type, i+41)
	i += 1
strSQL = strSQL +'\n'

control = 'button'
signal_type = 'note'
control_num = 0
i = 0
while i < 4:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 3, control, control_num,channel, signal_type, i+9)
	i += 1
strSQL = strSQL +'\n'

i = 0
while i < 4:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 3, control, control_num,channel, signal_type, i+25)
	i += 1
strSQL = strSQL +'\n'

i = 0
signal_type = 'cc'
while i < 4:
	control_num += 1
	strSQL = strSQL + insert_midi_control ( 3, control, control_num,channel, signal_type, i+114)
	i += 1
strSQL = strSQL +'\n'

#================================================insert sacn data===========================================
ip_address = '2.1.1.2'
universe = '221'
strSQL = strSQL + 'insert into sacn (ip_address, universe, mode) values (\'' + ip_address + '\', ' + universe + ',\'out\');\n'
universe = '222'
strSQL = strSQL + 'insert into sacn (ip_address, universe, mode) values (\'' + ip_address + '\', ' + universe + ',\'out\');\n'

#================================================insert sacn_channel data==================================
i=1
while i <= 512:
	strSQL = strSQL + 'insert into sacn_channel (id_sacn, ch_num) values (1,' + str(i) + ');\n'
	i+=1
strSQL += '\n'

i=1
while i <= 512:
	strSQL = strSQL + 'insert into sacn_channel (id_sacn, ch_num) values (2,' + str(i) + ');\n'
	i+=1
strSQL += '\n'

#================================================insert mapping data==================================
#mapping.sql have it.
f.write(strSQL)
f.close()
