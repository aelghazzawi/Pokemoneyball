from pathlib import Path
from django.test import TestCase
from replay.replay_parser.parser import Parser


class ParserTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ParserTest, cls).setUpClass()
        cls.parser = Parser(open(Path.cwd() / "replay" / "replay_parser" / "sample_replay.txt", "r").readlines())

    def test_parse_players(self):
        players = self.parser.parse_players()
        self.assertEqual(players["p1"], "Adaam")
        self.assertEqual(players["p2"], "Ban Manaphy")
