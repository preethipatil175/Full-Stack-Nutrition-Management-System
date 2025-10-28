from mongoengine import Document,StringField, IntField, FloatField
from projectMainFolder import db  # ensures connection


class User_Details(Document):
    GENDER_CHOICE=[('Male','Male'),('Female','Female')]
    GOAL_CHOICE=[('Loss','Weight loss'),('Maintain','Maintain Weight'),('Gain','Gain Weight')]
    ACTIVITY_CHOICE=[('Sedentary','Sedentary'),('Lightly Active','Lightly Active'),('Moderate','Moderate'),('Active','Active'),('Very Active','Very Active')]
    name = StringField(max_length=200,required=True)
    age = IntField(required=True)
    gender = StringField(max_length=10,choices=GENDER_CHOICE,required=True)
    height_cm = FloatField(required=True)
    weight_kg = FloatField(required=True)
    goal = StringField(max_length=100,choices=GOAL_CHOICE,required=True)
    activity_level =StringField(max_length=100,choices=ACTIVITY_CHOICE,required=True)
    # models which will be used later,after calculation
    bmr = FloatField()
    tdee = FloatField()
    calories = FloatField()