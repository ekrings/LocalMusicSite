from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')

@app.route('/artists')
def artists():
    artists = ["Lime Cordiale", "Saba", "Flo Milli", "Roy Ayers"]
    return render_template('artists.html', title='Artists', artists=artists)

@app.route('/newArtist')
def newArtist():
    return render_template('newArtist.html', title="Add New Artist")

@app.route('/about')
def about():
    info = {
        "name": "Lime Cordiale",
        "description": "Lime Cordiale are an Australian pop rock duo from Sydney, consisting of brothers Oli and Louis Leimbach. They formed in 2009 and released their debut studio album Permanent Vacation in 2017.",
        "events": ["Brisbane, Australia - October 8th, 2020", "Adelaide, Australia - October 10th, 2020"]
    }
    return render_template('about.html', title="About Artists", info=info)