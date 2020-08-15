import collections

FootballTeam = collections.namedtuple('FootballTeam', ['name', 'country'])

# Class definition with special methods implemented
class Teams:
    countries = ['Germany', 'France', 'Spain']
    bundesliga_teams = ['RB Leipzig', 'Bayern Munich', 'Borussia Dortmund']

    def __init__(self, country_name):
        # List comprehension with a filter on country name
        self._teams = [FootballTeam(name, country) for name in self.bundesliga_teams
                                                   for country in self.countries if country == country_name]

    def __len__(self):
        return len(self._teams)

    def __getitem__(self, position):
        return self._teams[position]

    def getAll(self):
        return self._teams
    
teams = Teams("Germany")

print(len(teams))
print(teams[0])
print(teams.getAll())