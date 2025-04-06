import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '600b5b5637c7b916381b1bcc5aa6115f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Scorpion",
    "photo_id": 4 
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']

change_pokemon = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = change_pokemon)
print(response_change.text)

catch_pokemon = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch_pokemon)
print(response_catch.text)