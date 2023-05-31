from habit import Habit
from analytics import habits_list, habits_by_period
import analytics
import sys
from database import *
import questionary as qt
import get

# welcome message
print("*** Welcome to the {} ***".format("Habit Tracker app"))


# Command-line interface
def cli():
    """
    using the command line interface in order to interact with the user.

   """


# Connect to the database by calling the connect function
db = connect()

stop = False
while not stop:
    choice = qt.select("What would you like to do?",
                       choices=[
                           "1. Create habit",
                           "2. Manage habit",
                           "3. Check off habit",
                           "4. Show my analytics",
                           "5. Exit"
                       ]).ask()  # Prompt the user for a choice of action from a list

    if choice == "1. Create habit":
        habit_name = qt.text("What name would you like to give your habit?").ask()  # Prompt for habit name
        habit_category = qt.text("What category would you like to give to your habit:").ask()  # Prompt for habit category
        habit_periodicity = qt.select("How many times do you want to do this task",
                                      choices=["Daily", "weekly", "Monthly"]).ask().lower()  # Prompt for habit periodicity
        habit = Habit(habit_name, habit_category, habit_periodicity)  # Create an instance of the Habit class
        habit.add()  # Add the habit to the database

    elif choice == "2. Manage habit":
        print("What would you like to do?")
        while True:
            print("1. Delete habit")
            print("2. Delete category")
            print("3. Modify periodicity")
            print("4. Go Back to the Menu")

            sub_choice = input("Enter your choice (1-4): ")  # Prompt for a sub-choice

            if sub_choice == "1":
                try:
                    habit_name = get.habits_from_db(db)
                    habit = Habit(habit_name)
                    habit.delete()
                # Code to delete the habit goes here
                except ValueError:
                    print("habit not deleted ")
            elif sub_choice == "2":
                try:
                    habit_category = get.defined_categories()
                    category_to_delete = Habit(db, habit_category)
                    category_to_delete.delete_category()
                    # Code to delete the category goes here
                    print(f"The category '{habit_category}' has been deleted.")
                except ValueError:
                    print("category not deleted ")

            elif sub_choice == "3":
                habit_name = get.habits_from_db(db)
                # Code to modify periodicity goes here
                if not habit_name:  # Check if database is empty
                    print("\nDatabase empty; Please add a habit first.\n")
                else:
                    print(f"Selected habit name: {habit_name}")
                    new_periodicity = qt.select("What would you like to change the periodicity to?",
                                                choices=["Daily", "Weekly", "Monthly"]).ask()
                    if qt.confirm(
                            f"Are you sure you want to change the periodicity of {habit_name} to {new_periodicity}!").ask():
                        habit = Habit(habit_name, new_periodicity)
                        habit.update_periodicity()
                        print(f"\nPeriodicity of {habit_name} changed to {new_periodicity}!\n")
                    else:
                        print(f"\nPeriodicity of {habit_name} remains unchanged! Thanks for confirming.\n")

            elif sub_choice == "4":
                print("Returning to the main menu...")
                cli()  # Call the cli() function to return to the main men
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    if choice == "3. Check off habit":
        # Code to check off a habit goes here
        try:
            habit_name = get.habits_from_db(db)

            habit = Habit(habit_name)
            habit.checked_off_habit()
        except (ValueError, TypeError, AttributeError) as e:
            print(f"Error: {e}")

    if choice == "4. Show my analytics":
        options = [
            "1. All your current habits with their details.",
            "2. All habits with a same time-period",
            "3. The longest streak you have out of all your current habits.",
            "4. The longest streak you've had for a specific habit.",
        ]
        analytics_choice = qt.select("Which analytics do you want to see?", choices=options).ask()   # Prompt for an analytics choice

        if analytics_choice == options[0]:
            habits_list(db)  # Call the habits_list() function to display all current habits
        elif analytics_choice == options[1]:
            time_period = qt.select("View",
                                    choices=[
                                        "Daily Habits",
                                        "Weekly Habits",
                                        "Monthly Habits",
                                        "Back to Main Menu"
                                    ]).ask()  # Prompt for a time period choice

            if time_period == "Daily Habits":
                habits_by_period(db, "daily")  # Call the habits_by_period() function with "daily" as the period
            elif time_period == "Weekly Habits":
                habits_by_period(db, "weekly")  # Call the habits_by_period() function with "weekly" as the period
            elif time_period == "Monthly Habits":
                habits_by_period(db, "monthly")  # Call the habits_by_period() function with "monthly" as the period

        elif analytics_choice == options[2]:
            longest_streak_all_habits = analytics.longest_streak_all_habits(db)  # Get the longest streak for all habits
            print(f"The longest streak you have out of all your current habits is {longest_streak_all_habits}.")

        elif analytics_choice == options[3]:
            habit_name = get.habits_from_db(db)  # Prompt for a habit name
            if habit_name is not None:
                longest_streak = analytics.habit_longest_streak(db, habit_name)  # Get the longest streak for the specified habit
                if longest_streak is not None:
                    print(f"The longest streak for habit {habit_name} is {longest_streak}.")
                else:
                    print(f"No streaks found for habit {habit_name}.")
            else:
                print("No habits found in the database.")

    elif choice == "5. Exit":
        print("\nYou have successfully exited the program. Goodbye!")
        sys.exit()  # Exit the program


stop = True

if __name__ == '__main__':
    cli()  # Call the cli() function if the script is executed directly
