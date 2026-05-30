import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv  # Importa a biblioteca

# Carrega as variáveis definidas no arquivo .env
load_dotenv()

# Recupera a URI de forma oculta
uri = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    # print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["lojadb"]