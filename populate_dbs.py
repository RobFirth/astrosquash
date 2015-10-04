import sys
sys.path.append('/Users/berto/astrosquash')
from app import db,models
import datetime

u = models.Player(played = 0, won = 0, lost = 0, name ='Rob Firth', photourl = '/static/images/rob_firth.jpg')
u1 = models.Player(played = 0, won = 0, lost = 0, name ='Chris Frohmaier', photourl = '/static/images/c_fro.jpg')
u2 = models.Player(played = 0, won = 0, lost = 0, name ='Aarran Shaw', photourl = '/static/images/a_shaw.jpg')
u3 = models.Player(played = 0, won = 0, lost = 0, name ='Chris Boon', photourl = '/static/images/c_boon.jpg')
u4 = models.Player(played = 0, won = 0, lost = 0, name ='Mat Smith', photourl = '/static/images/mathew_smith_small.jpg')

db.session.add(u)
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)

db.session.commit()

f = models.Fixtures(timestamp = datetime.datetime.utcnow(), winner = models.Player.query.filter_by(name = 'Rob Firth').first(), loser = models.Player.query.filter_by(name = 'Chris Boon').first())
f1 = models.Fixtures(timestamp = datetime.datetime.utcnow(), winner = models.Player.query.filter_by(name = 'Aarran Shaw').first(), loser = models.Player.query.filter_by(name = 'Chris Frohmaier').first())
f2 = models.Fixtures(timestamp = datetime.datetime.utcnow(), winner = models.Player.query.filter_by(name = 'Mat Smith').first(), loser = models.Player.query.filter_by(name = 'Rob Firth').first())

db.session.add(f)
db.session.add(f1)
db.session.add(f2)

db.session.commit()