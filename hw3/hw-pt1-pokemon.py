# June 15 2021

import requests


docs = 'https://pokeapi.co/docs/v2'


print(f'The documentations URL is: {docs}')


pokemon = 'https://pokeapi.co/api/v2/pokemon/{id}/'


poke55 = requests.get(pokemon.replace('{id}','55')).json()


generation = 'https://pokeapi.co/api/v2/generation/'


generation = requests.get(generation).json()


# https://pokeapi.co/docs/v2#pokemon

# height: The height of this Pokémon in decimetres.


print(f'The pokemon #55 is {poke55["name"]} and it has {poke55["height"]*10} centimetres. I have discovered {len(generation["results"])} versions of the game')


type = 'https://pokeapi.co/api/v2/type/'


types = requests.get(type).json()['results']


electric_api = list(filter(lambda pokes: pokes['name'] == 'electric', types))[0]['url']


electric_pokes = requests.get(electric_api).json()['pokemon']


electric_pokes = [pokes['pokemon']['name'] for pokes in electric_pokes]


electric_names = requests.get(electric_api).json()['names']


electric_korean_name = list(filter(lambda pokes: pokes['language']['name'] == 'ko', electric_names))[0]['name']


print(f'In Korea, electric pokemons are called {electric_korean_name} and we have found {len(electric_pokes)} in the API. Here is the list: {",".join(electric_pokes)}')


pikachu = requests.get(pokemon.replace('{id}','pikachu')).json()['stats']

eevee = requests.get(pokemon.replace('{id}','eevee')).json()['stats']


print(f'About the speed stats, Eevee has {eevee[5]["base_stat"]} and Pikachu {pikachu[5]["base_stat"]}, so the second one is faster')
