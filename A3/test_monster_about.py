from unittest import TestCase
from unittest.mock import patch
from A3 import monster
import io


class TestMonsterAbout(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)   # Tests printed output
    def test_monster_about(self, mock_stdout):
        expected_output = """The Monster Encyclopedia:
      Ghoul: Radioactive, humanoid creature with green flesh. Rumored to be whats left of humans.
      Radioactive Rat : An over sized rat. Sometimes a tasty snack for certain cat species.
      Rogue Robot: A robot with glitched programming. 
      Mutated Creature: Mutated beyond belief. Hard to tell what this creature is. 
      Pax: The demon thief of destiny. Feared by all and said to curse those unlucky enough to meet him.\n"""
        monster.monster_about()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_monster_about2(self):          # Tests that function returns None
        self.assertIsNone((monster.monster_about()))

