# Consultando os documentos (posts) do banco de dados "bancoteste"
import datetime
import pprint
import pymongo
from pymongo import MongoClient

# Conecta ao servidor MongoDB Atlas no endereço da nuvem
cliente = pymongo.MongoClient('mongodb+srv://eberbrea:TCbMH6Fj6FzG7YSb@cluster0.hanztba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = cliente.bancoteste                 # Acessa o banco de dados chamado 'bancoteste'
con = db.posts                          # conecta ao banco de dados

# for p in con.find():                    # imprime todos os documentos/objetos (registros)
#     pprint.pprint(p)
#     print()

print('Total de Documentos:', con.count_documents({}))  # quantidade de documentos (registros)

# pprint.pprint(con.find_one({'author':'José'}))    # documentos que satisfazem a seleção

# print(con.count_documents({'tags':'MongoDB'}))     # quantidade de documentos cujas "tags" tem "MongoDB"

for p in con.find().sort('author'): # imprime todos os documentos por ordem de "author"
    print()
    pprint.pprint(p)




# resultado = db.profiles.create_index([('author', pymongo.ASCENDING)])       # author_1
# print(sorted(list(db.profiles.index_information())))        # ['_id_', 'author_1']


'''
{'_id': ObjectId('6883c28b6542faa2620d44cd'),
 'author': 'Maria',
 'date': datetime.datetime(2025, 7, 25, 14, 44, 43, 231000),
 'tags': ['Python', 'MongoDB', 'html'],
 'text': 'Testando a inclusão de Itens'}
 
'''