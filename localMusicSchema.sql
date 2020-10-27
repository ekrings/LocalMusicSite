create table Artist (
 id	        integer primary key autoincrement,
 artistName varchar(64) not null,
 hometown 	varchar(128)
);

create table Event (
	id		      integer primary key autoincrement,
    date 	varchar(64) not null,
    venueID integer not null,
    artistID integer not null,
    foreign key (venueID) references Venue(id)
);

create table Venue (
    id	          integer primary key autoincrement,
    venueName     varchar(64),
    city          varchar(64)

);

create table ArtistToEvent (
	id	      integer primary key autoincrement,
 	artistID integer not null,
	eventID  integer not null,
	foreign key (artistID) references Artist(id),
	foreign key (eventID) references Event(id)
);

select * from Artist
join Event on Event.artistID = Artist.id
join ArtistToEvent on Event.id = ArtistToEvent.eventID
join Artist on ArtistToEvent.artistID = Artist.id
where Artist.firstname like "Steve";