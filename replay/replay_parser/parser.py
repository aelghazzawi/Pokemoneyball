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

	def parse_generation(self):
		""" Return generation as an integer """
		generation_line = [line for line in self.text if line.startswith("|gen")][0]
		return int(generation_line.split("|")[2])

	def parse_tier(self):
		""" Return tier name as a string (i.e OU) """
		tier_line = [line for line in self.text if line.startswith("|tier")][0]
		return tier_line.split(" ")[2].rstrip("\n")

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

	def parse_turn_count(self):
		""" Returns total number of turns in the battle. """
		return int([line for line in reversed(self.text)
						if line.startswith("|turn")][0].split("|")[2])

