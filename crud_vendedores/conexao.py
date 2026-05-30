from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin:admin%4026@lojadb.ldrpg3h.mongodb.net/?appName=lojadb"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["lojadb"]

for doc in db["itens_notas_fiscais"].find():
    print(doc)