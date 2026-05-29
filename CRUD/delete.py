from conexao import db

produtos = db['tabela_de_produtos']

produtos.delete_one({
    'CODIGO_DO_PRODUTO': 99999
})

print('Produto removido com sucesso!')
