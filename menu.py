from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://tarozogiovana_db_user:Tarozinho22!@cluster0.omzwl1t.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercado_livre

def delete_usuario(nome, sobrenome):
    #Delete
    global db
    mycol = db.usuario
    myquery = {"nome": nome, "sobrenome":sobrenome}
    mydoc = mycol.delete_one(myquery)
    print("Deletando o usuário ", mydoc)

def create_usuario():
    #Insert
    global db
    mycol = db.usuario
    print("\nInserindo um novo usuário")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    key = 1
    end = []
    while (key != 'N'):
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {
            "rua":rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco)
        key = input("Deseja cadastrar um novo endereço (S/N)? ")
    mydoc = { "nome": nome, "sobrenome": sobrenome, "cpf": cpf, "end": end }
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)

def read_usuario(nome):
    #Read
    global db
    mycol = db.usuario
    print("Usuários existentes: ")
    if not len(nome):
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"], x["cpf"])
    else:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_usuario(nome):
    #Update
    global db
    mycol = db.usuario
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    print("Dados do usuário: ", mydoc)
    nome = input("Mudar Nome:")
    if len(nome):
        mydoc["nome"] = nome

    sobrenome = input("Mudar Sobrenome:")
    if len(sobrenome):
        mydoc["sobrenome"] = sobrenome

    cpf = input("Mudar CPF:")
    if len(cpf):
        mydoc["cpf"] = cpf

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)

def create_produto():
    #Insert
    global db
    mycol = db.Produto
    print("\nInserindo um novo produto")
    titulo = input("Digite o produto a ser criado: ")
    preco = float(input("Digite o preço do produto: "))
    mydoc = { "titulo": titulo, "preco": preco }
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)

def read_produto(titulo):
    #Read
    global db
    mycol = db.Produto
    print("Produtos existentes: ")
    if not len(titulo):
        mydoc = mycol.find().sort("titulo")
        for x in mydoc:
            print(x["titulo"], x["preco"])
    else:
        myquery = {"titulo": titulo}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_produto(titulo):
    #Update
    global db
    mycol = db.Produto
    myquery = {"titulo": titulo}
    mydoc = mycol.find_one(myquery)
    print("Dados do produto: ", mydoc)
    
    novo_titulo = input("Mudar Título:")
    if len(novo_titulo):
        mydoc["titulo"] = novo_titulo

    novo_preco = input("Mudar Preço:")
    if len(novo_preco):
        mydoc["preco"] = float(novo_preco)

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)

def delete_produto(titulo):
    #Delete
    global db
    mycol = db.Produto
    myquery = {"titulo": titulo}
    mydoc = mycol.delete_one(myquery)
    print("Deletando o produto ", mydoc)

def create_compra():
    #Insert
    global db
    mycol = db.compra
    print("\nInserindo uma nova compra")
    data_pedido = input("Data do pedido: ")
    status = input("Status (ex: Pago): ")
    valor_total = float(input("Valor Total: "))
    mydoc = { "data_pedido": data_pedido, "status": status, "valor_total": valor_total }
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)

def read_compra(status):
    #Read
    global db
    mycol = db.compra
    print("Compras existentes: ")
    if not len(status):
        mydoc = mycol.find()
        for x in mydoc:
            print(x["data_pedido"], x["status"], x["valor_total"])
    else:
        myquery = {"status": status}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_compra(status):
    #Update
    global db
    mycol = db.compra
    myquery = {"status": status}
    mydoc = mycol.find_one(myquery)
    print("Dados da compra: ", mydoc)
    
    novo_status = input("Mudar Status:")
    if len(novo_status):
        mydoc["status"] = novo_status

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)

def delete_compra(status):
    #Delete
    global db
    mycol = db.compra
    myquery = {"status": status}
    mydoc = mycol.delete_one(myquery)
    print("Deletando a compra ", mydoc)


key = 0
sub = 0
while (key != 'S'):
    print("\n1-CRUD Usuário")
    print("2-CRUD Produto")
    print("3-CRUD Compra")
    key = input("Digite a opção desejada? (S para sair) ")

    if (key == '1'):
        print("\nMenu do Usuário")
        print("1-Create Usuário")
        print("2-Read Usuário")
        print("3-Update Usuário")
        print("4-Delete Usuário")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create usuario")
            create_usuario()
            
        elif (sub == '2'):
            nome = input("Read usuário, deseja algum nome especifico? ")
            read_usuario(nome)
        
        elif (sub == '3'):
            nome = input("Update usuário, deseja algum nome especifico? ")
            update_usuario(nome)

        elif (sub == '4'):
            print("delete usuario")
            nome = input("Nome a ser deletado: ")
            sobrenome = input("Sobrenome a ser deletado: ")
            delete_usuario(nome, sobrenome)
            
    elif (key == '2'):
        print("\nMenu do Produto")
        print("1-Create Produto")
        print("2-Read Produto")
        print("3-Update Produto")
        print("4-Delete Produto")  
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create produto")
            create_produto()
            
        elif (sub == '2'):
            titulo = input("Read produto, deseja algum título especifico? ")
            read_produto(titulo)
        
        elif (sub == '3'):
            titulo = input("Update produto, deseja algum título especifico? ")
            update_produto(titulo)

        elif (sub == '4'):
            print("delete produto")
            titulo = input("Título a ser deletado: ")
            delete_produto(titulo)

    elif (key == '3'):
        print("\nMenu da Compra")
        print("1-Create Compra")
        print("2-Read Compra")
        print("3-Update Compra")
        print("4-Delete Compra")  
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create compra")
            create_compra()
            
        elif (sub == '2'):
            status = input("Read compra, deseja algum status especifico? ")
            read_compra(status)
        
        elif (sub == '3'):
            status = input("Update compra, deseja algum status especifico? ")
            update_compra(status)

        elif (sub == '4'):
            print("delete compra")
            status = input("Status a ser deletado: ")
            delete_compra(status)

print("Tchau Prof...")