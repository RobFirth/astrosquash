from flask import Flask, render_template
from app import app, db
from .models import Player, Fixtures
from socket import gethostname

@app.route('/')
def home():
    return render_template('home.html', players = Player, fixtures = Fixtures, , link = '/results')

@app.route('/results')
def results():

    return render_template('results.html', players = Player, fixtures = Fixtures, link = '/')


from app import models
 
if __name__ == '__main__':
    if 'liveconsole' not in gethostname():
        app.run(debug=True)