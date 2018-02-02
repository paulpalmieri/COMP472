from itertools import product
from string import ascii_uppercase as alphabet

# Returns a list that maps a letter to a pair of indexes relevant to the game grid
def get_position_dict():
    position_dict = {}
    k = 0
    for i, j in product(range(3), range(5)):
        position_dict[alphabet[k]] = (i, j)
        k += 1
    return position_dict

position_dict = get_position_dict()