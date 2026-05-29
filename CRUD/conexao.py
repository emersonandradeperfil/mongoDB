import pymongo
from pymongo import MongoClient

# conexão local
client = MongoClient('mongodb://localhost:27017/')

# selecionar banco
db = client['lojadb']


print('Conectado ao banco de dados')





