from pathlib import Path
from django.test import TestCase
from replay.replay_parser.parser import Parser


class ParserTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ParserTest, cls).setUpClass()
        cls.parser = Parser(open(Path.cwd() / 'sample_replay.txt', 'r').readlines())

    def test_parse_players(self):
        players = self.parser.parse_players()
        self.assertEqual(players['p1'], 'Adaam')
        self.assertEqual(players['p2'], 'Ban Manaphy')

    def test_parse_teams(self):
        teams = self.parser.parse_teams()
        teams['p1'].sort()
        teams['p2'].sort()
        team1_names = []
        for pokemon in teams['p1']:
            team1_names.append(pokemon.species)
        self.assertEqual(team1_names, ['Houndoom', 'Latias', 'Nidoking', 'Scizor', 'Terrakion', 'Togekiss'])
        team2_names = []
        for pokemon in teams['p2']:
            team2_names.append(pokemon.species)
        self.assertEqual(team2_names, ['Aerodactyl', 'Cobalion', 'Gengar', 'Krookodile', 'Sylveon', 'Tsareena'])

    def test_parse_generation(self):
        gen = self.parser.parse_generation()
        self.assertEqual(gen, 7)

    def test_parse_tier(self):
        tier = self.parser.parse_tier()
        self.assertEqual(tier, 'UU')

    def test_parse_turn_count(self):
        count = self.parser.parse_turn_count()
        self.assertEqual(count, 21)

    def test_parse_turns(self):
        turns = self.parser.parse_turns()
        self.assertEqual(len(turns), 22)


