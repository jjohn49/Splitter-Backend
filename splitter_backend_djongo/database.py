import pymongo
import certifi

class DataBase:
    def __init__(self):
        self.connectionString = "mongodb+srv://jjohns49:Green2002@cluster0.7d65ffv.mongodb.net/?retryWrites=true&w=majority"
        self.dbName = "SplitterDB"
        self.cluster = pymongo.MongoClient(self.connectionString, tlsCAFile = certifi.where())
        self.db = self.cluster[self.dbName]


    def getDatabaseCollection(self, collectionName):

        collection = self.db[collectionName]

        return collection

    def getAllUserData(self):

        collection = self.getDatabaseCollection("Users")

        return collection.find()


    def findUserByField(self, field, value):
        collection = self.getDatabaseCollection("Users")

        if not collection.find({field:value}) == None:
            return collection.find({field:value})
        else:
            return {"Error" : "User not for " + field + " : " + value}

    def postUserData(self, email, fname, lname, username, password, friends_list):
        userCollections = self.getDatabaseCollection("Users")

        ret = userCollections.insert_one({
            "email": email,
            "first_name":fname,
            "last_name":lname,
            "username":username,
            "password":password,
            "friends_list":friends_list
        })

        return ret.acknowledged