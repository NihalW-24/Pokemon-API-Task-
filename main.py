import json 
import requests 

def get_pokemon_data(pokemon_name): 
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response  = requests.get(pokemon_url) 
    data = response.json()
    print(response.status_code)

    pokemon_height_weight = {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"]
    }

    print(pokemon_height_weight)
    
    with open ("pokemon.json", "a") as file : 
        json.dump (pokemon_height_weight,file, indent=4 )
    
get_pokemon_data("pikachu")
get_pokemon_data("bulbasaur")


