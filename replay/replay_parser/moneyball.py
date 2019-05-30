import queue
from replay.replay_parser.battle import Pokemon
from replay.replay_parser.battle import Turn
from replay.replay_parser.battle import Switch
from replay.replay_parser.battle import Move
from collections import Counter


def aggregate_switches(turns):
    p1 = []
    p2 = []
    for turn in turns:
        for switch in turn.switches:
            if switch.player == 1:
                p1.append(switch.pokemon)
            else:
                p2.append(switch.pokemon)

    counter1 = Counter(p1)
    counter2 = Counter(p2)
    return counter1, counter2


def aggregate_moves(turns):
    p1 = []
    p2 = []
    for turn in turns:
        for move in turn.moves:
            if move.player == 1:
                p1.append(move.pokemon)
            else:
                p2.append(move.pokemon)

    counter1 = Counter(p1)
    counter2 = Counter(p2)
    return counter1, counter2


def aggregate_damage(turns, teams):
    """ Computes direct damage done by each Pokemon """
    # TODO: Support indirect damage health, Substitute, recoil etc

    # Get the teams in a dict first
    player1_team = {}
    player2_team = {}
    for pokemon in teams['p1']:
        player1_team[pokemon.species] = Pokemon(pokemon)
    for pokemon in teams['p2']:
        player2_team[pokemon.species] = Pokemon(pokemon)




