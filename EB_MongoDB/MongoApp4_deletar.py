# Apagando os documentos (posts) do banco de dados "bancoteste"
import pprint
import pymongo

# Conecta ao servidor MongoDB Atlas no endereço da nuvem
cliente = pymongo.MongoClient('mongodb+srv://eberbrea:TCbMH6Fj6FzG7YSb@cluster0.hanztba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = cliente.bancoteste                 # Acessa o banco de dados chamado 'bancoteste'
con = db.posts                          # conecta ao banco de dados

apagar_documento = con.delete_one({"author": "Mike"})   # apaga o documento

for p in con.find():                    # imprime todos os documentos/objetos (registros)
    pprint.pprint(p)
    print()

print()
print("Deletados:", apagar_documento.deleted_count, '\n')
print('Total de Documentos:', con.count_documents({}))

# cliente.drop_database('bancoteste')   # apaga o banco de dados "bancoteste"




'''
O "drop" apaga o documentos (profiles, collections, profile_users) e o Banco de Dados:

    cliente.drop_database('bancoteste')


'''