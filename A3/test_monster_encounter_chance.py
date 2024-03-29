from unittest import TestCase
from unittest.mock import patch
import io
from A3 import sud


class TestMonsterEncounterChance(TestCase):
    @patch('random.randint', return_value=4)  # Tests printed output if monster encounter occurs
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_encounter_chance(self, mock_stdout, mock_integer):
        expected_output = 'You have encountered a monster yikes\n'
        sud.monster_encounter_chance()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('random.randint', return_value=4)  # Tests that return value is True if monster encounter occurs
    def test_monster_encounter_chance2(self, mock_integer):
        self.assertTrue(sud.monster_encounter_chance())

    @patch('random.randint', return_value=3)  # Tests that return value is False if monster encounter does not occur
    def test_monster_encounter_chance3(self, mock_integer):
        self.assertFalse(sud.monster_encounter_chance())

    @patch('random.randint', return_value=3)  # Tests printed output if monster encounter does not occur
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_encounter_chance4(self, mock_stdout, mock_integer):
        expected_output = 'You feel a calm wind blow in the air, At this moment you are truly alone in the wasteland\n'
        sud.monster_encounter_chance()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

