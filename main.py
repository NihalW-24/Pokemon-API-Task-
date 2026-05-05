import json 
import requests 

def get_pokemon_data(pokemon_name): 
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response  = requests.get(pokemon_url) 
    data = response.json()
    print(response.status_code)
    
    with open ("pokemon.json", "w") as file : 
        json.dump (data,file, indent=4 )
    

    

get_pokemon_data("pikachu")


