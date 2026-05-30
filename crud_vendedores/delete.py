from conexao import db

vendedores = db['tabela_de_vendedores']

vendedores.delete_one({
    'MATRICULA':238
})

print('Vendedor removido com sucesso!')
