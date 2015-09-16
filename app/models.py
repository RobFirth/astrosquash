from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    played = db.Column(db.Integer, index=True)
    won = db.Column(db.Integer, index=True)
    lost = db.Column(db.Integer, index=True)
    name = db.Column(db.String(64), index=True)
    photourl = db.Column(db.String(120), index=True, unique=True)
    def __repr__(self):
            return '<User %r>' % (self.name)