
select Artist.firstname, Artist.lastname, Event.date from Event
join Event on Event.artistID = Artist.id
where Artist.firstname = "Miley"

select * from Venue
join Event on Event.artistID = Artist.id
join ArtistToEvent on Event.id = ArtistToEvent.eventID
join Venue on ArtistToEvent.artistID = Event.id
