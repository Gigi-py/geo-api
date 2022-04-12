from enum import unique
from myapp import db

class Locations(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    address = db.Column(db.String(200), unique=False, nullable=False)
    city = db.Column(db.String(50), unique=False, nullable=False)
    state = db.Column(db.String(50), unique=False, nullable=False)
    zip_code = db.Column(db.String(20), unique=False, nullable=False)
    latitude = db.Column(db.String(40), unique=False, nullable=False)
    longitude = db.Column(db.String(40), unique=False, nullable=False)
    
    def __repr__(self):
        return f"{self.address}, {self.city}, {self.state}, \
                    {self.zip_code}, {self.longitude}, {self.latitude}"