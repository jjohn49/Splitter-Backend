from pymongo import MongoClient
import certifi

cluster = MongoClient("mongodb+srv://jjohns49:Green2002@cluster0.7d65ffv.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = certifi.where())
db = cluster["SplitterDB"]
collection = db["Users"]

collection.insert_one({"id":0,"name":"Jack"})

print("finished")

