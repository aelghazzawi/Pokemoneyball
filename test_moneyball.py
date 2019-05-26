from pathlib import Path
from django.test import TestCase
from replay.replay_parser.parser import Parser
import replay.replay_parser.moneyball as mb


class MoneyballTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(MoneyballTest, cls).setUpClass()
        cls.parser = Parser(open(Path.cwd() / 'sample_replay.txt', 'r').readlines())
        cls.turns = cls.parser.parse_turns()

    def test_aggregate_switches(self):
        counters = mb.aggregate_switches(self.turns)
        c1 = counters[0]
        self.assertEqual(c1['Houndoom'], 2)
        self.assertEqual(c1['Togekiss'], 1)
        self.assertEqual(c1['Terrakion'], 2)
        self.assertEqual(c1['Scizor'], 2)
        self.assertEqual(c1['Latias'], 2)
        self.assertEqual(c1['Nidoking'], 0)

        c2 = counters[1]
        self.assertEqual(c2['Sylveon'], 1)
        self.assertEqual(c2['Tsareena'], 1)
        self.assertEqual(c2['Gengar'], 3)
        self.assertEqual(c2['Cobalion'], 3)
        self.assertEqual(c2['Aerodactyl'], 3)
        self.assertEqual(c2['Krookodile'], 3)


