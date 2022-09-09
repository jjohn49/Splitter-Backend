from django.test import TestCase
from database import DataBase
# Create your tests here.

db = DataBase()

data = db.findUserByField("username","JJ")

datab = db.cluster


