import unittest
from habit import Habit
import database as db
from datetime import datetime, timedelta
import os
from freezegun import freeze_time


class TestHabit(unittest.TestCase):
    def setUp(self):
        # Initialize a habit object for testing
        self.habit = Habit("grocery", "life", "daily", "test.db")
        self.db = db.connect("test.db")
        self.habit.current_time = datetime.now().strftime("%m/%d/%Y %H:%M")

    def test_add(self):
        # Add a habit and check if it was added to the database
        self.habit.add()
        habit_exists = db.habit_exists(self.habit.db, self.habit.name)
        self.assertTrue(habit_exists)

    def test_delete(self):
        # Delete a habit and check if it was removed from the database
        self.habit.delete()
        habit_exists = db.habit_exists(self.habit.db, self.habit.name)
        self.assertFalse(habit_exists)

    def test_delete_category(self):
        # Delete a category and check if it was removed from the database
        self.habit.delete_category()

    def test_update_periodicity(self):
        # Update the periodicity of a habit and check if it was updated in the database
        self.habit.periodicity = "weekly"
        self.habit.update_periodicity()
        periodicity = db.fetch_habit_periodicity(self.habit.db, self.habit.name)
        self.assertEqual(periodicity, "weekly")

    def test_increment(self):
        # Increment the streak and check if it was updated in the habit object
        self.habit.increment()
        self.assertEqual(self.habit.streak, 1)

    def test_reset(self):
        # Reset the streak and check if it was updated in the habit object
        self.habit.reset()
        self.assertEqual(self.habit.streak, 0)

    def test_checkoff_daily_habit(self):
        # First checkoff
        self.habit.reset()
        self.habit.checked_off_habit()
        self.habit.increment()

    def test_checkoff_daily_habit_1(self):
        # Check off again on the same day, streak should increase
        self.habit.checked_off_habit()
        self.habit.increment()
        self.habit.update_streak()

    def test_checkoff_daily_habit_2(self):
        # Wait until next day and check off, streak should reset
        next_day = datetime.now() + timedelta(days=1)
        with freeze_time(next_day):
            self.habit.checked_off_habit()

    def test_checkoff_weekly_habit(self):
        # First checkoff
        self.habit.reset()
        self.habit.checked_off_habit()
        self.habit.increment()

    def test_checkoff_weekly_habit_2(self):
        # Check off the habit again after a week
        self.habit.checked_off_habit()
        self.habit.increment()

    def test_checkoff_monthly_habit(self):
        # First checkoff
        self.habit.reset()
        self.habit.checked_off_habit()
        self.habit.increment()

    def test_checkoff_monthly_habit_1(self):
        # Check off the habit again after a month
        self.habit.checked_off_habit()
        self.habit.increment()
        
    def tearDown(self):
        #Delete the test database
        os.remove("test.db")


if __name__ == '__main__':
    unittest.main()
