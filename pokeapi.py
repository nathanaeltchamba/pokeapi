from random import choices
from turtle import done
import requests


class Pokemon:
    calls = []
    base_url = 'https://pokeapi.co/api/v2/pokemon/'
    
    def __init__(self): 
        #self.api_version = f'data/{version}/weather'
        #self.api_key = '02435e511927d661b86684bcc096de53'
        self.data = None
        self.calls.append(self)
        
    def __repr__(self):
       return f'<APICall: works>'

    def pokemon_dictionary(self):
        pokemon_list = []

        
    def run(self):
        print('Loading Pokedeck...\n')

        print("Welcome to the Pokedeck where you'll find all the information about Pokemon. \n")


        pokemon = input("Which pokemon would you like to add to your pokedeck ").lower()


        

        
        response = requests.get(f'{self.base_url}/{pokemon}')
        self.data = response.json()

        
pokedeck = Pokemon()
pokedeck.run()
pokedeck.calls
pokedeck.data

pokemon_type = pokedeck.data['types'][0]['type']['name']
pokemon_weight = pokedeck.data['weight']
pokemon_abilites = pokedeck.data['abilities'][0]['ability']['name']
pokemon_hp = pokedeck.data['stats'][0]['base_stat']


print(pokemon_type, pokemon_weight,pokemon_abilites,pokemon_hp)

