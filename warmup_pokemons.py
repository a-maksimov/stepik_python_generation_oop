import sys
from collections import Counter

# pokemons = [line.strip() for line in sys.stdin]
pokemons = [
    'Pichu',
    'Pichu',
    'Tyrogue',
    'Pichu',
    'Combee',
    'Marill',
    'Tyrogue'
]
count = Counter(pokemons)
doubles = {pokemon: num for pokemon, num in count.items() if num > 1}
number = sum(doubles.values()) - len(doubles)
print(number)
