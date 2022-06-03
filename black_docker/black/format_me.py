

import logging

ELECTRIC = 'electric'
FIRE = 'fire'
FLYING = 'flying' 
GHOST = 'ghost'
GRASS = 'grass'
POISON = 'poison'
WATER = 'water'

POKEMON_TYPE_LOOKUP = {'bulbasaur': GRASS, 'pikachu': ELECTRIC, 'squirtle': WATER, 'gengar':[GHOST, POISON], 'CHARIZARD': [FIRE, FLYING]}

logger = logging.getLogger(__name__)

def get_pokemon_type(pokemon):
    pokemon_type = POKEMON_TYPE_LOOKUP.get(pokemon, None)

    if not pokemon_type:
        logger.error("Pokemon does not exist in type lookup dict!")
        raise Exception("Pokemon type not found!")
    
    logger.info(f"The pokemon type of {pokemon_type} was found for the pokemon {pokemon}.")
    return pokemon_type