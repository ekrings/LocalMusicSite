from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import CreateNewArtist
from app.models import Artist, Event, Venue

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/artists')
def artists():
    artistList = Artist.query.all()
    return render_template('artists.html', title='Artists', artists=artistList)

@app.route('/newArtists', methods=['GET', 'POST'])
def newArtists():
    form = CreateNewArtist()
    if form.validate_on_submit():
        a1 = Artist(artistName=form.name.data, description=form.description.data, hometown=form.hometown.data)
        db.session.add(a1)
        db.session.commit()
        flash('New artist created: {}'.format(form.name.data))
        return redirect(url_for('artists'))



    return render_template('newArtists.html', title="Add New Artist", form=form)

@app.route('/about/<name>')
def about(name):
    info = Artist.query.filter_by(artistName=name).first_or_404()
    return render_template('about.html', title="About Artists", info=info)

@app.route('/populate_db')
def populate_db():
    a1 = Artist(artistName='Stella Donnelly', hometown='Western Australia, Australia')
    a2 = Artist(artistName='Steve Lacy', hometown='Compton, California')
    a3 = Artist(artistName='Harry Styles', hometown='Redditch, United Kingdom')
    v1 = Venue(venueName='The Haunt', city='Ithaca, NY')
    v2 = Venue(venueName='Carnegie Hall', city='New York, NY')
    v3 = Venue(venueName='The Fonda Theatre', city='Los Angeles, CA')
    e1 = Event(date='Oct 12', venue_id=2, artist_id=1)
    e2 = Event(date='Sept 8', venue_id=3, artist_id=2)
    e3 = Event(date='Nov 30', venue_id=1, artist_id=3)
    e4 = Event(date='Dec 23', venue_id=1, artist_id=1)
    e5 = Event(date='Oct 31', venue_id=2, artist_id=2)
    db.session.add_all([a1, a2, a3, v1, v2, v3, e1, e2, e3, e4, e5])
    db.session.commit()
    return "Database has been populated"

@app.route('/reset_db')
def reset_db():
   flash("Resetting database: deleting old data and repopulating with dummy data")
   # clear all data from all tables
   meta = db.metadata
   for table in reversed(meta.sorted_tables):
       print('Clear table {}'.format(table))
       db.session.execute(table.delete())
   db.session.commit()
   return "Database has been reset"