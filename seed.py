from app import app
from models import db, Venue, Artist, Show

with app.app_context():
    db.drop_all()
    db.create_all()

    v1 = Venue( 
        name='The Musical Hop',
        genres=["Jazz", "Reggae", "Swing", "Classical", "Folk"],
        address='1015 Folsom Street',
        city='San Francisco',
        state='CA',
        phone='123-123-1234',
        website="https://www.themusicalhop.com",
        facebook_link='https://www.facebook.com/TheMusicalHop',
        seeking_talent=True,
        seeking_description="We are on the lookout for a local artist to play every two weeks. Please call us.",
        image_link='https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60',
        # past_shows=[4],
        upcoming_shows=[],
        # past_shows_count=1,
        upcoming_shows_count=0
    )

    v2 = Venue(
        name='The Dueling Pianos Bar',
        genres=["Classical", "R&B", "Hip-Hop"],
        address='335 Delancey Street',
        city='New York',
        state='NY',
        phone='914-003-113',
        website="https://www.theduelingpianos.com",
        facebook_link='https://www.facebook.com/theduelingpianos',
        seeking_talent=False,
        image_link='https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80',
        # past_shows=[],
        upcoming_shows=[],
        # past_shows_count=0,
        upcoming_shows_count=0
    )

    v3 = Venue(
        name='Park Square Live Music & Coffee',
        genres=["Rock n Roll", "Jazz", "Classical", "Folk"],
        address='34 Whiskey Moore Ave',
        city='San Francisco',
        state='CA',
        phone='415-000-1234',
        website="https://www.parksquarelivemusicandcoffee.com",
        facebook_link='https://www.facebook.com/ParkSquareLiveMusicAndCoffee',
        seeking_talent=False,
        image_link='https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80',
        # past_shows=[5],
        # upcoming_shows=[4, 5, 6],
        # past_shows_count=1,
        # upcoming_shows_count=1
    )

    a1 = Artist(
        id=4,
        name='Guns N Petals',
        genres=["Rock n Roll"],
        city='San Francisco',
        state='CA',
        phone='326-123-5000',
        website_link="https://www.gunsnpetalsband.com",
        facebook_link='https://www.facebook.com/GunsNPetals',
        seeking_venue=True,
        seeking_description="Looking for shows to perform at in the San Francisco Bay Area!",
        image_link='https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80',
        # past_shows=[1],
        upcoming_shows=[],
        # past_shows_count=1,
        # upcoming_shows_count=0
    )

    a2 = Artist(
        id=5,
        name='Matt Quevedo',
        genres=['Jazz'],
        city='new york',
        state='NY',
        phone='300-400-5000',
        website_link='',
        facebook_link="https://www.facebook.com/mattquevedo923251523",
        seeking_venue=False,
        image_link='https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80',
        # past_shows=[3],
        upcoming_shows=[],
        # past_shows_count=1,
        # upcoming_shows_count=0
    )

    a3 = Artist(
        id=6,
        name='The Wild Sax Band',
        genres=['Jazz', 'Classical'],
        city='San Francisco',
        state='CA',
        phone='432-325-5432',
        website_link='',
        seeking_venue=False,
        image_link='https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80',
        facebook_link='',
        # past_shows=[],
        upcoming_shows= [],
        # past_shows_count=0,
        # upcoming_shows_count=3
    )

    s1 = Show(
        artist_id = 4,
        venue_id = 1,
        artist_name = 'Guns N Petals',
        artist_image_link = 'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80',
        start_time = '2019-05-21T21:30:00.000Z'
    )
    
    s2 = Show(
        artist_id = 5,
        venue_id = 3,
        artist_name = 'Matt Quevedo',
        artist_image_link = 'https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80',
        start_time = '2019-06-15T23:00:00.000Z'
    )

    s3 = Show(
        artist_id=6,
        venue_id=3,
        artist_name = 'The Wild Sax Band',
        artist_image_link = 'https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80',
        start_time="2035-04-01T20:00:00.000Z"
    )

    s4 = Show(
        artist_id=6,
        venue_id=3,
        artist_name = 'The Wild Sax Band',
        artist_image_link = 'https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80',
        start_time="2035-04-08T20:00:00.000Z"
    )

    s5 = Show(
        artist_id=6,
        venue_id=3,
        artist_name = 'The Wild Sax Band',
        artist_image_link = 'https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80',
        start_time="2035-04-15T20:00:00.000Z"
    )

    db.session.add_all([v1, v2, v3])
    db.session.add_all([a1, a2, a3])
    db.session.add_all([s1, s2, s3,s4,s5])
    db.session.commit()
