#!/usr/bin/python3


class Place(BaseModel):
"""Public class attributes"""
    def __init__(self):
    city_id = City.id
    user_id = User.id
    name = ''
    self.description = 0
    self.number_rooms = 0
    self.number_bathrooms = 0
    self.max_guest = 0
    self.price_by_night = 0
    self.latitude = 0.0
    self.longitude = 0.0
    self.amenity_ids = {}
