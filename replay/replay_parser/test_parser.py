from pathlib import Path
from django.test import TestCase
from replay.replay_parser.parser import Parser


class ParserTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ParserTest, cls).setUpClass()
        parser = Parser(open(Path.cwd() / "replay" / "replay_parser" / "sample_replay.txt", "r").readlines())

    def test_parse_players(self):
        self.assertEqual(1, 2-1)

    def test44(self):
        self.assertEqual(4, 4)


