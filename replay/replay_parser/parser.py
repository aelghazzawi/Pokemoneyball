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

