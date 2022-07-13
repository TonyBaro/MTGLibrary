from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class card:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.type=data['type']
        self.cost=data['cost']
        self.keywords=data['keywords']
        self.flavor=data['flavor']
        self.power=data['power']
        self.toughness=data['toughness']

    @classmethod
    def add_card(cls,data):
        query = 'INSERT INTO cards'
        return connectToMySQL('mtg_library').query_db( query, data)
