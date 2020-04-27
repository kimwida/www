
create table midi_device (
	id int primary key not null,
	name text not null,
	mode text not null check (mode in ('off','in','out'))
);

create table midi_control (
	id integer not null,
	name text not null check (name in ('fader','knob','button')),
	control_num integer not null,
	channel integer not null check (channel >=0 and channel <= 15),
	midi_type not null check ( midi_type in ('cc','note')),
	type_number not null check ( type_number >=0 and type_number <=127),
	foreign key(id) references midi_device(id)
		on update cascade
		on delete cascade
);

create table sacn (
	id_sacn integer primary key not null,
	ip_address text not null,
	universe integer not null,
	mode text not null check (mode in ('off','in','out'))
);

create table sacn_channel (
	id_sacn integer not null,
	channel_number integer not null,
	foreign key(id_sacn) references sacn(id_sacn)
		on update cascade
		on delete cascade
);

create table mapping (
	id integer not null,
	id_sacn integer not null,
	foreign key(id) references midi_device(id),
	foreign key(id_sacn) references sacn_channel(id_sacn)
);
