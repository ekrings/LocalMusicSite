from flask import render_template, flash, redirect
from app import app
from app.forms import CreateNewArtist

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')

@app.route('/artists')
def artists():
    artists = ["Lime Cordiale", "Saba", "Flo Milli", "Roy Ayers"]
    return render_template('artists.html', title='Artists', artists=artists)

@app.route('/newArtists', methods=['GET', 'POST'])
def newArtists():
    form = CreateNewArtist()
    if form.validate_on_submit():
        flash ('New artist created: {}'.format(
            form.name.data))
        info = {}
        info["name"] = form.name.data
        info["description"] = form.description.data
        info["hometown"] = form.hometown.data
        return render_template('about.html', info=info)
    return render_template('newArtists.html', title="Add New Artist", form=form)

@app.route('/about')
def about():
    info = {
        "name": "Lime Cordiale",
        "description": "Lime Cordiale are an Australian pop rock duo from Sydney, consisting of brothers Oli and Louis Leimbach. They formed in 2009 and released their debut studio album Permanent Vacation in 2017.",
        "hometown": "Somewhere in Australia",
        "events": "Brisbane, Australia - October 8th, 2020"
    }
    return render_template('about.html', title="About Artists", info=info)