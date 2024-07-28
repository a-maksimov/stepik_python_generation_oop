from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass
class FootballTeam:
    name: str
    players: list = field(default_factory=list, repr=False, compare=False)

    def add_players(self, *args):
        self.players.extend(args)


player1 = FootballPlayer('Jude', 'Bellingham', 120000000)
player2 = FootballPlayer('Vinicius', 'Junior', 120000000)
player3 = FootballPlayer('Kylian', 'Mbappe', 180000000)

print(player1 == player2)
print(player1 == player3)
print(player1 > player3)
print(player1 < player3)


team = FootballTeam('PSG')

print(team)
print(team.name)
print(team.players)

team.add_players(FootballPlayer('Kylian', 'Mbappe', 180000000))
print(team.players)