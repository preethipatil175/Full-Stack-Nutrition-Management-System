from mongoengine import Document, StringField, IntField, ListField
from projectMainFolder import db 

class Recipe(Document):
    name = StringField(required=True)
    meal_type = StringField(required=True, choices=["Breakfast", "Lunch", "Dinner"])
    diet_type = StringField(required=True, choices=["Veg", "Non-Veg"])
    calories = IntField(required=True)
    ingredients = ListField(StringField())
    instructions = StringField()


