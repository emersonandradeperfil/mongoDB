from conexao import db

vendedores = db['tabela_de_vendedores']

vendedores.update_one({'MATRICULA':2387},
                    {'$set': {'MATRICULA': 238}} )

print('Dados do vendedor atualizado com sucesso')