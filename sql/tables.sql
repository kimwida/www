
create table midi_device (
	id integer primary key autoincrement,
	name text not null,
	mode text not null check (mode in ('off','in','out'))
);

create table midi_control (
	id_midi_device integer not null,
	id integer primary key autoincrement,
	name text not null check (name in ('fader','knob','button')),
	num integer not null,
	ch integer not null check (ch >=0 and ch <= 15),
	signal_type text not null check ( signal_type in ('cc','note')),
	signal_num int not null check ( signal_num >=0 and  signal_num <=127),
	foreign key(id_midi_device) references midi_device(id)
		on update cascade
		on delete cascade
);

create table sacn (
	id integer primary key autoincrement,
	ip_address text not null,
	universe integer not null,
	mode text not null check (mode in ('off','in','out'))
);

create table sacn_channel (
	id_sacn integer not null,
	id integer primary key autoincrement,
	ch_num integer not null,
	foreign key(id_sacn) references sacn(id)
		on update cascade
		on delete cascade
);

create table mapping (
	id_midi_control integer not null,
	id_sacn_channel integer not null,
	foreign key(id_midi_control) references midi_control(id),
	foreign key(id_sacn_channel) references sacn_channel(id)
		on update cascade
		on delete cascade
);
