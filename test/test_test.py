import unittest, sqlite3
import sys
sys.path.insert(0, '..')
from sql_queries import *

connection = sqlite3.connect('../heroes.db')
cursor = connection.cursor()

class TestJoinStatements(unittest.TestCase):

    file = open("../sql_queries.py", "r")
    file.read()

    def test_select_all_power_types_for_batman(self):
        result = [('works hard',), ('unlimited financing',), ('expert martial artist',), ('advanced weaponry',)]
        self.assertEqual(cursor.execute(select_all_power_types_for_batman()).fetchall(), result)

    def test_select_total_damage_points_for_wonder_woman(self):
        result = [(50,)]
        self.assertEqual(cursor.execute(select_total_damage_points_for_wonder_woman()).fetchall(), result)

    def test_list_iron_mans_powers_and_respective_damage_points(self):
        result = [('works hard', 5), ('ultra smart', 20), ('unlimited financing', 5), ('advanced weaponry', 10)]
        self.assertEqual(cursor.execute(list_iron_mans_powers_and_respective_damage_points()).fetchall(), result)

    def test_total_power_of_only_humans(self):
        result = [(235,)]
        self.assertEqual(cursor.execute(total_power_of_only_humans()).fetchall(), result)

    def test_select_all_hero_names_with_superstrength_in_alphabetical_order(self):
        result = [('Captain America',), ('Cyborg',), ('Goku',), ('Hulk',), ('Superman',), ('Thor',), ('Wonder Woman',)]
        self.assertEqual(cursor.execute(select_all_hero_names_with_superstrength_in_alphabetical_order()).fetchall(), result)

    def test_list_heroes_and_their_num_of_powers_ordered_by_hero_name_alphabetically(self):
        result = [('Aquaman', 1), ('Batman', 4), ('Black Panther', 4), ('Black Widow', 4), ('Captain America', 5), ('Cyborg', 3), ('Goku', 7), ('Green Lantern', 1), ('Hulk', 2), ('Iron Man', 4), ('Megaman', 3), ('StretcherFlex', 1), ('Superman', 7), ('Thor', 3), ('Wonder Woman', 4)]
        self.assertEqual(cursor.execute(list_heroes_and_their_num_of_powers_ordered_by_hero_name_alphabetically()).fetchall(), result)

    def test_select_heroes_name_and_sum_damage_points_ordered_by_most_damage_to_least(self):
        result = [('Goku', 80), ('Superman', 80), ('Black Widow', 55), ('Captain America', 55), ('Wonder Woman', 50), ('Black Panther', 40), ('Cyborg', 40), ('Iron Man', 40), ('Thor', 40), ('Batman', 35), ('Hulk', 30), ('Megaman', 25), ('StretcherFlex', 10), ('Aquaman', 5), ('Green Lantern', 1)]
        self.assertEqual(cursor.execute(select_heroes_name_and_sum_damage_points_ordered_by_most_damage_to_least()).fetchall(), result)
