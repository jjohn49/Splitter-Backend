from django.test import TestCase
from database import DataBase
# Create your tests here.

db = DataBase()

data = db.findUserByField("username","JJ")

print(type(data[0]))

for x in data:
    print(x)

