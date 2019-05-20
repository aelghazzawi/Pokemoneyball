from pathlib import Path
from django.test import TestCase
from replay.replay_parser.parser import Parser


class ParserTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ParserTest, cls).setUpClass()
        cls.parser = Parser(open(Path.cwd() / "sample_replay.txt", "r").readlines())

    def test_parse_players(self):
        players = self.parser.parse_players()
        self.assertEqual(players["p1"], "Adaam")
        self.assertEqual(players["p2"], "Ban Manaphy")

    def test_parse_teams(self):
        teams = self.parser.parse_teams()
        self.assertEqual(sorted(teams["p1"]), ["Houndoom", "Latias", "Nidoking", "Scizor", "Terrakion", "Togekiss"])
        self.assertEqual(sorted(teams["p2"]), ["Aerodactyl", "Cobalion", "Gengar", "Krookodile", "Sylveon", "Tsareena"])

    def test_parse_generation(self):
        gen = self.parser.parse_generation()
        self.assertEqual(gen, 7)

    def test_parse_tier(self):
        tier = self.parser.parse_tier()
        self.assertEqual(tier, "UU")


