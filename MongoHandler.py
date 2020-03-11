from pymongo import MongoClient

class MongoHandler:
    def __init__(self, adress='mongodb://127.0.0.1:27017/mongo-spite'):
        self.mongoAdress = adress
        self.client = MongoClient(mongoAdress)
        self.db = client['local']
        posts = db.posts
    def getCollection():
        self.collection = self.db['emails']