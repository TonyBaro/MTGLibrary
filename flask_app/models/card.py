from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Card:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.type=data['type']
        self.cost=data['cost']
        self.keywords=data['keywords']
        self.flavor=data['flavor']
        self.power=data['power']
        self.toughness=data['toughness']
        self.user=[]

    @classmethod
    def add_card(cls,data):
        query = "INSERT INTO cards (name,type,cost,keywords,flavor,power,toughness,users_id) VALUES(%(name)s,%(type)s,%(cost)s,%(keywords)s,%(flavor)s,%(power)s,%(toughness)s,%(user)s)"
        return connectToMySQL('mtg_library').query_db( query, data)

    @classmethod
    def get_all_cards(cls,data):
        query ="SELECT * FROM cards WHERE cards.users_id = %(id)s"
        results = connectToMySQL ('mtg_library').query_db(query, data)
        all_cards= []
        for row in results:
            c={
                'id':row['id'],
                'name':row['name'],
                'type':row['type'],
                'cost':row['cost'],
                'keywords':row['keywords'],
                'flavor':row['flavor'],
                'power':row['power'],
                'toughness':row['toughness'],
            }
            all_cards.append(cls(c))
        return all_cards

