from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from .models import Player

app = Flask(__name__)      
db = SQLAlchemy(app)

@app.route('/')
def home():
  return render_template('home.html')

from app import models
 
if __name__ == '__main__':
  app.run(debug=True)