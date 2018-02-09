from itertools import product
from string import ascii_uppercase

# candy types and colors
TYPES = {
    'r': 'orange',
    'b': 'pink',
    'w': 'sienna',
    'y': 'blue',
    'g': 'yellow',
    'p': 'green',
    'e': 'gray17'
}

# key codes for user input
KEY_CODES = {
    65362: 'UP',
    65361: 'LEFT',
    65363: 'RIGHT',
    65364: 'DOWN'
}

OUTPUT_PATH = "output/"

# maps uppercase letters to a grid index tuple (x, y)
def get_letter_to_index_map():
    position_dict = {}
    k = 0
    for i, j in product(range(3), range(5)):
        position_dict[ascii_uppercase[k]] = (i, j)
        k += 1
    return position_dict

# generates a list of positional letters (3x5 with 15 uppercase letters)
def get_index_to_letter_list():
    return [list(ascii_uppercase[0:5]), list(ascii_uppercase[5:10]), list(ascii_uppercase[10:15])]

# reads a file and generates a list containing the first line
def load_single_game(file_name):
    with open(file_name) as f:
        return f.readline().split()

letter_to_index_map = get_letter_to_index_map()
letter_list = get_index_to_letter_list()
