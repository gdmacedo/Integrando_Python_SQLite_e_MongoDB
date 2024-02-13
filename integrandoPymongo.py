import pprint

client = []
db = client.test
collection = db.test_collection

post = {
    "Nome":"Glener",
    "cpf":"6547898544",
    "endereco": "dadadad",
    "conta": {
        "tipo": "digital",
        "agencia": "Vila Olimpia",
        "num": 34,
        "saldo": 7584553233
        },
    }

posts = db.pots
post_id = posts.insert_one(post).inserted_id
print(post_id)

pprint.pprint(db.posts.find_one())
new_post = [{
    "Nome":"Isabel",
    "cpf":"121212314588",
    "endereco": "Rua Santa Cecilia, 332",
    "conta": {
        "tipo": "corrente",
        "agencia": "ccddee",
        "num": 35,
        "saldo": 3285133
        },
    },
    {
        "Nome":"AnaLúcia",
        "cpf":"1234567895",
        "endereco": "dadadad",
        "conta": {
            "tipo": "poupança",
            "agencia": "aabbcc",
            "num": 66,
            "saldo": 852113
        },
    }]

result = posts.insert_many(new_post)
print(result.inserted_ids)

pprint.pprint(db.posts.find_one({"Nome": "AnaLúcia"}))

print("\n Documentos presentes em posts")
for post in posts.find():
    pprint.pprint(post)

print(post.count_documents({"Nome":"Isabel"}))

print("\n Documentos presentes em posts de maneira ordenada")
for post in posts.find({}).sort("Nome"):
    pprint.pprint(post)