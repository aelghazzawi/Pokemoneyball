class Parser:
	def __init__(self, text, url=None):
		self.text = text
		self.url = url

	def parse_players(self):
		""" Returns dict of player num -> player name"""
		players_lines = [line for line in self.text if line.startswith("|player")]
		players = {}
		for line in players_lines:
			split_line = line.split("|")
			players[split_line[2]] = split_line[3]
		return players

	def parse_teams(self):
		""" Returns dict of player num -> team. Team represented by list of 6 mons. """
		pokemon_lines = [line for line in self.text if line.startswith("|poke")]
		teams = {}
		for line in pokemon_lines:
			split_line = line.split("|")
			player_number = split_line[2]
			pokemon = split_line[3].split(",", 1)[0]
			if player_number in teams.keys():
				teams[player_number].append(pokemon)
			else:
				teams[player_number] = [pokemon]
		return teams

