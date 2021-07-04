from flashcards import db


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String)
    translation = db.Column(db.String)
