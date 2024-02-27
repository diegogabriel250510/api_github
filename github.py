import requests

print('Github Users\n')

username = input('qual o nome do usuario?')

url = f'https://api.github.com/users/{username}'
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(data)
    #print(f'\nnome completo: {data["name"]}')
    #print(f'bio: {data["bio"]}')
    #print(f'localização: {data["location"]}')
    #print(f'seguidores: {data["followers"]}')
    #print(f'seguindo: {data["following"]}')
else:
    print('não foi possivel encotrar usuario')