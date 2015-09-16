from flask import Flask, render_template
from app import app, db
from .models import Player

@app.route('/')
def home():
  return render_template('home.html', players = Player)

from app import models
 
if __name__ == '__main__':
  app.run(debug=True)