from app import app

from flask import render_template, request
import requests

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pokemon/', methods=['POST'])
def pokemon():
    pokemon_name = request.form['pokemon_name']
    pokemon_data = get_data(pokemon_name)
    return render_template('pokemon.html', data=pokemon_data)

def get_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if response.ok:
        pokemon = response.json()
        poke_info = {
            'Name' : pokemon['name'].title(),
            'Ability' : pokemon['abilities'][0]['ability']['name'].title(),
            'Sprite' : pokemon['sprites']['front_shiny'],
            'HP-Base Stat' : pokemon['stats'][0]['base_stat'],
            'Attack-Base-Stat' : pokemon['stats'][1]['base_stat'],
            'Defense-Base-Stat' : pokemon['stats'][2]['base_stat']
        }
        return poke_info

