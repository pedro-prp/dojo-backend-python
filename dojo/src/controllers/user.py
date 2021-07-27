from db.db import user_db

def insert_new_user(content):
    new_user = dict()
    new_user['first_name'] = content['first_name']
    new_user['last_name']= content['last_name']
    new_user['birth_date']= content['birth_date']
    new_user['age'] = content['age']
    new_user['cpf'] = content['cpf']

    user_db.append(new_user)

    return 'Criado com sucesso', 201


def get_all_users():
    response = dict()
    response['users'] = user_db

    return response, 200

