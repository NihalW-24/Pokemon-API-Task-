import json 
import requests 

def get_pokemon_data(pokemon_name): 
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response  = requests.get(pokemon_url) 
    data = response.json()
    print(response.status_code)

    types = [t["type"]["name"] for t in data["types"]]
    sprite = data["sprites"]["front_default"]

    pokemon_height_weight = {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": types,
        "sprite": sprite
    }

    print(pokemon_height_weight)
    return pokemon_height_weight

pokemon_list = []
pokemon_list.append(get_pokemon_data("pikachu"))
pokemon_list.append(get_pokemon_data("bulbasaur"))
pokemon_list.append(get_pokemon_data("charizard"))
    
with open ("pokemon.json", "w") as file : 
    json.dump (pokemon_list,file, indent=4 )


