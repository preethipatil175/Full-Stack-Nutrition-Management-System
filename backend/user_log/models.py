from mongoengine import Document,StringField, IntField, FloatField,DateField
from projectMainFolder import db

# Create your models here.
class User_Log(Document):
    MEAL_TYPE=[('Breakfast','Breakfast'),('Lunch','Lunch'),('Dinner','Dinner'),('Snacks','Snacks')]
    user_id=IntField(required=True)
    user_name=StringField(max_length=200,required=True)
    date=DateField(required=True)
    meal_type=StringField(choices=MEAL_TYPE,required=True)
    food_name=StringField(max_length=200,required=True)
    quantity_in_grams=IntField(min_value=1,required=True)
    calories=IntField(min_value=10,required=True)
    