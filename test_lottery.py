import unittest


from lottery import generate_random_number
from lottery import lottery_random
from lottery import player_numbers

class Test_Lottery(unittest.TestCase):


    def test_generate_random_number(self):
        self.assertEqual(generate_random_number(), (1, 49),"Any number within range")
        self.countTestCases()

    def test_generate_lottery_numbers(self):
        self.assertEqual(lottery_random(), 1, 49)
        self.countTestCases()

    def test_generate_player_numbers(self):
        self.assertEqual(player_numbers(), 1, 49)
        self.countTestCases()




















