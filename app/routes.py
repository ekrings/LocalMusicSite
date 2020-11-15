from flask import render_template, flash, redirect, url_for, request, session
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import CreateNewArtist, LoginForm, RegistrationForm, CreateNewVenue, CreateNewEvent
from app.models import Artist, Event, Venue, User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/artists')
def artists():
    artistList = Artist.query.all()
    return render_template('artists.html', title='Artists', artists=artistList)

@app.route('/about/<name>')
def about(name):
    info = Artist.query.filter_by(artistName=name).first_or_404()
    return render_template('about.html', title="About Artists", info=info)


@app.route('/populate_db')
def populate_db():
    a1 = Artist(artistName='Stella Donnelly', hometown='Western Australia, Australia')
    a2 = Artist(artistName='Steve Lacy', hometown='Compton, California')
    a3 = Artist(artistName='Harry Styles', hometown='Redditch, United Kingdom')
    v1 = Venue(name='The Haunt', city='Ithaca, NY')
    v2 = Venue(name='Carnegie Hall', city='New York, NY')
    v3 = Venue(name='The Fonda Theatre', city='Los Angeles, CA')
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/newArtists', methods=['GET', 'POST'])
@login_required
def newArtists():
    form = CreateNewArtist()
    if form.validate_on_submit():
        a1 = Artist(artistName=form.name.data, description=form.description.data, hometown=form.hometown.data)
        db.session.add(a1)
        db.session.commit()
        flash('New artist created: {}'.format(form.name.data))
        return redirect(url_for('artists'))
    return render_template('newArtists.html', title="Add New Artist", form=form)


@app.route('/newVenue', methods=['GET', 'POST'])
@login_required
def newVenue():
    form = CreateNewVenue()
    if form.validate_on_submit():
        v1 = Venue(name=form.name.data, address=form.address.data, city=form.city.data, state=form.state.data)
        db.session.add(v1)
        db.session.commit()
        flash('New venue created: {}'.format(form.name.data))
        return redirect(url_for('artists'))
    return render_template('newVenue.html', title="Add New Venue", form=form)

@app.route('/newEvent', methods=['GET', 'POST'])
@login_required
def newEvent():
    form = CreateNewEvent()
    venue = Venue.query.all()
    if form.validate_on_submit():
        e1 = Event(name=form.name.data, date=form.startTime.data, venue_id=venue)
        session['startdate'] = form.startdate.data
        form.venue.choices = [(g.id, g.name) for g in Venue.query.order_by('name')]
        db.session.add(e1)
        db.session.commit()
        flash('New event created: {}'.format(form.name.data))
        return redirect(url_for('artists'))
    return render_template('newEvent.html', title="Add New Event", form=form)


