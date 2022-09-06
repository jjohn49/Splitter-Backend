from database import DataBase

db = DataBase()
ret = db.postUserData("jjohns49@villanova.edu", "Jack", "Johnston", "JJ", "Green2002", ["mmoran", "mcarroll"])

print(ret)

