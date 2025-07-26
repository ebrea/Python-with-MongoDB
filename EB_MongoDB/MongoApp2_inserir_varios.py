# Inserindo vários documentos/objetos (registros)

import datetime
import pprint
import pymongo
# from pymongo import MongoClient

# Conecta ao servidor MongoDB Atlas no endereço da nuvem
cliente = pymongo.MongoClient('mongodb+srv://eberbrea:TCbMH6Fj6FzG7YSb@cluster0.hanztba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = cliente.bancoteste                 # Acessa o banco de dados chamado 'bancoteste'
con = db.posts                          # conecta ao banco de dados

novas_colecoes = [{                     # Inserção em massa/lotes ("bulk") de documentos (registros):
    "author": "José",
    "text": "Bom dia a todos",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime.now()
    },
    {
        "author": "Mike",
        "text": "Post from Mike",
        "title": "Mongo is fun",
        "date": datetime.datetime(2025, 7, 25, 15, 10)
    }
]

id_gerado = con.insert_many(novas_colecoes)       # Insere vários documentos e obtém o _id gerado
# pprint.pprint(id_gerado)

pprint.pprint(con.find_one())


