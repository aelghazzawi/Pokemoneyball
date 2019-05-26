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
