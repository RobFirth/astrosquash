from app import db

class Player(db.Model):
    id = db.Column(db.integer, primary_key=True)
    played = db.Column(db.integer, primary_key=True)
    won = db.Column(db.integer, primary_key=True)
    lost = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    photourl = db.Column(db.String(120), index=True, unique=True)
    def __repr__(self):
            return '<User %r>' % (self.nickname)