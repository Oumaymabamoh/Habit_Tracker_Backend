import database as db
from datetime import datetime


class Habit:
    # Create a Habit object with specified attributes
    def __init__(self, name: str, category: str = None, periodicity: str = None, database="habits.db"):
        self.name = name
        self.category = category
        self.periodicity = periodicity
        self.db = db.connect(database)
        self.current_time = datetime.now().strftime("%m/%d/%Y %H:%M")
        self.streak = 0
        self.completion_time = None

    # adds new habit to the habit db and update the checks habit
    def add(self):
        if not db.habit_exists(self.db, self.name):  # Check if habit already exists
            # Create a new habit entry and check off the habit
            db.new_habit(self.db, self.name, self.category, self.periodicity, self.current_time, self.streak)
            db.checkoff_habit(self.db, self.name, False, 0, self.current_time)
            print(f"\nThe '{self.name.capitalize()} and '{self.periodicity.capitalize()}'"
                  f" Habit in '{self.category.capitalize()}' has been added.\n")
        else:
            print("\nHabit already exists, please select another habit.\n")

    # Delete the habit from the habit db
    def delete(self):
            db.delete_habit(self.db, self.name)  # Delete the habit entry
            print(f"\n '{self.name.capitalize()} is successfully deleted from database'\n")

    # Delete the category and all assigned category from the habit database
    def delete_category(self):
        if self.category is not None:  # Check if category is specified
            db.delete_category(self.db, self.name, self.category)  # Delete the category and assigned habits
            print(f"\n '{self.category.capitalize()} is successfully deleted from database'\n")
        else:
            print("No category specified.")

    # Update the habit periodicity and update the habit checks
    def update_periodicity(self):
        #if self.periodicity is not None:
        # Fetch the updated periodicity from the database
        db.update_periodicity(self.db, self.name, self.periodicity)
        db.checkoff_habit(self.db, self.name, False, 0, self.current_time)
            # Update the habit's periodicity attribute
            #print(f"\nSuccessfully changed the periodicity of the habit '{self.name.capitalize()}' to "
                  #f"'{self.periodicity.capitalize()}'\n")
        # Optionally, you can include an informative message if the habit's periodicity is already None
       # else:
            #print("The habit's periodicity is None. Please set a valid periodicity first.")

    # Get the current habit streak from the db and increases it by 1
    def increment(self):
        self.streak += 1

    def update_streak(self):
        # Increment the streak count
        self.streak += 1
        # Update the streak value in the database
        db.update_streak(self.db, self.name, self.streak, self.completion_time)

    # Resets the streak to 0
    def reset(self):
        self.streak = 0
        self.completion_time = None
        db.update_streak(self.db, self.name, self.streak, self.completion_time)

    def checked_off_habit(self):
        if not db.habit_exists(self.db, self.name):  # Check if habit exists
            print(f"\n {self.name.capitalize()} habit not found. \n")
            return

        # Get periodicity of habit
        periodicity = db.fetch_habit_periodicity(self.db, self.name)

        # Check if already completed based on periodicity
        if periodicity == "daily":
            # Check if already checked off today
            last_completed = db.fetch_last_completed(self.db, self.name)
            if last_completed == '0':
                self.update_streak()
                print(f"\n {self.name.capitalize()} habit already completed today. \n")
            else:
                self.reset()
        elif periodicity == "weekly":
            # Check if already completed this week
            last_completed_week = db.fetch_last_completed_week(self.db, self.name)
            if last_completed_week == '0':
                self.update_streak()
                print(f"\n{self.name.capitalize()} habit already completed this week.\n")
            else:
                self.reset()
        elif periodicity == "monthly":
            # Check if already completed this month
            last_completed_month = db.fetch_last_completed_month(self.db, self.name)
            if last_completed_month == '0':
                self.update_streak()
                print(f"\n{self.name.capitalize()} habit already completed this month.\n")
            else:
                self.reset()

        # Update streak and completion time
        db.checkoff_habit(self.db, self.name, True, self.streak, self.current_time.strip("%m/%d/%Y %H:%M"))

        print(f"\n{self.name.capitalize()} habit completed!\n")
