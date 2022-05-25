import sqlalchemy as db
from sqlalchemy.orm import relationship

from db import Base


class User(Base):
    full_name = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean(), default=True)


class Address(Base):
    House No. = db.Column(db.String, nullable=False)
    Area = db.Column(db.String, nullable=False)
    City = db.Column(db.String, nullable=False)
    State = db.Column(db.String, nullable=False)
    PinCode = db.Column(db.Integer, nullable=False)
    Latitude = db.Column(db.String, nullable=False)
    Longitude = db.Column(db.String, nullable=False)
 


