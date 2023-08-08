import base64
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["medix_db"]
collection = db["pateints"]

datay = collection.find_one({ '_id' : "Image"})

byte = datay['string']

with open('test1.jpg', 'wb') as image:
    image.write(base64.b64decode((byte)))
