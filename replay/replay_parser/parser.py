class Parser:
	def __init__(self, text, url=None):
		self.text = text
		self.url = url

	def parse_players(self):
		""" Returns list of player names """
		players_lines = [line for line in self.text if line.startswith("|player")]

