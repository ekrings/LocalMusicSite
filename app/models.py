from app import db

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artistName = db.Column(db.String(60), index=True, unique=True)
    description = db.Column(db.String(240), index=True)
    hometown = db.Column(db.String(128), index=True)

    def __repr__(self):
        return '<Artist ()>'.format(self.artistName)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(60), index=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    venueName = db.Column(db.String(60), index=True)
    city = db.Column(db.String(128), index=True)

class ArtistToEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

















