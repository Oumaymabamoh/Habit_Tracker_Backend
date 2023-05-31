import unittest
from unittest.mock import patch
from io import StringIO
from analytics import *


class TestAnalytics(unittest.TestCase):
    def setUp(self):
        # Create a test database connection
        self.test_db = connect("test.db")

    def test_habits_list(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            habits_list(self.test_db)
            self.assertNotEqual(fake_out.getvalue(), "")  # Check if output is not empty
            print(fake_out.getvalue())

    def test_habits_by_period(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            habits_by_period(self.test_db, "Daily")
            self.assertNotEqual(fake_out.getvalue(), "")  # Check if output is not empty
            print(fake_out.getvalue())

    def test_longest_streak_all_habits(self):
        longest_streak = longest_streak_all_habits(self.test_db)
        expected_streak = 0
        self.assertEqual(longest_streak, expected_streak)
        print(f"Longest streak: {longest_streak}")

    def test_habit_longest_streak(self):
        streak = habit_longest_streak(self.test_db, "Habit1")
        expected_streak = 0
        self.assertEqual(streak, expected_streak)
        print(f"Habit1 longest streak: {streak}")


if __name__ == "__main__":
    unittest.main()
