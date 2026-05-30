from crud_vendedores.conexao import db

produtos = db['tabela_de_produtos']

produtos.update_one({'CODIGO_DO_PRODUTO': 99999},
                    {'$set': {'PRECO_DE_LISTA': 10.5}} )

print('Preço do produto atualizado com sucesso')

