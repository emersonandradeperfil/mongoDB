from conexao import db

produtos = db['tabela_de_produtos']

resultado_produto = produtos.find()

# resultado_produto = produtos.find({
#     "SABOR": "Pera"
# })


for item in resultado_produto:
    print(item)


