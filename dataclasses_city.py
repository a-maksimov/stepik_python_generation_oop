from dataclasses import dataclass


@dataclass
class City:
    name: str
    population: int
    founded: int


city1 = City('Tokyo', 14043239, 1457)
city2 = City('New York', 8467513, 1624)
city3 = City('Tokyo', 14043239, 1457)

print(city1 == city2)
print(city1 != city2)
print(city1 == city3)
print(city1 != city3)
