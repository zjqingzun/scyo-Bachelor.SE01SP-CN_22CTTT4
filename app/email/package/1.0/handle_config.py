import json




# ./app/email/config/username.json
def get_smtp(__name) :
    with open('./app/email/config/username.json', 'r') as file :
        data = json.load(file)
    return data['smtp'][__name]

def get_pop3(__name) :
    with open('./app/email/config/username.json', 'r') as file :
        data = json.load(file)
    return data['pop3'][__name]


# ./app/email/update/autoload.json
def update_autoload(__name) :
    with open('./app/email/update/autoload.json', 'r') as file :
        data = json.load(file)
    return data[__name]
