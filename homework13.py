import requests
def func(user_id):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users =response.json()
    for user in users:
        if user['id'] == user_id:
            return { 
                "name": user['name'],
                "email":user['email'] ,
                "city":user['adress']['city'] ,
                "company":user['company']['name']
                }
        return None
        