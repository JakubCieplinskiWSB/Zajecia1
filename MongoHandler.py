from pymongo import MongoClient
import pprint

class formContent:
    @staticmethod
    def getDictionary(email, rss):
        content = dict(email = str(email),
                    rss = str(rss))
        return content


class MongoHandler:
    def __init__(self, adress='mongodb://127.0.0.1:27017/mongo-spite'):
        self.mongoAdress = adress
        self.client = MongoClient(self.mongoAdress)
        self.db = self.client['test']
        self.posts = self.db.posts
    def getCollection(self):
        self.collection = self.db['emails']
    def getFeedsForAddress(self, email):
        feeds = []
        for post in self.posts.find({'email': str(email)}):
            feeds.append(post['rss'])
        return feeds
    def insert(self, data):
        self.posts.insert_one(data)