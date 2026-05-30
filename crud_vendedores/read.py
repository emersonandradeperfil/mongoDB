from conexao import db

vendedores = db['tabela_de_vendedores']

resultado_vendedor = vendedores.find()

# resultado_produto = produtos.find({
#     "SABOR": "Pera"
# })


for item in resultado_vendedor:
    print(f'Matricula: {item['MATRICULA']} Vendedor: {item['NOME']}')


