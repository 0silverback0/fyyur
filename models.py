
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    genres = db.Column(db.ARRAY(db.String(120)))
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    upcoming_shows = db.Column(db.ARRAY(db.String(500)))
    # past_shows_count = db.Column(db.Integer)
    upcoming_shows_count = db.Column(db.Integer)

    shows= db.relationship('Show', passive_deletes='all', backref='venue',  lazy='subquery')
    
    def __repr__(self):
        return f'<Venue ID: {self.id}, name: {self.name} city: {self.city} >'

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.ARRAY(db.String(120)))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website_link = db.Column(db.String)
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    upcoming_shows = db.Column(db.String)
    # past_shows_count = db.Column(db.Integer)
    # upcoming_shows_count = db.Column(db.Integer)

    shows = db.relationship('Show', backref='artist', lazy='subquery')

    def __repr__(self):
        return f'<Artist ID: {self.id} name: {self.name} city: {self.city} >'

class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id', ondelete='CASCADE'), nullable=False)
    artist_name = db.Column(db.String)
    artist_image_link = db.Column(db.String)
    start_time = db.Column(db.String, nullable=False)

   

# TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
