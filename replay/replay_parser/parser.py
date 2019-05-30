import queue
import re
from replay.replay_parser.battle import Pokemon
from replay.replay_parser.battle import Turn
from replay.replay_parser.battle import Switch
from replay.replay_parser.battle import Move


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
		tier_line = [line for line in self.text if line.startswith('|tier')][0]
		return tier_line.split(' ')[2].rstrip('\n')

	def parse_teams(self):
		""" Returns dict of player num -> team. Team represented by list of 6 mons. """
		pokemon_lines = [line for line in self.text if line.startswith('|poke')]
		teams = {}
		for line in pokemon_lines:
			split_line = line.split('|')
			player_number = split_line[2]
			pokemon = split_line[3].split(',', 1)[0]
			if player_number in teams.keys():
				teams[player_number].append(Pokemon(pokemon))
			else:
				teams[player_number] = [Pokemon(pokemon)]
		return teams

	def parse_turn_count(self):
		""" Returns total number of turns in the battle. """
		return int([line for line in reversed(self.text)
						if line.startswith('|turn')][0].split('|')[2])

	def parse_turns(self):
		""" Returns a Queue of all the turns with Turn 1 at the front """
		turns = []
		switches = []
		moves = []
		# treat leads as Turn 0
		turn_number = 0
		is_switch = True
		p1_pokemon = None
		p2_pokemon = None
		for line in self.text:
			split_line = line.split('|')
			# accumulate all the switches and moves until next turn is found
			if line.startswith('|turn') and split_line[2] != '1':
				turns.append(Turn(turn_number, switches, moves))
				turn_number = line.split('|')[2]
				switches = []
				moves = []

			if line.startswith('|switch'):
				is_switch = True
				switch = split_line[2].split(' ')
				pokemon = switch[1]
				health = int(split_line[4].split('/', 1)[0])
				if switch[0] == 'p1a:':
					player = 1
					p1_pokemon = Pokemon(pokemon, health)
				else:
					player = 2
					p2_pokemon = Pokemon(pokemon, health)
				switches.append(Switch(player, Pokemon(pokemon, health)))

			if line.startswith('|move'):
				is_switch = False
				move = split_line[2].split(' ')
				player = 1 if move[0] == 'p1a:' else 2
				target = p2_pokemon if move[0] == 'p1a:' else p1_pokemon
				user_pokemon = move[1]
				move_name = split_line[3]
				moves.append(Move(player, user_pokemon, move_name, target))

			if line.startswith('|-damage'):
				new_health = int(re.split(r'[ /]+', split_line[3])[0])
				if is_switch:
					old_switch = switches[-1]
					del switches[-1]
					old_switch.pokemon.health = new_health
					if old_switch.player == 1:
						p1_pokemon = old_switch.pokemon
					else:
						p2_pokemon = old_switch.pokemon
					# TODO: keep track of how much damage dealt via hazards
					switches.append(Switch(old_switch.player, old_switch.pokemon))

				# TODO: add rocky helm/rough skin support (remove length condition)
				if not is_switch and len(split_line) < 5:
					old_move = moves[-1]
					del moves[-1]
					damage = old_move.target.health - new_health
					#print(old_move.user + ' has done ' + str(damage) + ' damage.')
					old_move.target.health = new_health
					moves.append(Move(old_move.player, old_move.user, old_move.move, old_move.target, damage))


		turns.append(Turn(turn_number, switches, moves))
		return turns





